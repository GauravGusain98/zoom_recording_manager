from flask import request, jsonify
from zoom_recording_manager import app
from . import services


@app.route('/')
def home():
    return '<div>Welcome to Zoom Recording Manager developed by <a href="https://coloredcow.com">ColoredCow Team</a></div>.'

@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == "POST":
        # try:
        jsonData = request.get_json()
        webhook_handler = services.webhook_handler.WebhookHandler()
        webhook_handler.capture_webhook(jsonData)
        # except:
            # return jsonify(message="Something went wrong!"), 400
        return jsonify(message="Success"), 200
    else:
        return jsonify(message="Currently, the system do not accept a GET request"), 405
    
