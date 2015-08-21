#!/usr/bin/env python
#coding:utf-8
"""
  Author:  HieuHT --<>
  Purpose: Generate a auth.txt for openvpn
  Created: 08/19/2015
"""
import subprocess
import pyotp
import os, sys
def main():
    PATH = "/home/hieuht/Documents/openvpn/"
    openvpn_config = 'hieuht.ovpn'
    my_secret = 'I7OVM53OAIACLTAS'
    my_account = 'hieuht'
    my_password = '123456'

    auth = pyotp.TOTP(my_secret)
    my_otp = str(auth.now())
    my_valid_password = my_password+my_otp
    # Update Auth.txt
    f = open(PATH + 'auth.txt', 'w')
    f.write(my_account + '\n')
    f.write(my_valid_password + '\n')
    f.close()
    command = '/usr/sbin/openvpn %s' % PATH + openvpn_config
    proc = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell= True)
if __name__ == '__main__':
    if not os.geteuid()==0:
        sys.exit("\nOnly root can run this script\n")
    else:
        main()