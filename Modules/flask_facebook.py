from dotenv import dotenv_values
from flask import Flask, request, jsonify
import json, requests

# Load secrets
my_secrets = dotenv_values(".env")
FACEBOOK_PAGE_ACCESS_TOKEN = my_secrets["FACEBOOK_PAGE_ACCESS_TOKEN"]
FACEBOOK_VERIFY_TOKEN = my_secrets["FACEBOOK_VERIFY_TOKEN"]
FACEBOOK_API_VERSION=my_secrets["FACEBOOK_API_VERSION"]

# This is API key for Facebook Messenger.
API = "https://graph.facebook.com/" + FACEBOOK_API_VERSION + "/me/messages?access_token="+ FACEBOOK_PAGE_ACCESS_TOKEN

# Configure flask
app = Flask(__name__)

# Configure flask route(s)
# [GET] - Hello, World! landing page
@app.route("/", methods=['GET'])
def hello_world():
    print("Page Triggered - [GET]: Hello, World!")
    return "Hello, World!", 200

# [GET] - Facebook Messenger Webhook verification
@app.route("/facebook_messenger_webhook", methods=['GET'])
def facebook_messenger_webhook_verification():
    print("Page Triggered - [GET]: Facebook Messenger Webhook verification")
    print(request.args)

    # Facebook Messenger Webhook verification happens here
    # request.args.get("hub.mode") == "subscribe"
        # This checks if the hub.mode parameter in the query string is set to "subscribe", which indicates a subscription request.
            # This value will always be set to subscribe.
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        # request.args.get("hub.verify_token")
            # This checks if the hub.verify_token parameter in the query string matches.
                # This value is configured in the:
                    # 1) Webhook on Facebook in the Developer App section
                    # 2) The .env file
        if not request.args.get("hub.verify_token") == FACEBOOK_VERIFY_TOKEN:
            return "Verification token missmatch", 403
        # Returns challenge value to Facebook provided that the above verification(s) matches.
        print("Returning challenge to Facebook: " + request.args['hub.challenge'])
        return request.args['hub.challenge'], 200

# [POST] - Facebook Messenger Webhook
@app.route("/facebook_messenger_webhook", methods=['POST'])
def facebook_messenger_webhook():
    print("Page Triggered - [POST]: Facebook Messenger Webhook")

    print("Request data:")
    data = request.get_json()
    print(data)

    ### Facebook Messenger Messenging ###

    try:
        # Read messages from Facebook Messenger.
        message = data['entry'][0]['messaging'][0]['message']

        # Get the Sender's ID to respond to
        sender_id = data['entry'][0]['messaging'][0]['sender']['id']

        # Set request_body to None
        request_body = None

        # Response is crafted here
        if message['text'].casefold() == "test":
            # Basic text response
            request_body = {
                "recipient": {
                    "id": sender_id
                },
                "message": {
                    "text": "Hello, World! - This is a test response from the chatbot..."
                }
            }
        elif message['text'].casefold() == "choice":
            # Quick reply
            request_body = {
                "recipient": {
                    "id": sender_id
                },
                "messaging_type": "RESPONSE",
                "message": {
                    "text": "Confirm your choice:",
                    "quick_replies": [
                        {
                            "content_type": "text",
                            "title": "Confirm",
                            "payload": "<POSTBACK_PAYLOAD>",
                            "image_url": "http://example.com/img/green.png"
                        }, {
                            "content_type": "text",
                            "title": "Cancel",
                            "payload": "<POSTBACK_PAYLOAD>",
                            "image_url": "http://example.com/img/red.png"
                        }
                    ]
                }
            }

        # Generated the HTTP POST request
        response = requests.post(API, json=request_body).json()

        # Send the request
        return response

    # Exception handling
    except Exception as e:
        print(f"An error occurred: {e}")

    ### Facebook Messenger Messenging ###

# Main execution
if __name__ == '__main__':
    app.run()