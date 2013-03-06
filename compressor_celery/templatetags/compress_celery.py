from django import template
from compressor.conf import settings
from compressor.templatetags.compress import OUTPUT_MODES, \
    OUTPUT_FILE, OUTPUT_INLINE
from compressor.templatetags.compress import CompressorNode

from compressor_celery.tasks import render_output_task
register = template.Library()


class CompressorNode(CompressorNode):

    # This method is copied from Jannis original code except for the
    # part with celery
    def render_compressed(self, context, kind, mode, forced=False):
        # See if it has been rendered offline
        cached_offline = self.render_offline(context, forced=forced)
        if cached_offline:
            return cached_offline

        # Take a shortcut if we really don't have anything to do
        if ((not settings.COMPRESS_ENABLED and
             not settings.COMPRESS_PRECOMPILERS) and not forced):
            return self.get_original_content(context)

        context['compressed'] = {'name': getattr(self, 'name', None)}
        compressor = self.get_compressor(context, kind)

        # Prepare the actual compressor and check cache
        cache_key, cache_content = self.render_cached(compressor, kind, mode, forced=forced)

        if cache_content is not None:
            return cache_content
        else:
            # There is no cache, start celery task
            content = self.get_original_content(context)
            render_output_task.delay(cache_key, content, kind, mode)

        # Or don't do anything in production
        return self.get_original_content(context)


# The compress function is copied from Jannis original implementation
@register.tag
def compress(parser, token):
    nodelist = parser.parse(('endcompress',))
    parser.delete_first_token()

    args = token.split_contents()

    if not len(args) in (2, 3, 4):
        raise template.TemplateSyntaxError(
            "%r tag requires either one, two or three arguments." % args[0])

    kind = args[1]

    if len(args) >= 3:
        mode = args[2]
        if not mode in OUTPUT_MODES:
            raise template.TemplateSyntaxError(
                "%r's second argument must be '%s' or '%s'." %
                (args[0], OUTPUT_FILE, OUTPUT_INLINE))
    else:
        mode = OUTPUT_FILE
    if len(args) == 4:
        name = args[3]
    else:
        name = None
    return CompressorNode(nodelist, kind, mode, name)
