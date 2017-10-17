from collections import Counter


def ransom_note(magazine, ransom):
    return ransom.issubset(magazine)

m, n = map(int, input().strip().split(' '))
magazine = Counter(input().strip().split(' '))
ransom = Counter(input().strip().split(' '))
A, B = set(), set()

for k, v in magazine.items():
    for i in range(v):
        A.add(k+str(i))

for k, v in ransom.items():
    for i in range(v):
        B.add(k + str(i))

if (ransom_note(A, B)):
    print("Yes")
else:
    print("No")
