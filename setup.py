from setuptools import setup, find_packages
import sys, os

version = '1.2.2'

shortdesc = "Base common calendaring features: Convinience or not coverd yet."
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(name='bda.calendar.base',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 4 - Beta',
            'Environment :: Web Environment',
            'Framework :: Zope2',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',            
      ], # http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='Calendaring',
      author='Jens Klein, Robert Niedereiter',
      author_email='dev@bluedynamics.com',
      url=u'http://svn.plone.org/svn/collective/bda.calendar.base',
      license='General Public Licence',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['bda', 'bda.calendar'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'pytz',
          'zope.interface',              
          # -*- Extra requirements: -*
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )