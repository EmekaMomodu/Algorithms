# decorator example

def my_double_args(func):
    def multiply_args_by_two(*args):
        func(args[0] * 2, args[1] * 2)
    return multiply_args_by_two


@my_double_args
def my_mult(x, y):
    print(x * y)
    return x * y

import base64
from itertools import cycle


def decrypt(encrypted_message, encryption_key):
    base64_decoded              = base64.b64decode(encrypted_message)
    decrypted_message           = [''] * len(base64_decoded)
    encryption_key_iterator     = cycle(encryption_key)
    for i, c in enumerate(base64_decoded):
        decrypted_message[i] += chr(ord(c) ^ ord(encryption_key_iterator.next()))
    return ''.join(decrypted_message)




if __name__ == '__main__':
    # encryption_key = 'chukwuemeka'
    # encrypted_message = 'HkoWHgJNCBweSERPRUoCGQRPGUhBT0MWCgEJDgBJGApKT15VQggWHwRLAAoJSEhVQggDDQ5cGRxK T15VQgQLCBNLCQYPAwFSSU1CCgJGBAobCgkQCxlCS1sOShoDAwsWDggBTE0OSh0MDQYcER5CS1sO ShwMCQFSSU1CDQ5BSk9XT0MCDANETBw='
    #
    # decrypted_message = decrypt(encrypted_message, encryption_key)
    # print(decrypted_message)

    # !/usr/bin/env python
    # -*- coding: utf-8 -*-

    import base64

    MESSAGE = '''
    HkoWHgJNCBweSERPRUoCGQRPGUhBT0MWCgEJDgBJGApKT15VQggWHwRLAAoJSEhVQggDDQ5cGRxK T15VQgQLCBNLCQYPAwFSSU1CCgJGBAobCgkQCxlCS1sOShoDAwsWDggBTE0OSh0MDQYcER5CS1sO ShwMCQFSSU1CDQ5BSk9XT0MCDANETBw=
    '''

    KEY = 'emeka.momodu'

    result = []
    for i, c in enumerate(base64.b64decode(MESSAGE)):
        result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

    print
    ''.join(result)

    # my_mult(1, 1)
