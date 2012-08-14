import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()
version = open(os.path.join("w20e", "pycms_events", "version.txt")
               ).readlines()[0].strip()


requires = [
    'zope.interface',
    'w20e.pycms >= 1.1.0a'
    ]

setup(name='w20e.pycms_events',
      version=version,
      description='Pyramid CMS events package',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='D.A.Dokter',
      author_email='dokter@w20e.com',
      url='',
      keywords='web pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires = requires,
      message_extractors = { '.': [
          ('**.pt',   'lingua_xml', None ),
          ]},
      tests_require= requires,
      test_suite="w20e.pycms_events",
      entry_points = "",
      )
