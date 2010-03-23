from setuptools import setup, find_packages

version = '1.0b17'

setup(name='plone.app.jquerytools',
      version=version,
      description="JQuery Tools Integration for Plone",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      classifiers=[
          "Framework :: Plone",
          "Programming Language :: Python",
        ],
      keywords='Plone JQuery',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.app.jquerytools',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'zope.component',
          'Products.CMFCore',
          'Products.GenericSetup',
          'Zope2',
      ],
      entry_points="""
          [z3c.autoinclude.plugin]
          target = plone
      """,
      )
