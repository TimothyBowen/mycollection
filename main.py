START_VALUE = object()
def reduce(func, seq, start = START_VALUE):
    it = iter(seq)
    if start is not START_VALUE:
        val = it
    else:
        try:
            val = next(it)
        except StopIteration:
            raise TypeError("cannot perform reduction of empty interable with no start value")
    
    for v in it:
        val = func(val, v)
    return val

def floor(val):
    if type(val) != float:
        raise TypeError("n must be a float")

    return int(val)

def ceil(val):
    if type(val) != float:
        raise TypeError("n must be a float")

    return -(-val // 1)

def fact(n):
    if type(n) != int or n < 0:
        raise TypeError("n must be a positive integer")

    if n in [0, 1]:
        return 1
    return n * fact(n-1)

FIB_CACHE = dict()
def fib(n):
    if type(n) != int or n < 0:
        raise TypeError("n must be a positive integer")

    return floor((((1 + (5 ** 0.5)) ** n)-((1 - (5 ** 0.5)) ** n))/((2 ** n) * (5 ** 0.5)))