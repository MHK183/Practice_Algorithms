import sys

def push(n):
    stack.append(n)
def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop()
def size():
    print(len(stack))
def empty():
    if len(stack) == 0:
        print(1)
    else:
        print(0)
def top():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])

stack = []

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
    elif command[0] == 'top':
        top()