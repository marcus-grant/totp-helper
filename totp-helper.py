#!/usr/bin/env python3

import os
import sys


def is_valid_totp_file(totp_file):
    pass


def get_secret_from_str(totp_str):
    pass


if __name__ == '__main__':
    print(sys.argv)
    args = sys.argv[1:]
    print(args)
    if len(args) < 1:
        sys.exit('A filepath or TOTP secret key is needed as an argument')
    arg_is_file = True
    totp_str = args[0]
    totp_secret = ''
    try:
        with open(totp_str) as f:
            totp_str = f.read()
    except:
        arg_is_file = False
    if arg_is_file:
        print('The arg IS a file, it\'s contents:\n{}'.format(totp_secret))

