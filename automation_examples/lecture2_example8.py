'''
lecture2_example8.py. This example first imports the Internet Message
Access Protocol (imap). It then establishes a connection with a
mail server using generic credentials. It requests the contents
of all undeleted emails in the inbox folder.
'''

import imapclient

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('user@gmail.com', 'password')
imapObj.select_folder('INBOX')
messages = imapObj.search(['NOT','DELETED'])