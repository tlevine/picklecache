from picklecache.cache import downloader

def test_downloader_success():
    fake_warehouse = {}
    url = 'http://a.b/c'
    get = downloader(lambda _: int(expected_response), fake_warehouse)

    expected_response = 88
    observed_response = get(url)
    n.assert_equal(observed_response, expected_response)
    n.assert_tuple_equal(fake_warehouse[url], (None, expected_response))

def test_get_error():
    fake_warehouse = {}
    url = 'http://a.b/c'

    error = ValueError('This is a test.')
    def fake_get(_):
        raise error
    get = downloader(fake_get, fake_warehouse)

    try:
        get(fake_warehouse, url, requests_get = fake_get)
    except ValueError:
        n.assert_tuple_equal(fake_warehouse[url], (error, None))
    else:
        raise AssertionError('An error should have been raised.')

