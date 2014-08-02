import os
import shutil
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

def test_new_error():
    tmp = mkdtemp()
    warehouse = Warehouse(tmp)
    url = 'http://a.b/c'
    error = ValueError('This is a test.')

    @cache(tmp)
    def get(_):
        raise error

    try:
        get(url)
    except ValueError as e:
        n.assert_equal(str(e), str(error))
        n.assert_equal(str(warehouse[(url,)]), str((error, None)))
    else:
        raise AssertionError('An error should have been raised.')


def test_old_error():
    tmp = mkdtemp()
    warehouse = Warehouse(tmp)
    url = 'http://a.b/c'
    error = ValueError('This is a test.')
    warehouse[url] = (error, None)

    @cache(tmp)
    def get(_):
        raise AssertionError('This should not run.')

    try:
        get(url)
    except ValueError as e:
        n.assert_equal(str(e), str(error))
    else:
        raise AssertionError('An error should have been raised.')


def test_expanduser():
    try:
        shutil.rmtree(os.path.expanduser('~/.picklecache-test'))
    except:
        pass

    @cache('~/.picklecache-test')
    def a(_):
        return 3
    a('b')
    n.assert_true(os.path.isfile(os.path.expanduser('~/.picklecache-test/b')))

def test_function_name():
    try:
        shutil.rmtree('a_function')
    except:
        pass

    @cache()
    def a_function(_):
        return 3
    n.assert_true(os.path.isdir('a_function'))
