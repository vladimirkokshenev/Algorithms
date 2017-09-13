
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


def split_big_integer(arg):
    """
    Take big integer in form of a list, and splits it into to integers of size len(arg)/2
    
    :param arg: list of integers
    :return: a,b pair containing two lists of integers. a.append(b) is arg. 
    """

    a = []
    b = []

    for i in range(len(arg)/2):
        a.append(arg[i])

    for i in range(len(arg)/2, len(arg)):
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

    # x = a*10^n1 + b
    a, b = split_big_integer(x)
    n1 = len(b)
    # y = c*10^n2 + d
    c, d = split_big_integer(y)
    n2 = len(d)

    ac = mul_big_integers(a, c)
    ad = mul_big_integers(a, d)
    bc = mul_big_integers(b, c)
    bd = mul_big_integers(b, d)

    res1 = shift_big_integer(ac, n1+n2)
    res2 = shift_big_integer(ad, n1)
    res3 = shift_big_integer(bc, n2)

    res4 = sum_big_integers(res1, res2)
    res5 = sum_big_integers(res4, res3)

    res = sum_big_integers(res5, bd)

    return res


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
