from django.core.exceptions import ImproperlyConfigured

from celery import task

from compressor.templatetags.compress import CompressorMixin
from compressor.utils import get_class
from compressor.cache import cache_set, cache_get


@task
def render_output_task(cache_key, content, kind, mode):
    if cache_get(cache_key) is not None:
        return 'No update required for %s' % cache_key

    compressors = CompressorMixin().compressors
    compressor = get_class(compressors.get(kind),
                           exception=ImproperlyConfigured)
    compressor = compressor(content=content)
    output = compressor.output(mode)
    cache_set(cache_key, output)
    return 'Cache key %s updated' % cache_key
