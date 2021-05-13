import sys

def get_ints():
    return map(int, sys.stdin.readline().strip().split())


T = int(input())  # no of test case
while (T):
    a,b,x,y = get_ints()


    T -= 1
    print((a*x)+(b*y))

