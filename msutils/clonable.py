from copy import copy, deepcopy
from abc import ABC

class Clonable(ABC):
    _simple_attrs = ()
    _flat_attrs = ()
    _deep_attrs = ()
    
    def _copyAttrs(self, other, attrs, copy_func=None):
        for attr in attrs:
            val = getattr(self, attr)

            if copy_func is None:
                setattr(other, attr, val)
            else:
                setattr(other, attr, copy_func(val))
    
    def copy(self, deep=False):
        klass = type(self)
        other = klass.__new__(klass)
        copyAttrs = self._copyAttrs
        
        copyAttrs(other, self._simple_attrs)
        copyAttrs(other, self._flat_attrs, copy)
        
        if deep:
            copyAttrs(other, self._deep_attrs, deepcopy)
        else:
            copyAttrs(other, self._deep_attrs, copy)
        
        return other
    
    def __copy__(self, *args, **kwargs):
        return self.copy()
    
    def __deepcopy__(self, *args, **kwargs):
        return self.copy(deep=True)

__all__ = (Clonable.__name__, )
