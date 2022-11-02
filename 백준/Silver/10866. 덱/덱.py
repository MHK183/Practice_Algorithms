import sys

def push_front(n):
    deque.insert(0, n)
def push_back(n):
    deque.append(n)
def pop_front():
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[0])
        deque.pop(0)
def pop_back():
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[-1])
        deque.pop()
def size():
    print(len(deque))
def empty():
    if len(deque) == 0:
        print(1)
    else:
        print(0)
def front():
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[0])
def back():
    if len(deque) == 0:
        print(-1)
    else:
        print(deque[-1])

deque = []

for _ in range(int(input())):
    command = sys.stdin.readline().rstrip().split()
    if len(command) == 2:
        if command[0] == 'push_front':
            push_front(int(command[1]))
        elif command[0] == 'push_back':
            push_back(int(command[1]))
    elif command[0] == 'pop_front':
        pop_front()
    elif command[0] == 'pop_back':
        pop_back()
    elif command[0] == 'size':
        size()
    elif command[0] == 'empty':
        empty()
    elif command[0] == 'front':
        front()
    elif command[0] == 'back':
        back()