#n = 10
#for i in range (n):
#    for j in range (n):
#        print(i, j)    #Time Complexity = o(n^2)
        
        

m = 3
for i in range (m):
    for j in range (m):
        for k in range (m):
            print(i,j,k)   # o(n^3)
            
            
s = 10
for i in range(s):
    j =1
    while j<s:
        j *= 2
        



def contains_duplicate(arr):
    seen = [1,2]

    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False


print(contains_duplicate([1, 2, 3, 4, 5]))         # o(n) time + o(n) space


