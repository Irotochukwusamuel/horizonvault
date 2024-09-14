import decimal
import json

from flask import jsonify


class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        return super(DecimalEncoder, self).default(o)


def return_json(output):
    del_keys = []
    for k, v in output.__dict__.items():
        if not v and k != 'data':
            del_keys.append(k)
    for k in del_keys:
        del output.__dict__[k]
    # jsonStr = json.dumps(output.__dict__, cls=DecimalEncoder)
    return jsonify(output.__dict__)


class OutputObj:
    def __init__(self,
                 message="There's some error processing your request. Please try again later",
                 token='',
                 code=200,
                 status='0',
                 response_code=90000,
                 profile={},
                 data={}
                 ):
        self.message = message
        self.token = token
        self.code = code
        self.response_code = response_code
        self.status = status
        self.profile = profile
        self.data = data
