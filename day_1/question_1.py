"""
    Write a program which will find all such numbers which are
    divisible by 7 but are not a multiple of 5, between 2000
    and 3200 (both included).The numbers obtained should be
    printed in a comma-separated sequence on a single line.
"""


def res1():
    l = []
    for a in range(2000, 3200):
        if a % 7 == 0 and a % 5 != 0:
            l.append(str(a))
    print(','.join(l))


def res2():
    print(*(a for a in range(2000, 3200) if a % 7 == 0 and a % 5 != 0), sep=",")


if __name__ == '__main__':
    res1()
