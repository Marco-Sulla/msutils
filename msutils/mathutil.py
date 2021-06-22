import math
import random
from cmath import isnan

try:
    from collections.abc import Iterable
except ImportError:
    from collections import Iterable


inf = float("+Inf")
minus_inf = float("-Inf")

def minDeep(arg, exclude=None, no_nan=False):
    """
    Calculate min recursively for nested iterables, at any depth (arrays,
    matrices, tensors...) and for any type of iterable (list of tuples,
    tuple of sets, list of tuples of dictionaries...)
    """

    if exclude is None:
        exclude = ()

    if not isinstance(exclude, Iterable):
        exclude = (exclude, )

    if isinstance(arg, tuple(exclude)):
        return inf

    try:
        if next(iter(arg)) is arg:  # avoid infinite loops
            return min(arg)
    except TypeError:
        return arg

    try:
        mins = map(lambda x: minDeep(x, exclude), arg.keys())
    except AttributeError:
        try:
            mins = map(lambda x: minDeep(x, exclude), arg)
        except TypeError:
            return inf

    try:
        if no_nan:
            res = min((x for x in mins if not isnan(x)))
        else:
            res = min(mins)
    except ValueError:
        res = inf

    return res


def maxDeep(arg, exclude=None):
    """
    Calculate max recursively for nested iterables, at any depth (arrays,
    matrices, tensors...) and for any type of iterable (list of tuples,
    tuple of sets, list of tuples of dictionaries...)
    """

    if exclude is None:
        exclude = ()

    if not isinstance(exclude, Iterable):
        exclude = (exclude, )

    if isinstance(arg, tuple(exclude)):
        return minus_inf

    try:
        if next(iter(arg)) is arg:  # avoid infinite loops
            return max(arg)
    except TypeError:
        return arg

    try:
        maxes = map(lambda x: maxDeep(x, exclude), arg.keys())
    except AttributeError:
        try:
            maxes = map(lambda x: maxDeep(x, exclude), arg)
        except TypeError:
            return minus_inf

    try:
        res = max(maxes)
    except ValueError:
        res = minus_inf

    return res


def magnitudeOrder(num):
    if num == 0:
        return 0
    
    absnum = abs(num)
    order = math.log10(absnum)
    res = math.floor(order)
    
    return res


def tossCoin():
    return random.choice((0, 1))


def isInt(num):
    return num % 1 == 0


def isEven(num):
    return num % 2 == 0

def median(iterable, member=False, sort=True, sort_fn=None):
    has_sort_fn = sort_fn is not None
    
    if sort:
        if has_sort_fn:
            sort_fn_true = sort_fn
        else:
            sort_fn_true = sorted
        
        sorted_it = sort_fn_true(iterable)
    else:
        if has_sort_fn:
            raise ValueError("You can't specify `sort_fn` and `sort` False")
        
        # do it only if data is already sorted!
        sorted_it = iterable
    
    try:
        len_it = len(sorted_it)
    except TypeError:
        # iterator or other iterable that not supports len()
        sorted_it = tuple(sorted_it)
        len_it = len(sorted_it)
    
    if not len_it:
        raise ValueError("The iterator must not be empty")
    
    index = len_it // 2
    b = sorted_it[index]
    
    if isEven(len_it):
        a = sorted_it[index-1]
        
        if isnan(a):
            res = b
        elif isnan(b):
            res =  a
        elif member:
            # same logic of Round Even Up
            if isEven(len_it / 2):
                # maybe the iterable is *reverse* sorted...
                res = min(a, b)
            else:
                res = max(a, b)
        else:
            res = (a + b) / 2.0
    else:
        res = b

    return res

def divideAndRedistribute(a, b, alternate=False):
    _a = int(a)
    _b = int(b)

    if not (_a == a and _b == b):
        raise ArithmeticError("Expected integer parameters")

    num, rest = divmod(_a, _b)
    res = [num] * _b
    
    if alternate:
        if rest:
            r = range(0, _b, 2)
            
            for i in r:
                res[i] += 1
                rest -= 1
                
                if rest == 0:
                    break
        
        if rest:
            r = range(1, _b, 2)
            
            for i in r:
                res[i] += 1
                rest -= 1
                
                if rest == 0:
                    break
    else:
        for i in range(rest):
            res[i] += 1

    return res

__all__ = (
    minDeep.__name__,
    maxDeep.__name__,
    magnitudeOrder.__name__,
    isInt.__name__,
    divideAndRedistribute.__name__,
    tossCoin.__name__,
    isEven.__name__,
    median.__name__,
    "inf",
    "minus_inf",
)
