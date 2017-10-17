#!/bin/python3

from math import ceil
import bisect

n = int(input().strip())

def read(): return int(input().strip())

a = []
i = 0
for a_i in range(n):
    bisect.insort_right(a, read())
    i += 1

    if len(a)%2:
        print("%.1f"%(a[int(i/2)]))
    else:
        print("%.1f"%((a[int(i/2)]+a[int(i/2)-1])/2.0))