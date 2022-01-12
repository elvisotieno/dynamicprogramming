# using list

# Initializing a queue
queue = []

# Adding elements to the queue(Enque)
queue.append('a')
queue.append('b')
queue.append('c')
queue.append('d')

print("Initial queue")
print(queue)

# Removing elements from the queue(Dequeue)
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

# Uncommenting print(queue.pop(0))
# will raise and IndexError
# as the queue is now empty



#Implementation using collections.deque
# Python program to
# demonstrate queue implementation
# using collections.dequeue


from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

# Uncommenting q.popleft()
# will raise an IndexError
# as queue is now empty

#implementation using cyclic buffer
N=4
queue = [0] * N
head, tail = 0, 0


def push(x):
    global tail
    tail = (tail + 1) % N
    queue[tail] = x


def pop():
    global head
    head = (head + 1) % N
    return queue[head]


def size():
    return (tail - head + N) % N


def empty():
    return head == tail