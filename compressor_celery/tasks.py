from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from celery import task

from compressor.templatetags.compress import CompressorMixin
from compressor.utils import get_class
from compressor.cache import cache_set, cache_get

task_config = {
    'ignore_result': True
}
task_config.update(getattr(settings, 'COMPRESS_CELERY_TASK_CONFIG', {}))

@task(**task_config)
def compress(cache_key, content, kind, mode):
    logger = compress.get_logger()

    if cache_get(cache_key) is not None:
        logger.debug('No update required for %s', cache_key)
        return

    compressors = CompressorMixin().compressors
    compressor = get_class(compressors.get(kind),
                           exception=ImproperlyConfigured)
    compressor = compressor(content=content)
    output = compressor.output(mode)
    cache_set(cache_key, output)

    logger.debug("Successfully updated cache key %s", cache_key)
