#Created by: Phillip Zeelig

from flask import Flask, jsonify, abort, make_response, request, url_for, json
import json

app = Flask(__name__)

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
	    return jsonify(test), 201

	else:
		print("hello terminal")
		return "hello web"

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
