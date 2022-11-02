import sys

def push(n):
    queue.append(n)
def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
        queue.pop(0)
def size():
    print(len(queue))
def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)
def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])
def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])

queue = []

for _ in range(int(input())):
    command = sys.stdin.readline().rstrip().split()
    if len(command) == 2:
        push(int(command[1]))
    elif command[0] == 'pop':
        pop()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()