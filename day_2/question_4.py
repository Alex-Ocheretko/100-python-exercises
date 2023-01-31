def met(my_str: str):
    a = my_str.split(", ")
    b = tuple(a)
    print(a)
    print(b)


if __name__ == "__main__":
    met(input())
