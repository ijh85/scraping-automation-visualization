'''
lecture2_example9.py. This example first imports the twilio module, which
facilitates SMS and MMS messaging. It then demonstrates how to send
an error message that is conditional on the outcome of a program's
execution. Note that all credentials are examples and must be replaced.
'''

from twilio.rest import Client

error_status = 0
message_target = 1

def sendMessage(error_status, message_target):
	account_sid = "ACXXXXXXXXXXXXXXXXX"
	auth_token = "YYYYYYYYYYYYYYYYYY"
	to_number = generateTarget(message_target)
	twilio_number = "+YYYYYYYYYYYY"
	body_message = generateMessage(error_status)
	client = Client(account_sid, auth_token)
	client.api.account.messages.create(
		to = to_number,
		from_ = twilio_number,
		body = body_message)
           
def generateMessage(error_status): 
	if error_status == 0:
		body_message = "No errors."
	else:
		body_message =	"Program failed."
	return body_message           
           
def generateTarget(message_target): 
	if message_target == 0:
		to_number = "+XXXXXXXXXXXX"
	else:
		to_number =	"+ZZZZZZZZZZZZ"
	return to_number
	
sendMessage(error_status, message_target)	          