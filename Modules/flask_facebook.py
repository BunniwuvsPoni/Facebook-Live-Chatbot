from dotenv import dotenv_values
from flask import Flask, request, jsonify
import json, requests

# Load secrets
my_secrets = dotenv_values(".env")
FACEBOOK_PAGE_ACCESS_TOKEN = my_secrets["FACEBOOK_PAGE_ACCESS_TOKEN"]
FACEBOOK_VERIFY_TOKEN = my_secrets["FACEBOOK_VERIFY_TOKEN"]

# This is API key for Facebook messenger.
API = "https://graph.facebook.com/LATEST-API-VERSION/me/messages?access_token="+ FACEBOOK_PAGE_ACCESS_TOKEN

# Configure flask
app = Flask(__name__)

# Configure flask route
@app.route("/", methods=['GET'])
def facebook_verify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == FACEBOOK_VERIFY_TOKEN:
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200


@app.route("/", methods=['POST'])
def facebook_webhook():
    data = request.get_json()
    print(data)
    try:
        # Read messages from facebook messanger.
        message = data['entry'][0]['messaging'][0]['message']
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']
        if message['text'] == "hi":
            request_body = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "hello, world!"
                }
            }
            response = requests.post(API, json=request_body).json()
            return response

# Main execution
if __name__ == '__main__':
    app.run()