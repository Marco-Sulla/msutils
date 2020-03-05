import json
from copy import deepcopy
from collections.abc import Mapping
from .clonable import Clonable
from .jsonutil import jsonLoad, jsonDump as jsonUtilDump
from .klass import Klass

class JsonMap(Mapping, Clonable, Klass):
    _deep_attrs = ("_data_raw", )
        
    def __init__(self, source):
        try:
            # it's a JsonMap!
            self._data_raw = deepcopy(source._data_raw)
        except AttributeError:
            self._data_raw = jsonLoad(source)

    def jsonDump(self, fp=None, *args, **kwargs):
        return jsonUtilDump(self._data_raw, fp=fp, *args, **kwargs)


    def copy(self, deep=True):
        return super().copy(deep=deep)
    
    def __getitem__(self, k):
        return self._data_raw[k]

    def __iter__(self):
        return iter(self._data_raw)

    def __len__(self):
        return len(self._data_raw)

    def __repr__(self, *args, **kwargs):
        return "{klass}({body})".format(
            klass = self._klass_name,
            body = repr(self._data_raw)
        )
    
    def __str__(self, *args, **kwargs):
        return "{klass}({body})".format(
            klass = self._klass_name,
            body = self.jsonDump()
        )
        

__all__ = (JsonMap.__name__, )
