import functools

from pickle_warehouse import Warehouse
import requests

from picklecache.cache import downloader

get = functools.partial(downloader, lambda x: requests.get(x), Warehouse('get'))
