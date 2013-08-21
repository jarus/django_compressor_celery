django-compressor-celery
========================

A extension of django_compressor which compress the files by celery workers.
The system behind the scene is very simple. The first request on a page with a
``{% compress %}`` block will create a celery task which compress this specific block. 
Instead to wait for the compressed version the first request gets the uncompressed 
version. After the compress task is finished compressor will deliver the compressed
code from the server cache.

Benefits:
 - Support all features of template inheritance
 - No offline compression by deployment

Install
-------

* Install as usual `django-compressor <http://django-compressor.readthedocs.org/en/latest/quickstart/#installation>`_ and `celery for django <http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html>`_
* Install django-compressor-celery
* Add ``compressor_celery`` to your installed apps
* Replace in your template ``{% load compress %}`` with ``{% load compress_celery %}``

