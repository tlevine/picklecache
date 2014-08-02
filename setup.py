from distutils.core import setup

setup(name='picklecache',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='Cache functions with pickle and files',
      url='https://github.com/tlevine/picklecache',
      packages=['picklecache'],
      install_requires = ['pickle_warehouse'],
      tests_require = ['nose'],
      version='0.0.5',
      license='AGPL',
)
