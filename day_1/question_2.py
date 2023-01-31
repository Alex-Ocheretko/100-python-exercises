"""
    Write a program which can compute the factorial of a given numbers.
    The results should be printed in a comma-separated sequence on a single line.
    Suppose the following input is supplied to the program: 8 Then, the output should be:40320
"""

from functools import reduce


def res1(num: int):
    a = 1
    for i in range(1, num+1):
        a *= i
    print(a)


def fun(acc, item):
    return acc * item


if __name__ == '__main__':
    num = 5
    res1(num)
    print(reduce(fun, range(1, num+1)))
