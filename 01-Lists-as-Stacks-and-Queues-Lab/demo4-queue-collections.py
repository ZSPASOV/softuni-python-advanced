from collections import deque
queue = deque([1, 2, 3, 4, 5])
queue.popleft()
queue.append(6)
print(queue) # deque([2, 3, 4, 5, 6])
print(type(queue)) # <class 'collections.deque'>
queue.rotate(1) # 1 is the number of times it is rotated
print(queue) # deque([6, 2, 3, 4, 5])
queue.rotate(2) # 1 is the number of times it is rotated
print(queue) # deque([4, 5, 6, 2, 3])





