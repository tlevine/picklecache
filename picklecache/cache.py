def downloader(func, warehouse):
    '''
    func :: a -> b
    warehouse :: dict-like
    
    Returns a function with warehouse cache :: a -> b
    '''
    def download(*args, **kwargs):
        if args in warehouse:
            output = warehouse[args]
        else:
            try:
                response = func(*args, **kwargs)
            except Exception as error:
                output = error, None
            else:
                output = None, response
            warehouse[args] = output
        error, response = output
        if error == None:
            return response
        else:
            raise error
    return download
