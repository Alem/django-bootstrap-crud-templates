from setuptools import setup, find_packages
from os.path import dirname
import bsct

setup(
    name    = '%s' % bsct.__pkg_name__,
    version = bsct.__version__,
    author  = bsct.__author__,
    author_email = "alem@cidola.com",
    description  = bsct.__desc__,
    license      = bsct.__licence__,
    keywords     = "django, templates. bootstrap, bootstrap templates, crud templates",
    url          = "http://packages.python.org/%s" % bsct.__pkg_name__,
    packages     = find_packages(),
    include_package_data = True,
    long_description = open('README.rst').read(),
    classifiers  = [
         'Environment :: Web Environment',
         'Framework :: Django',
         'Intended Audience :: Developers',
         "License :: OSI Approved :: %s" % bsct.__licence__,
         'Operating System :: OS Independent',
         'Programming Language :: Python',
         'Programming Language :: Python :: 2.7',
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
