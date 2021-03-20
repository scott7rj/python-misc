def html_tag(tag):
    def wrap_text(msg):
        print(f"<{tag}>{msg}</{tag}>")
    return wrap_text


def outer_func(msg):
    message = msg
    def inner_func():
        print(message)
    return inner_func


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('added before functionality to wrapper')
        return original_function(*args, **kwargs)
    return wrapper_function


class Decorator(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print('call method before functionality to wrapper')
        return self.original_function(*args, **kwargs)

@decorator_function
def display():
    print('display function ran')


@decorator_function
def display_info(name, age):
    print(f"display info ran with arguments {name}, {age}")


@Decorator
def display2():
    print('display function ran')


@Decorator
def display_info2(name, age):
    print(f"display info ran with arguments {name}, {age}")


def main():
    h1 = html_tag('h1')
    h1('Hello World')

    html_tag('h1')('Hello World2')

    my_func = outer_func('xpto')
    print(my_func.__name__)
    my_func()
    outer_func('xpto2')()
    print('-----')
    display()
    display_info('john doe', 44)
    print('-----')
    display2()
    display_info2('mary jane', 33)

if __name__ == '__main__':
    main()