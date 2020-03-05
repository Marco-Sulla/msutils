class Klass():
    def __new__(klass, *args, **kwargs):
        self = super().__new__(klass)
        self._klass = klass
        self._klass_name = klass.__name__
        
        return self

__all__ = (Klass.__name__, )
