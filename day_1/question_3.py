"""
    With a given integral number n, write a program to generate a dictionary
    that contains (i, i x i) such that is an integral number between 1 and n (both included).
    and then the program should print the dictionary.
    Suppose the following input is supplied to the program: 8
"""


def func(num):
    my_dict = {i : i*i for i in range(1, num+1)}
    print(my_dict)


if __name__ == "__main__":
    func(4)
