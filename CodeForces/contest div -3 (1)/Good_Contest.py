import sys
input = sys.stdin.readline

def participant():
    no_of_participated = int(input())
    no_of_solved = list(map(int, input().split()))
    
    if no_of_participated == min(no_of_solved):
        return 0
    else:
        return no_of_participated - min(no_of_solved)
    
        
n = int(input())
for _ in range(n):
    print(participant())      
        