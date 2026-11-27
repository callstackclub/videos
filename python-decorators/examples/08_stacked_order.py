def make(tag):
    def decorator(fn):
        print(f'apply {tag}')
        def wrapper():
            print(f'enter {tag}')
            fn()
            print(f'exit {tag}')
        return wrapper
    return decorator

@make('top')
@make('bottom')
def job():
    print('job')

job()