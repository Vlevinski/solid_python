### Decorator
    '''
    def up_(func):
        def wrapper(text):
            return func(text.upper())
        return wrapper
    '''

### Decorating
    '''
    @up_
    def show(text):
        return text
    '''

### Running
    '''
    >>> show('hello')
    'HELLO'
    > 
    >>> show('mama')
    'MAMA'
    '''