# decorator example

def my_double_args(func):
    def multiply_args_by_two(*args):
        func(args[0] * 2, args[1] * 2)
    return multiply_args_by_two


@my_double_args
def my_mult(x, y):
    print(x * y)
    return x * y


if __name__ == '__main__':
    my_mult(1, 1)
