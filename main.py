from flask import Flask, request, json, jsonify
import os
import webbrowser

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
	if request.headers['Content-Type'] == 'application/json':
		my_info = json.dumps(request.json)
		web = '{"url": "https://app.procedureflow.com"}'
		print(my_info)
		print(web)

		return web

if __name__ == '__main__':
	app.run(debug=True)