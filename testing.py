from flask import Flask, jsonify, abort, make_response, request, url_for, json
import json

app = Flask(__name__)

data = {
    "contact_phone_number": "+14086494479",
    "call_id": '123',
    "url": "https://app.procedureflow.com"
}

@app.route('/', methods=['POST'])
def webhook():
    if request.headers['Content-Type'] == 'application/json':
        info = json.dumps(request.json)
        info2 = json.loads(info)
        # print(info2)
        print(info2["contact_phone_number"])
        print(info2["call_id"])
        print(info2["url"])
        post_data = {
            "contact_phone_number": info2["contact_phone_number"],
            "call_id": info2["call_id"],
            "url": info2["url"]
        }
        print(post_data)
        return jsonify(post_data), 201

@app.route('/get', methods=['GET'])
def get_tasks():
    return jsonify(data)

@app.route('/post', methods=['GET'])
def create_task():
    if not request.json:
        abort(400)
    test = {
        "contact_phone_number": request.json["contact_phone_number"],
        "call_id": request.json["call_id"],
        "url": request.json["url"]
    }
    print(test)
    return jsonify(test), 201

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)