To Dos
======


In-Progress
-----------

- [ ] Warn of missing gpg command if not there and needed then exit
- [ ] If not a valid file path, then assume its an otpauth uri string or a base32 secret key string
- [ ] Check whether input is a valid `otpauth` file as specified by [Google's Spec][01]
- [ ] Strip all other data besides the `secret=BASE32_ENCODED_SECRET`
- [ ] If not valid otpauth, check if valid secret *i.e. is base32 encoded*
    - Normally it's all upper case, but let's just move it all to upper case
    - Check that only the number digits `2~7` are in use, as per [RFC3548][02]
- [ ] Check if `oathtool` installed before trying to use it to through shell to generate the TOTP code
    - If it's there assume it's a 6 digit base32 code


Planning
--------

- [ ] Handle 6~8 digits as per [Google's Spec][01]
- [ ] Handle periods beyond the standard 30s
- [ ] Better README
    - [ ] Basic Usage Section
    - [ ] Install Section
    - [ ] Dependencies Section
- [ ] Handle stdin when popup hooks aren't helping input for `gpg --decrypt`


Considering
-----------

- [ ] PyAuth/PyOTP module
    - check if it exists on host system first, 
    - Consider hardcoding it or some easier way of distributing it
- [ ] GPG module from python
    - Consider `try`'ing the existance of the module first, if not `try` the shell command
- [ ] Verify secret for base32 validity


Completed
---------

- [x] Check if file path is a gpg encrypted file
- [x] Decrypt (using shell gpg for now)
- [x] Check if input is valid file path
- [x] Initial README


[01]: https://github.com/google/google-authenticator/wiki/Key-Uri-Format "Github: Google/Google-Authenticator - Key URI Format Wiki Entry"
[02]: http://tools.ietf.org/html/rfc3548 "Network Working Group: Base16, Base32, & Base64 RFC3548 Encoding Standard"
