'''
lecture2_example7.py. This example first imports the Simple Mail Transfer
Protocol (smtplib) module. It then establishes a connection to a mail server
and sends an email. Note that the account details and message are an example
and must be replaced.
'''

import smtplib

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('user@gmail.com', 'PASSWORD') 
smtpObj.sendmail('user@gmail.com', 'other.user@gmail.com',\
'Subject: Test. Dear Other User, This is a a test. Sincerely, User')