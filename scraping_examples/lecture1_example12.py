'''
lecture1_example12.py. This example imports the requests library and
sends a POST request to a login form. Note that no real login form
is used for this example. Additionally, note that many websites prohibit
login form POST requests in the robots.txt file. Finally, POST requests 
may also be sent via Selenium, as lecture1_example10.py demonstrates.
'''

import requests

params = {'vb_login_username':'user@gmail.com', 'vb_login_password':\
'password'} 
r = requests.post("https://www.example.com/...", data=params)
print r.text