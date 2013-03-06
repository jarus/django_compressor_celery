from setuptools import setup, find_packages

setup(
    name="django_compressor_celery",
    version="0.1",
    url='http://github.com/jarus/django_compressor_celery/',
    license='MIT',
    description="",
    long_description="",
    author='Christoph Heer',
    author_email='christoph.heer@googlemail.com',
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
    ],
)
