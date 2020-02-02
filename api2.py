from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

data_dic = []

class People(Resource):
    def get(self, name):
        for x in data_dic:
            if x['Data'] == name:
                return x
        return {"Data" : "none"}

    def post(self, name):
        Tem = {'Data':name}
        data_dic.append(Tem)
        return Tem
    
api.add_resource(People, '/Name/<string:name>')

if __name__ == '__main__':
    app.run(debug = True)
