from decimal import getcontext, Decimal
getcontext().prec = 130

### Constants ###
# Math #
ADD = lambda a, b: a+b
SUB = lambda a, b: a-b
MUL = lambda a, b: a*b
DIV = lambda a, b: a/b
IDV = lambda a, b: a//b
MOD = lambda a, b: a%b
PI = Decimal('3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460')

# Tools #
MISSING_START = object()

class Math:
    # Container of all mathematic functions

    @staticmethod
    def floor(val):
        #Take a floating point value and return the rounded down version.
        
        #Return the truncated integer version of the value using int built-in function if its positive.
        #Return the negative integer version of its rounded up absolute value if the value is negative.

        if type(val) != float:
            raise TypeError("n must be a float")
        
        if val > 0:
            return int(val)
        return -ceil(abs(val))

    @staticmethod
    def ceil(val):
        #Take a floating point value and return the rounded up version.
        
        #Any decimal amount added to a value when negative will add one to the integer division result,
        #therefore returning this value multiplied by -1 will round up the value.

        if type(val) != float:
            raise TypeError("n must be a float")

        return int((-val // 1) * -1)
    
    @staticmethod
    def fact(n):
        # Reduce an array of integers from 1 to n+1 using MUL

        if type(n) != int or n < 0:
            raise TypeError("n must be a positive integer")

        return Tools.reduce(MUL, [i for i in range(1, n+1)])

    @staticmethod
    def root(n, r=2):
        #Take an integer or floating point value and return its rth root.
        
        #Any number to the power of 1/r will give its rth root.

        if type(n) not in [int, float] or n < 0:
            raise TypeError("n must be a positve integer or float")
        
        power = 1/r
        val = Decimal(n ** power)
        if int(val) == float(str(val)[:8]):
            return Decimal(val)
        return val

    @staticmethod
    def fib(n):
        #Calculate nth value of the fibonacci sequence using a version of Binet's Forumula.

        #posPHI = 1 + root(5)
        #negPHI = 1 - root(5)
        #val = posPHIⁿ - negPHIⁿ / 2ⁿ * √5
        #floor(val)

        if type(n) != int or n < 0:
            raise TypeError("n must be a positive integer")

        posPHI = 1 + root(5)
        negPHI = 1 - root(5)
        numerator = posPHI**n - negPHI**n
        denominator = (2**n) * root(5)
        val = numerator / denominator
        return floor(val)
    
    @staticmethod
    def product(arr):
        # Take an array and reduce it using MUL

        if not hasattr(arr, "__iter__"):
            raise TypeError(f"{arr} is not iterable and must be")

        return Tools.reduce(MUL, arr)

    @staticmethod
    def deepproduct(arr):
        # Take an array and flatten it, then call product on it

        flattened_arr = Tools.flatten(arr)
        return Math.product(flattened_arr)
    
    @staticmethod
    def sum(arr):
        # Take an array and reduce it using ADD

        if not hasattr(arr, "__iter__"):
            raise TypeError(f"{arr} is not iterable and must be")

        return Tools.reduce(ADD, arr)

    @staticmethod
    def deepsum(arr):
        # Take an array and flatten it, then call sum on it

        flattened_arr = Tools.flatten(arr)
        return Math.sum(flattened_arr)

class Tools:
    # Container for all 'tool' functions

    @staticmethod
    def reduce(func, seq, start = MISSING_START):
        #Take a sequence and cumulativly apply a function of two arguments to the items of it, reducing it to a single value.

        it = iter(seq)
        if start is not MISSING_START:
            val = it
        else:
            try:
                val = next(it)
            except StopIteration:
                raise TypeError("cannot perform reduction of empty interable with no start value")
        
        if not callable(func):
            raise TypeError(f"{func} is not callable and must be")

        for v in it:
            val = func(val, v)
        return val

    @staticmethod
    def flatten(arr):
        #Take an array/list of multiple dimensions and flatten it to 1 dimension

        try:
            if type(arr) is list:
                val = Tools.flatten(arr[0])
                if len(arr) > 1:
                    val += Tools.flatten(arr[1:])
            else:
                val = [arr]
            return val
        except IndexError:
            return []

# Create decorator to bind a function to a class after the classes intialisation
def addmethod(cls, reuse = False):
    def decor(func):
        def wrap(*args, **kwargs): 
            return func(*args, **kwargs)
        setattr(cls, func.__name__, wrap)
        if reuse:
            return func # Returning here allows the function to be used seperate of the class
    return decor