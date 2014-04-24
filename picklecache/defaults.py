from pickle_warehouse import Warehouse
import requests

from picklecache.cache import downloader

get = downloader(lambda x: requests.get(x), Warehouse('get', mutable = False))
