from flask import Flask, make_response, request, jsonify
from flask.views import MethodView
from flask_cors import CORS

from service import OperationService

app = Flask(__name__)
cors = CORS(app, resources={"/api/operations": {"origins": "*"}})


class OperationsApi(MethodView):
    """/api/operations"""
    @staticmethod
    def get():
        print("this is getting called")
        result = OperationService.calculate(data=request.json)
        if isinstance(result, int):
            return make_response(jsonify(result), 200)
        return make_response(jsonify(result), 400)


app.add_url_rule("/api/operations", view_func=OperationsApi.as_view("operations_api"))

if __name__ == '__main__':
    app.run(debug=True)
