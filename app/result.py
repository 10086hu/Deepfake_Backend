from flask import jsonify


class Result:
    @staticmethod
    def ok(data=None, message="success", code=200):
        return jsonify({"code": code, "message": message, "data": data}), code

    @staticmethod
    def fail(data=None, message="error", code=400):
        return jsonify({"code": code, "message": message, "data": data}), code