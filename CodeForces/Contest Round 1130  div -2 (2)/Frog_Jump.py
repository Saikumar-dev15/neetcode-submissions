import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    row1 = input().strip()
    row2 = input().strip()

    a = row1.count("f")
    b = row2.count("f")
    d = abs(a - b)

    if d == 0:
        return 0

    heavy = row1 if a > b else row2

    pairs = 0
    run = 0
    for ch in heavy:
        if ch == "f":
            run += 1
        else:
            pairs += run // 2
            run = 0
    pairs += run // 2

    return d - 2 * min(pairs, d // 2)


n = int(input())
for _ in range(n):
    print(solve())