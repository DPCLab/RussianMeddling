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

app.run(debug=False)