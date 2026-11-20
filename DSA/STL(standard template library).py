stack = []

stack.append(10)
stack.append(20)
stack.append(30)

stack.pop(1)
stack[1] = 100
#print(stack)


from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

queue.popleft()
print(queue)




#priority queue

import heapq

arr = [50,30,20,10,40]

heapq.heapify(arr)

#print(arr)

#Min Heap
heap = []

heapq.heappush(heap, 10)
heapq.heappush(heap, 55)
heapq.heappush(heap, 20)
heapq.heappush(heap, 25)

heapq.heapify(heap)
smallest = heapq.heappop(heap)
#print(heap)
#print(smallest)

#Max Heap

heap = []

heapq.heappush_max(heap, 10)
heapq.heappush_max(heap, 15)
heapq.heappush_max(heap, 20)
heapq.heappush_max(heap, 25)

largest = heapq.heappop_max(heap)
#print(heap)
#print(largest)




#Exercise find 3rd largest number in the array 

arr = [10,50,20,40,60,70,90]

heap = arr.copy()
heapq._heapify_max(heap)

for i in range (3):
    largest = heapq.heappop_max(heap)
    
print(largest)
    
    

    