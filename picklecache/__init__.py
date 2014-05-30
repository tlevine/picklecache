try:
    # Python 3
    from picklecache.picklecache import cache
except ImportError:
    # Python 2
    from picklecache import cache
