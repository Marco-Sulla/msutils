def rangeStep(it):
    """
    returns a sequence from 0 to 1, by step the inverse of it length
    """

    length = len(it)

    return (i/length for i in range(length))

__all__ = (rangeStep.__name__, )
