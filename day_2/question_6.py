from math import sqrt

C, H = 50, 30


def calc(D):
    return sqrt((2 * C * D) / H)


D = input().split(',')
D = [str(round(calc(int(i)))) for i in D]
print(",".join(D))
