from collections import deque

queue = deque()
queue.appendleft('Edna')
queue.appendleft('Adhiambo')
queue.appendleft('Kesa')

print(queue)
print(queue.popleft())
print(queue.pop())
