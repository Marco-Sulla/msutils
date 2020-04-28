"""
@author  Marco Sulla (marcosullaroma@gmail.com)
@date    2015-11-09
"""

import os
from asyncio import coroutine


number_re = r"([-+]?\d+(\.\d+)?([eE][-+]?\d+)?)|\bNaN\b|\bnan\b|\bNan\b"


class NaNError(ValueError):
    pass


class NoMatch(RuntimeError):
    pass


def mergeDicts(*dicts):
    len_dicts = len(dicts)

    if not len_dicts > 1:
        err_tpl = "You must provide at least 2 arguments ({num} given)"
        raise TypeError(err_tpl.format(num=len_dicts))

    it = iter(dicts)
    z = next(it).copy()
    
    for d in it:
        z.update(d)
    
    return z


def tarRelative(tar_f, path):
    tar_f.add(path, arcname=os.path.basename(path))



def dbString(dtype, user, password, host, port, db_name):
    if dtype == "oracle":
        type_verb = "oracle"
    elif dtype == "mysql":
        type_verb = "mysql+mysqlconnector"
    elif dtype == "postgres":
        type_verb = "postgresql"
    else:
        raise RuntimeError("Unsupported db type: {t}".format(t=dtype))

    if dtype == "oracle":
        db_tpl = ("{t}://{u}:{pw}@(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)" +
                  "(Host = {h})(Port={po}))" +
                  "(CONNECT_DATA=(SERVICE_NAME = {d})))")
    else:
        db_tpl = "{t}://{u}:{pw}@{h}:{po}/{d}"

    return db_tpl.format(
        t = type_verb,
        u = user,
        pw = password,
        h = host,
        po = port,
        d = db_name
    )


def reprForClass(self, attributes_to_print):
    attributes = []
    
    for k in attributes_to_print:
        attributes.append("{k}={v}".format(k=k, v=getattr(self, k)))
    
    return "{klass}({attributes})".format(
        klass = self.__class__.__name__, 
        attributes = ", ".join(attributes), 
    )


@coroutine
def recvAll(reader, msg_len, packet_len=4096):
    """
    Implements a recv_all su un asyncio.StreamReader
    """

    data_all = bytearray()

    while len(data_all) < msg_len:
        chunk = yield from reader.read(
            min(msg_len - len(data_all), packet_len)
        )

        if not chunk:
            data_all = bytearray()
            break

        data_all.extend(chunk)

    return data_all


_sentinel = object()

def boolean(arg=_sentinel):
    if arg is _sentinel:
        return False
    
    try:
        return bool(arg)
    except ValueError:
        # maybe a numpy array?
        return bool(arg.size)

__all__ = (
    "number_re",
    NaNError.__name__,
    NoMatch.__name__,
    mergeDicts.__name__,
    tarRelative.__name__,
    dbString.__name__,
    reprForClass.__name__,
    recvAll.__name__,
    boolean.__name__,
)
