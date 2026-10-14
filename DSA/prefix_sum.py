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


arr = [2,6,7,3,1,9]
n = len(arr)
prefix = [0] * (n+1)

for i in range (n):
    prefix[i+1] = prefix[i] + arr[i]                       # it creates arr[0] = 0 to .... it add one zero. becuase of [i+1]                    

def range_append(L,R):
    return prefix[R+1] - prefix[L]                          # it avoid if condition and reduce syntax

print(range_append(1,3)) 
print(range_append(0,3))



#Difference Array 
n = 5

diff = [0] * (n+1)

diff[1] += 3
diff[4] -= 3

arr = [0] * n
running_sum = 0

for i in range(n):
    running_sum += diff[i]
    arr[i] = running_sum

#print(arr)



#Suppose the original array contains five zeros, and we have these operations:
#Add 3 to indices 1 through 3.
#Add 2 to indices 2 through 4.
#Add -1 to indices 0 through 2.

n = 5
updates = {
    (1,3,3),
    (2,4,2),
    (0,2,-1)
}

diff = [0] * (n+1)

for L,R,X in updates:
    diff[L] += X
    diff[R+1] -= X
    
arr = [0]* n
total_sum = 0
 
for i in range (n):
    total_sum += diff[i]
    arr[i] = total_sum
    
print(arr)   

