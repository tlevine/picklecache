from tempfile import mkdtemp

import nose.tools as n
from pickle_warehouse import Warehouse

from picklecache import cache

def test_new_success():
    tmp = mkdtemp()
    warehouse = Warehouse(tmp)
    url = 'http://a.b/c'

    @cache(tmp)
    def get(_):
        return 88

    observed_response = get(url)
    n.assert_equal(observed_response, 88)
    n.assert_tuple_equal(warehouse[(url,)], (None, 88))

def test_old_success():
    tmp = mkdtemp()
    warehouse = Warehouse(tmp)
    url = 'http://a.b/c'
    warehouse[url] = (None, 88)

    @cache(tmp)
    def get(_):
        raise AssertionError('This should not run.')

    observed_response = get(url)
    n.assert_equal(observed_response, 88)
    n.assert_tuple_equal(warehouse[(url,)], (None, 88))

def test_cache_error():
    tmp = mkdtemp()
    warehouse = Warehouse(tmp)
    url = 'http://a.b/c'

    @cache(tmp)
    def get(_):
        return 88

    error = ValueError('This is a test.')
    def fake_get(_):
        raise error

    try:
        get(url)
    except ValueError:
        n.assert_tuple_equal(warehouse[(url,)], (error, None))
    else:
        raise AssertionError('An error should have been raised.')

