word = input()
letter, digit = 0, 0

for i in word:
    if i.isalpha():
        letter += 1
    elif i.isnumeric():
        digit += 1
print(f"LETTERS {letter}\nDIGITS {digit}")
