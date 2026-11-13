arr = [10, 20, 30, 40, 0]

left = 0
right = len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]
    
    left += 1
    right -= 1
    
#print(arr)



#count elements in a array
arr = [12, 12, 13, 12, 19, 32]
arr.reverse()

count = 0 

for i in range (len(arr)):
    if arr[i] == 12:
        count += 1
        
#print(count)
#print(arr)


#count Even and odd Numbers in one phase
arr = [12, 15, 17, 19, 31, 71]
even = 0
odd = 0

for i in range (len(arr)):
    if arr[i]% 2 == 0:
       even +=1
    else :
        odd +=1
#print(f"Even Numbers in the array: {even}")
#print(f"Odd Numbers in the array: {odd}") 



array = [1,2,3,4,5,6,7,8]
even_ = 0 
odd_ = 0
left = 0
right = len(array) - 1

while left < right:
    
    if array[left]%2 == 0:
        even_ += 1
            
    else :
        odd_ += 1
        
    if array[right]%2 == 0:
        even_ += 1
        
    else:
        odd_ +=1
            
    array[left] , array[right] = array[right], array[left]
    
    left += 1
    right -=1 
    
if left == right :
    if array[left]%2 == 0:
        even_ +=1
        
    else :
        odd_ +=1
    
print("Even: ", even_)
print("Odd: ", odd_)
print("Two Pointers: ", array)
    
    