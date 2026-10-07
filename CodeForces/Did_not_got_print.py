import sys
input = sys.stdin.readline


def solve():
    n1 = int(input())
    n2 = str(input())
    
    memory = []
    unprint = []
    
    for i in range (1 , n1+1):
        if n2[i-1] == "1":
            memory.append(i)
            
        elif n2[i-1] == "2":
            if memory:
                memory.pop()
                unprint.append(i)
             
        else :
            continue

    unprint.extend(memory)
    unprint.sort()
    
    print(len(unprint))
    if len(unprint) != 0:
        print(*unprint)
    else :
        print()
        

n = int(input())
for _ in range (n):
    solve()