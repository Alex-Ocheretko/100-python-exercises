class SomeClass:

    def __init__(self):
        self.my_string = str

    def get_string(self):
        self.my_string = input()

    def print_str(self):
        print(self.my_string.upper())


if __name__ == "__main__":
    some_class = SomeClass()
    some_class.get_string()
    some_class.print_str()
