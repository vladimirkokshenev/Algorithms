
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
    Take big intger in form of a list, and splits it into to integers of size len(arg)/2
    
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