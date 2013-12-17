from setuptools import setup, find_packages
import os

version = '2.3.2dev'

setup(name='Products.FileSystemSite',
      version=version,
      description="File system based site",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("Products", "FileSystemSite", "HISTORY.txt")).read(),
      classifiers=[
              "Framework :: Zope2",
              "License :: OSI Approved :: Zope Public License",
              "Programming Language :: Python",
              "Topic :: Software Development :: Libraries :: Python Modules",
              ],
      keywords='file system site zope2',
      author='Zope community',
      author_email='info@infrae.com',
      url='http://infrae.com/products/silva',
      license='ZPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Zope2',
          ],
      )