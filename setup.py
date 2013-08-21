import codecs
from setuptools import setup, find_packages

def get_long_description():
    return codecs.open("README.rst", "r", "utf-8").read()

setup(
    name="django_compressor_celery",
    version="0.2",
    url='http://github.com/jarus/django_compressor_celery/',
    license='MIT',
    description="Integrate django_compressor with celery",
    long_description=get_long_description(),
    author='Christoph Heer',
    author_email='christoph@thelabmill.de',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
    install_requires=[
        'django-compressor>=1.2',
        'django-celery>=3.0'
    ],
)
