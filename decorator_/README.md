### Decorator
    '''
    def up_(func):
        def wrapper(text):
            return func(text.upper())
        return wrapper
    '''

### Wrapper
    '''
    @up_
    def show(text):
        return text
    '''

### Run
    '''
    >>> show('hello')
    'HELLO'
    > 
    >>> show('mama')
    'MAMA'
    '''