#! coding: utf-8

from distutils.core import setup
import os

version = __import__('simple_faq').__version__
install_requires = open('requirements.txt').readlines(),

# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.

packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

PACKAGE = 'simple_faq'

for dirpath, dirnames, filenames in os.walk(PACKAGE):
    for i, dirname in enumerate(dirnames):
        if dirname in ['.', '..']:
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[len(PACKAGE) + 1:] # Strip package directory + path separator
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

setup(
    name='django-simple-faq',
    version=version,
    author='Leandro Gomez',
    author_email='lgomez@devartis.com',

    packages=packages,
    package_data={'simple_faq': data_files},

    url='http://github.com/devartis/django-simple-faq/',
    license=open('LICENSE.txt').read(),
    description='Simple FAQ app for django',
    long_description=open('README.md').read(),

    download_url='http://pypi.python.org/packages/source/d/django-simple-faq/django-simple-faq-%s.tar.gz' % version,

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
