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