import sys 
input = sys.stdin.readline

def solve():
    xo,yo ,r = map(int, input().split())
    x = xo
    y = yo + r

    return f"{x} {y}"
        
n = int(input())
for _ in range (n):
    print(solve())