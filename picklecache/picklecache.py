def cache(*args, **kwargs):
    '''
    Decorate a function with this to cache it to a pickle_warehouse.Warehouse
    '''
    warehouse = Warehouse(*args, **kwargs):
    def decorator(func):
        def wrapper(*_args, **_kwargs):
            if _args in warehouse:
                output = warehouse[_args]
            else:
                try:
                    result = func(*_args, **_kwargs)
                except Exception as error:
                    output = error, None
                else:
                    output = None, result
                warehouse[_args] = output
            error, result = output
            if error == None:
                return result
            else:
                raise error
        return wrapper
    return decorator
