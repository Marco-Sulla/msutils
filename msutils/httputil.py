from http import HTTPStatus

def isGoodHttpStatusCode(code):
    return code < HTTPStatus.BAD_REQUEST

__all__ = (isGoodHttpStatusCode.__name__, )
