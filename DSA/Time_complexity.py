n = 10
for i in range (n):
    for j in range (n):
        print(i, j)    #Time Complexity = o(n^2)
        
        

m = 3
for i in range (n):
    for j in range (n):
        for k in range (i):
            print(i,j,k)   # o(n^3)
            
            
