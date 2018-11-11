from flask import Flask
from flask_restful import Api, Resource, reqparse
import model

analyzer = model.load_analyzer()

class Analyze(Resource):
    def get(self, sentence):
        return analyzer.analyze(sentence), 200

app = Flask(__name__)
api = Api(app)

api.add_resource(Analyze, "/analyze/<string:sentence>")

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

app.run(debug=False, host='0.0.0.0', port=8080)