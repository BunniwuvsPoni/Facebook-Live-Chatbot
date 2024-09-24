from flask import Flask, request, jsonify
import json

# Configure flask
app = Flask(__name__)

# Hello, World!
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Calculate
@app.route('/compute/', methods=['GET'])
def compute():

    name = request.args.get('name')
    var1 = request.args.get('var1')
    var2 = request.args.get('var2')

    if not name or not var1 or not var2:
        return jsonify({'Error': 'Missing parameters'}), 400

    try:
        var1 = float(var1)
        var2 = float(var2)
    except ValueError:
        return jsonify({'Error': 'Invalid number format'}), 400

    response = {
        'name': name,
        'addition': var1 + var2,
        'subtraction': var1 - var2,
        'multiplication': var1 * var2,
        'division': var1 / var2 if var2 != 0 else 'undefined'
    }

    response = json.dumps(response, indent=4)

    return response, 200

if __name__ == '__main__':
    app.run()