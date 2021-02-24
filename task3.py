def read_number(line: str, start: int, end: int) -> int:
    try:
        num = int(line[start:end])
        return num
    except ValueError:
        print("ERROR")
        exit(0)


record = str(input())
record_list = []

# Parse the last number
equal_idx = record.find('=')
if equal_idx < 0:
    print("ERROR")
    exit(0)

last = (read_number(record, equal_idx+1, len(record)))

# Parse first two numbers
for idx, i in enumerate(record[1:equal_idx]):
    if i == '+' or i == '-' or i == '*' or i == '/':
        first = read_number(record, 0, idx+1)
        second = read_number(record, idx+2, equal_idx)

        result = 0
        if i == '+':
            result = first + second
        elif i == '-':
            result = first - second
        elif i == '*':
            result = first * second
        elif i == '/':
            result = first // second
        if result == last:
            print("YES")
        else:
            print("NO")

        break
else:
    print("ERROR")
