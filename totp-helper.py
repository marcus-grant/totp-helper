#!/usr/bin/env python3

import os
import subprocess as sp
import sys


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        sys.exit('A filepath or TOTP secret key is needed as an argument')
    arg_is_file = True
    totp_str = None
    totp_secret = ''
    totp_is_encrypted = False
    gpg_present = True
    try:
        cmd_res = sp.run(["gpg", "--decrypt", args[0]], capture_output=True)
        totp_is_encrypted = cmd_res.returncode == 0
        totp_str = cmd_res.stdout.decode('UTF-8')
    except:
        gpg_present = False
    if not totp_is_encrypted:
        try:
            with open(args[0]) as f:
                totp_str = f.read()
        except:
            arg_is_file = False
    if totp_str is None:
        totp_str = args[0]
    print(totp_str)
