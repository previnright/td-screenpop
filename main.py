#Created by: Phillip Zeelig

from flask import Flask, jsonify, abort, make_response, request, url_for, json, render_template, session
from flask_socketio import SocketIO, send, emit
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
# app.config.from_object('config')
socketio = SocketIO(app)

# @socketio.on('msg')
# def receivedMessage(msg):
# 	print('Received: ' + msg)
	# send(msg, broadcast=True, namespace='/')

@socketio.on('message')
def sentMessage(message):
    send(message, broadcast=True, namespace='/')

@app.route('/socket')
def socket():
	return render_template('data.html')

@app.route('/', methods=['POST', 'GET'])
def webhook():

	if request.method == 'POST':
	    if not request.json:
	        abort(400)
	    test = {
	        "contact_phone_number": request.json["contact_phone_number"],
	        "call_id": request.json["call_id"],
	        "url": request.json["url"]
	    }
	    print(test)
	    # print(test["contact_phone_number"])
	    test2 = json.dumps(test)
	    test3 = str(test)
	    test3 = 'Sent: ' + test3
	    sentMessage(test3)
	    return jsonify(test), 201

	else:
		print("hello terminal")
		return "hello web"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    # app.run(debug=True)
    socketio.run(app, host='0.0.0.0', port=8080)
