sentence = "hello world and practice makes perfect and hello world again"


def my_met(my_str: str):
    my_list = my_str.split(" ")
    result = list(dict.fromkeys(my_list))
    result.sort()
    return " ".join(result)


if __name__ == "__main__":
    print(my_met(sentence))
