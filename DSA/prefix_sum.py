arr = [ 2,6,7,3,1,9]

prefix = []

for i in range (len(arr)):
    total = 0
    
    for j in range (i+1):
        total += arr[j]
    prefix.append(total)
    
print(prefix)                     # this is o(n^2)



# 2nd method

arr = [2,6,7,3,1,9]
prefix = [0] * len(arr)

prefix[0] = arr[0]

for i in range (1, len(arr)):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)                    # this is o(n)
    
def range_sum(L,R):              # this method is called range sum quries o(1)
    if L ==0 :
        return prefix[R]
    
    else:
        return prefix[R] - prefix[L-1]                     # Here i used condition if L = 0 and L > 0. it will be useful to find range blw index 
        
print(range_sum(1,3)) 
print(range_sum(0,3))
print(range_sum(2,5))  



arr = [2,6,7,3,1,9]
n = len(arr)
prefix = [0] * (n+1)

for i in range (n):
    prefix[i+1] = prefix[i] + arr[i]                       # it creates arr[0] = 0 to .... it add one zero. becuase of [i+1]                    

def range_append(L,R):
    return prefix[R+1] - prefix[L]                          # it avoid if condition and reduce syntax

print(range_append(1,3)) 
print(range_append(0,3))
print(range_append(2,4))



