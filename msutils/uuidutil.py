from uuid import uuid4

def getUuid():
    return str(uuid4())

__all__ = (getUuid.__name__, )
