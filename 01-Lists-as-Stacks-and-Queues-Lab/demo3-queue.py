# A queue is a first-in first-out (FIFO) abstract data type
# We use them when we want things to happen in the order that they were called
# It is possible to use a list as a queue, however they are not efficient for this purpose
# Doing inserts or pops from the beginning of a list is slow
# That's why we use collections.deque
# We use append() to add to the queue and popleft() to remove from the queue
