data = input().split(',')
data = [num for num in data if int(num, 2) % 5 == 0]
print(','.join(data))
