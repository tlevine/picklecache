from distutils.core import setup

__version__ = '0.0.1'

setup(name='request_pickles',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Download stuff with python-requests, pickling the responses and errors',
      url='https://github.com/tlevine/request_pickles',
      packages=['request_pickles'],
      install_requires = ['pickle_warehouse'],
      extras_require = [],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
