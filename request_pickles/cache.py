import requests

def downloader(func, warehouse):
    '''
    func :: anything -> response
    '''
    def download(*args, **kwargs):
        if url in warehouse:
            output = warehouse[url]
        else:
            try:
                response = func(*args, **kwargs)
            except Exception as error:
                output = error, None
            else:
                output = None, response
            warehouse[url] = output
        error, response = output
        if error == None:
            return response
        else:
            raise error
    return download

get = functools.partial(downloader, requests.get)
post = functools.partial(downloader, requests.post)
