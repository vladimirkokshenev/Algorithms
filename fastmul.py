
def convert_string_to_big_integer(s):
    """
    The method take string as an input, and returns input as a list of integers
    
    :param s: string containing digits only
    :return: list of single digit integers
    """

    arg = []
    for i in range(len(s)):
        arg.append(int(s[i]))
    return arg


def split_big_integer(arg, n):
    """
    Take big integer in form of a list, and splits it into to integers of size len(arg)/2
    
    :param arg: list of integers
    :param n: number of high order digits to split (n<len(arg))
    :return: a,b pair containing two lists of integers. a.append(b) = arg; len(a)=n; len(b)=len(arg)-n
    """

    a = []
    b = []
    l = len(arg)
    # left part of big number split
    for i in range(0, l-n):
        a.append(arg[i])
    # make the left part of size n (if it is smaller)
    if l-n < n:
        for i in range(2*n-l):
            a.insert(0, 0)
    # right part of big number split
    for i in range(l-n, l):
        b.append(arg[i])

    return a, b


def sum_big_integers(a, b):
    """
    Sum two big integers represented as lists. For example, 123 should be represented as [1,2,3].
    
    :param a: 1st argument represented as a list 
    :param b: 2nd argument represented as a list 
    :return: sum of a and b represented as a list
    """

    # bring both arguments to same number of digits
    if len(a) < len(b):
        for i in range(len(b)-len(a)):
            a.insert(0, 0)
    else:
        if len(b) < len(a):
            for i in range(len(a) - len(b)):
                b.insert(0, 0)

    sum = []

    # calculate sum (possible overflow will be handled later)
    for i in range(len(a)-1, -1, -1):
        sum.insert(0, a[i]+b[i])

    # handle overflow in digits
    for i in range(len(sum)-1, -1, -1):
        if i == 0:
            if sum[i] > 9:
                sum[i] -= 10
                sum.insert(0, 1)
        else:
            if sum[i] > 9:
                sum[i] -= 10
                sum[i-1] += 1

    return sum


def shift_big_integer(a, n):
    """ Shift big integer a for n digit left
    
    :param a: big integer as a list
    :param n: integer
    :return: 
    """

    for i in range(n):
        a.append(0)

    return a


def drop_leading_zero(arg):
    """ Remove leading zeros from big integer arg
    
    :param arg: big integer in form of a list
    :return: big integers with zeros removed
    """

    while len(arg) > 1 and arg[0] == 0:
        arg.remove(0)
    return arg


def sub_big_integers(x, y):
    """ Substract y from x. Note that x MUST BE greater than or equal y 
    
    :param x: arg x
    :param y: arg y
    :return: big integer corresponding to (x-y)
    """

    if len(y) < len(x):
        for i in range(len(x)-len(y)):
            y.insert(0, 0)

    for i in range(len(x)-1, -1, -1):
        x[i] = x[i] - y[i]
        if x[i] < 0:
            x[i-1] -= 1
            x[i] += 10

    x = drop_leading_zero(x)
    return x


def mul_big_integers(x, y):
    """ Multiplies two big integers and returns their product
    
    :param x: 1st argument 
    :param y: 2nd argument
    :return: product
    """

    mul = []

    if len(x) == 1:
        # multiply every digit of y by x, going from lower to upper digits
        for i in range(len(y)-1, -1, -1):
            mul.insert(0,x[0]*y[i])
        # resolve overflow
        for i in range(len(mul) - 1, 0, -1):
            mul[i-1] += mul[i] / 10
            mul[i] = mul[i] % 10
        if mul[0] > 9:
            cr = mul[0] / 10
            mul[0] = mul[0] % 10
            mul.insert(0, cr)
        return mul

    if len(y) == 1:
        return mul_big_integers(y, x)

    # x = a*10^n + b
    n = max(len(x), len(y))/2
    a, b = split_big_integer(x, n)
    # y = c*10^n + d
    c, d = split_big_integer(y, n)

    # get (1)
    ac = mul_big_integers(a, c)
    # get (2)
    bd = mul_big_integers(b, d)
    # get (3)
    abcd = mul_big_integers(sum_big_integers(a, b), sum_big_integers(c, d))

    res1 = shift_big_integer(list(ac), 2*n)
    res2 = shift_big_integer(sub_big_integers(sub_big_integers(abcd, ac), list(bd)), n)

    res = sum_big_integers(sum_big_integers(res1, res2), bd)
    res_final = drop_leading_zero(res)
    return res_final


if __name__ == "__main__":

    successful_input = False
    while not successful_input:
        print("Enter 1st integer: ")
        s = raw_input()
        if s.isdigit():
            arg1 = convert_string_to_big_integer(s)
            successful_input = True
        else:
            print("Invalid input!")

    successful_input = False
    while not successful_input:
        print("Enter 2nd integer: ")
        s = raw_input()
        if s.isdigit():
            arg2 = convert_string_to_big_integer(s)
            successful_input = True
        else:
            print("Invalid input!")

    print(arg1)
    print(arg2)

    res = mul_big_integers(arg1, arg2)

    s = ""

    for i in range(len(res)):
        s += str(res[i])

    print("Result:")
    print(s)
