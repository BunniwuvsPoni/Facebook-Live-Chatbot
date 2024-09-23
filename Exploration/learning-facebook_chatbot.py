from dotenv import dotenv_values
from flask import Flask, request
import requests

# Load secrets
my_secrets = dotenv_values(".env")
FACEBOOK_PAGE_ACCESS_TOKEN = my_secrets["FACEBOOK_PAGE_ACCESS_TOKEN"]

# Create the Flask instance
app = Flask(__name__)

# This is API key for Facebook messenger.
API = "https://graph.facebook.com/LATEST-API-VERSION/me/messages?access_token="+ FACEBOOK_PAGE_ACCESS_TOKEN

@app.route("/", methods=['GET'])
def fbverify():
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token")== "<Your Verify token>":
            return "Verification token missmatch", 403
        return request.args['hub.challenge'], 200
    return "Hello world", 200