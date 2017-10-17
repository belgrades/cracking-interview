# url: https://www.hackerrank.com/challenges/ctci-making-anagrams

from collections import Counter

a, b = Counter(input()), Counter(input())
A, B = set(), set()

for k, v in a.items():
    for i in range(v):
        A.add(k+str(i))

for k, v in b.items():
    for i in range(v):
        B.add(k+str(i))

inter = A.intersection(B)

print(len(A.difference(inter))+len(B.difference(inter)))



