from flask import Flask, request, jsonify
import json

# Configure flask
app = Flask(__name__)

# Hello, World!
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Main execution
if __name__ == '__main__':
    app.run()