#frequency counting
nums = [1,2,3,2,1,3,4,5,1]
freq = [0]*6

for num in nums:
    freq[num] += 1
print(freq)
    
for i in range (len(freq)):
    if freq[i]> 1:
        print(i)
        
        
#character frequency.
s = "saikumar"
freq = [0] *26

for str in s:
    index = ord(str) - ord('a')
    freq[index] +=1
    
print(freq)


#Exercise 

s = "racecar"
t = "carrace"

if len(s) != len(t):
    print("incorrect length for the inputs")
    
countS, countT = {},{}
    
for i in range (len(s)):
    countS[s[i]] = 1+ countS.get(s[i], 0)
    countT[t[i]] = 1+ countT.get(t[i], 0)
    
if countS == countT :
    print("True")
        
else:
    print("False")
        