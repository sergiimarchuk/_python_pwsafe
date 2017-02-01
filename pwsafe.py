#!/usr/bin/python

import sys
import pexpect
import random
import os

def get_passwd():
    """Generates password for Oracle.
    Password should begins with letter
    Password should contain only letters and numbers

    Returns:
        final_pass: random password
    """

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    pw_length = 11
    first_letter = ""
    mypw = ""

    first_letter_index = random.randrange(len(letters))
    first_letter = letters[first_letter_index]

    for i in range(pw_length):
            next_index = random.randrange(len(alphabet))
            mypw = mypw + alphabet[next_index]

    final_pass = str(first_letter) + str(mypw)
    return final_pass

def add_user():
    """Adds user with random password to pwsafe database

    Args:
        pwfile: pwsafe database file
        newuser: user name to create

    Returns:
        string: user was added or error info
        exitcode: sucess or not
    """

    pwfile = sys.argv[1]
    newuser = sys.argv[2]

    if not os.path.isfile(pwfile):
        print("Error: files does not exists")
        sys.exit(1)

    try:
        if len(newuser) > 3: 
            password = get_passwd()
            child = pexpect.spawn("pwsafe -f %s --add %s" % (pwfile,newuser))
            child.expect ('passphrase')
            child.sendline ('123456')
            child.expect ('group')
            child.sendline ('admin')
            child.expect ('username:')
            child.sendline (newuser)
            child.expect ('password')
            child.sendline (password)
            child.expect ('again:')
            child.sendline (password)
            child.expect ('notes:')
            child.sendline ('admin user')
            child.expect(pexpect.EOF)
            print("User   " + newuser + "    was created in pwsafe.")
            sys.exit(0)

        else:
            print('Error: Please provide valide path and username (more than 3 characters).')
            print('    Usage: ./pwsafe.py <pwsafe db file> <username>')
            sys.exit(1)
    except IndexError:
        print('Error: Please provide valide path and username.')
        print('    Usage: ./pwsafe.py <pwsafe db file> <username>')
        sys.exit(1)

if __name__ == '__main__':
    add_user()

