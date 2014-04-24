from picklecache.cache import downloader
from picklecache.defaults import get

def test_get_success():
    fake_warehouse = {}
    url = 'http://a.b/c'
    expected_response = 88
    observed_response = get(fake_warehouse, url, requests_get = lambda _: int(expected_response))
    n.assert_equal(observed_response, expected_response)
    n.assert_tuple_equal(fake_warehouse[url], (None, expected_response))

def test_get_error():
    fake_warehouse = {}
    url = 'http://a.b/c'

    error = ValueError('This is a test.')
    def fake_get(_):
        raise error

    try:
        get(fake_warehouse, url, requests_get = fake_get)
    except ValueError:
        n.assert_tuple_equal(fake_warehouse[url], (error, None))
    else:
        raise AssertionError('An error should have been raised.')

