from flask import jsonify


def error(http_code, error_code, message):
    assert isinstance(http_code,  int)
    assert isinstance(error_code, str)
    assert isinstance(message,    str)

    return (jsonify(status='Error', error_code=error_code, message=message), http_code)

def error_missed_argument(arg_name):
    return error(400, 'MISSED_ARGUMENT', 'Missed required argument: {}'.format(arg_name))

def error_bad_argument(arg_name):
    return error(400, 'BAD_ARGUMENT', 'Bad argument format: {}'.format(arg_name))
