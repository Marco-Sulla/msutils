import json
from json import JSONEncoder
from copy import deepcopy
from json.decoder import JSONDecodeError

MINIMAL_SEPARATORS = (",", ":")

class MsJsonEncoder(JSONEncoder):
    def default(self, obj):
        try:
            return super().default(obj)
        except TypeError:
            try:
                # numpy array-like
                return obj.tolist()
            except AttributeError:
                # msutils JsonDict-like
                return obj._data_raw

def jsonLoad(source):
    path = None

    try:
        # most common case: JSON string
        res = json.loads(source)
    except TypeError:
        try:
            # check if it's a dict-like object
            source.items
            res = deepcopy(source)
        except AttributeError:
            try:
                # maybe a file object?
                res = json.load(source)
            except AttributeError:
                # maybe a PathLike?
                path = source
    except JSONDecodeError:
        # maybe a path string?
        path = source

    if path:
        with open(path) as f:
            res = json.load(f)
    
    return res


def jsonDump(source, fp=None, *args, **kwargs):
    kwargs.setdefault("indent", 4)
    kwargs.setdefault("cls", MsJsonEncoder)
    
    if fp is None:
        return json.dumps(source, *args, **kwargs)
    else:
        try:
            fp.write
            return json.dump(source, fp, *args, **kwargs)
        except AttributeError:
            with open(fp, "w") as f:
                res = f.write(json.dumps(source, *args, **kwargs))

            return res

def jsonDumpMinimal(source, fp=None, *args, **kwargs):
    err = "{fname}() does not support the parameter '{parameter}'"
    
    for parameter in ("indent", "separators"):
        if parameter in kwargs:
            fname = jsonDumpMinimal.__name__
            raise ValueError(err.format(fname=fname, parameter=parameter))
    
    kwargs["indent"] = None
    kwargs["separators"] = MINIMAL_SEPARATORS
    
    return jsonDump(source, fp=fp, *args, **kwargs)

__all__ = (
    jsonLoad.__name__, 
    jsonDump.__name__, 
    jsonDumpMinimal.__name__, 
    "MINIMAL_SEPARATORS", 
    MsJsonEncoder.__name__
)
