from flask import Flask, request, json, jsonify
import os
import webbrowser

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/webhook', methods=['POST'])
def webhook():
	if request.headers['Content-Type'] == 'application/json':
		my_info = json.dumps(request.json)
		# print(my_info)
		# webbrowser.open('https://app.procedureflow.com')
		enter_number = 14086494479
		obj = json.loads(my_info)
		numb = obj["contact_phone_number"]
		no_plus = numb.strip('+')
		to_int = int(no_plus)
		print("Contact Phone Number Calling:", to_int)

		if to_int == enter_number:
			webbrowser.open('https://app.procedureflow.com')
			print("Number is equal, open Procedure Flow")

		else:
			webbrowser.open('https://google.com')
			print("Number is not equal, open Google")		

		return my_info

@app.route('/testing')
def testing():
	
	enter_number = 14086494479

	data = '{"contact_phone_number": "+14086494479"}'
	obj = json.loads(data)
	numb = obj["contact_phone_number"]
	no_plus = numb.strip('+')
	to_int = int(no_plus)
	print(to_int)

	if to_int == enter_number:
		print("Number is equal, open Procedure Flow")
		webbrowser.open('https://app.procedureflow.com')	

	else:
		print("Number is not equal, open Google")
		webbrowser.open('https://google.com')
		
	return data


if __name__ == '__main__':
	app.run(debug=True)