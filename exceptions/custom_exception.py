from exceptions.codes import ExceptionCode


class CustomException(Exception):
    def __init__(self, exception_code=None, status_code=500, payload=None, response_code=1999,
                 message="Internal Server Error. Please try again later"):
        Exception.__init__(self)
        self.message = exception_code.value['message'] if exception_code else message
        self.status_code = exception_code.value['status_code'] if exception_code else status_code
        self.response_code = exception_code.value['response_code'] if exception_code else response_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

    def __repr__(self) -> str:
        return super().__repr__()


