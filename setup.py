from distutils.core import setup

from picklecache import __version__

setup(name='picklecache',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Cache functions with pickle and files',
      url='https://github.com/tlevine/request_pickles',
      packages=['picklecache'],
      install_requires = ['pickle_warehouse'],
      tests_require = ['nose'],
      version=__version__,
      license='AGPL',
)
