__version__ = '0.0.3'

try:
    # Python 3
    from picklecache.picklecache import cache
except ImportError:
    # Python 2
    from picklecache import cache
