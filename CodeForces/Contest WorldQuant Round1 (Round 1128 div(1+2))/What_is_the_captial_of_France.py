import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    array = list(map(int, input().split()))

    odd = []
    even = []
    for num in array:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    if len(odd) % 2 == 0:
        return "Moggity"

    if (len(odd) == 1 and len(even) == 1) or (len(odd) == 3 and len(even) == 0):
        return "Larpity"

    return "Moggity"


x = int(input())
for _ in range(x):
    print(solve())