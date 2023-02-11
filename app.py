#Flask app for interacting with climbing instructor

from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from chefbot import ask, append_interaction_to_chat_log
import os

account_sid = os.getenv('TWSID')
auth_token = os.getenv('TW_API')

client = Client(account_sid,auth_token)
app = Flask(__name__)
# if for some reason your conversation with the chef gets weird, change the secret key 
app.config['SECRET_KEY'] = 'Falling!!!!'

@app.route('/chefbot', methods=['POST'])
def chef():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)
    
    msg = MessagingResponse()
    print(msg)
    msg = msg.message(answer)

    return str(msg)
    

if __name__ == '__main__':
    app.run(debug=True)