start, end = map(int, input().split())

numbers = []
for i in range(start, end+1):
    for j in str(i):
        if j == '0':
            break
        if i % int(j) != 0:
            break
    else:
        numbers.append(i)
print(numbers)