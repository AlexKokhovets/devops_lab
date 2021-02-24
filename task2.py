s1 = set(map(int, input().split(' ')))
s2 = set(map(int, input().split(' ')))
print(' '.join(map(str, sorted(s1.intersection(s2)))))
