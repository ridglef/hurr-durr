import orjson as orjson
from flask import Flask, request

app = Flask(__name__)

@app.route('/push')
def push():
    if (len(request.args.get('Author')) + len(request.args.get('Message')) >= 256):
        return 'Message Is Too Long!'
    with open('data.json', 'rb') as file:
        json_data = orjson.loads(file.read())

        json_data["Beans"].append({"Author": request.args.get('Author'), "Message": request.args.get("Message")})

        if len(json_data["Beans"]) > 8:
            json_data["Beans"].pop(0)

    with open('data.json', 'wb') as file:
        file.write(orjson.dumps(json_data))

    return 'Message Submitted!'


@app.route('/get')
def get():
    with open('data.json', 'rb') as file:
        json_data = orjson.loads(file.read())
    return json_data
