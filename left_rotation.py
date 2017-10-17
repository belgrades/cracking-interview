# url: https://www.hackerrank.com/challenges/ctci-array-left-rotation

def array_left_rotation(a, n, k):
    return a[ k %n: ] +a[0: k %n]


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
