#! coding: utf-8

from distutils.core import setup

version = __import__('simple_faq').__version__
install_requires = open('requirements.txt').readlines(),

setup(
    name='django-simple-faq',
    version=version,
    author='Leandro Gomez',
    author_email='lgomez@devartis.com',
    packages=['simple_faq', ],
    url='http://github.com/devartis/django-simple-faq/',
    license=open('LICENSE.txt').read(),
    description='Simple FAQ app for django',
    long_description=open('README.md').read(),

    download_url='http://pypi.python.org/packages/source/D/django-simple-faq/django-simple-faq-%s.tar.gz' % version,

    install_requires=install_requires,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)

__author__ = 'lgomez'
