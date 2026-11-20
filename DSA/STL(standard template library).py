stack = []

stack.append(10)
stack.append(20)
stack.append(30)

stack.pop(1)
stack[1] = 100
print(stack)


from collections import deque

queue = deque()

queue.append(10)
queue.append(20)
queue.append(30)

queue.popleft()
print(queue)

