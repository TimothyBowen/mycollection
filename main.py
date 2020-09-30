class Math:
    @staticmethod
    def floor(val):
        """
        Take a floating point value and return the rounded down version.
        
        Return the truncated integer version of the value using int built-in function if its positive.
        Return the negative integer version of its rounded up absolute value if the value is negative.
        """
        if type(val) != float:
            raise TypeError("n must be a float")
        
        if val > 0:
            return int(val)
        return -ceil(abs(val))

    @staticmethod
    def ceil(val):
        """
        Take a floating point value and return the rounded up version.

        Any decimal amount added to a value when negative will add one to the integer division result,
        therefore returning this value multiplied by -1 will round up the value.
        """
        if type(val) != float:
            raise TypeError("n must be a float")

        return int((-val // 1) * -1)

    @staticmethod
    def fact(n):
        if type(n) != int or n < 0:
            raise TypeError("n must be a positive integer")

        if n in [0, 1]:
            return 1
        return n * fact(n-1)

    @staticmethod
    def root(n, r=2):
        """
        Take an integer or floating point value and return its rth root.

        Any number to the power of 1/r will give its rth root.
        """
        if type(n) not in [int, float] or n < 0:
            raise TypeError("n must be a positve integer or float")
        
        power = 1/r
        val = n ** power
        if int(val) == float(str(val)[:8]):
            return int(val)
        return val

    @staticmethod
    def fib(n):
        """
        Calculate nth value of the fibonacci sequence using a version of Binet's Forumula.

        posPHI = 1 + root(5)
        negPHI = 1 - root(5)
        val = posPHIⁿ - negPHIⁿ / 2ⁿ * √5
        floor(val)
        """
        if type(n) != int or n < 0:
            raise TypeError("n must be a positive integer")

        posPHI = 1 + root(5)
        negPHI = 1 - root(5)
        numerator = posPHI**n - negPHI**n
        denominator = (2**n) * root(5)
        val = numerator / denominator
        return floor(val)


class Tools:
    @staticmethod
    MISSING_START = object()
    def reduce(func, seq, start = MISSING_START):
        """
        Take a sequence and cumulativly apply a function of two arguments to the items of it, reducing it to a single value.
        """
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

    def flatten(arr):
        """
        Take an array/list of multiple dimensions and flatten it to 1 dimension
        """
        try:
            if type(arr) is list:
                val = flatten(arr[0])
                if len(arr) > 1:
                    val += flatten(arr[1:])
            else:
                val = [arr]
            return val
        except IndexError:
            return []