import sys


class CQueue:
    def __init__(self, max_size):
        self.max_size = max_size
        self.container = [None for _ in range(self.max_size)]
        self._front = 0
        self._rear = 0

    def empty(self):
        if self._front == self._rear:
            return 1
        return 0

    def __step_forward(self, x):
        x += 1
        if x >= self.max_size:
            x = 0
        return x

    def is_full(self):
        next = self.__step_forward(self._rear)
        if next == self._front:
            return True
        return False

    def push(self, data):
        if self.is_full():
            return
        self.container[self._rear] = data
        self._rear = self.__step_forward(self._rear)

    def pop(self):
        if self.empty():
            return -1
        ret = self.container[self._front]
        self._front = self.__step_forward(self._front)
        return ret

    def size(self):
        if self._rear >= self._front:
            return self._rear - self._front
        else:
            return self.max_size - (self._front - self._rear)

    def front(self):
        if self.empty():
            return -1
        return self.container[self._front]

    def back(self):
        if self.empty():
            return -1
        return self.container[self._rear - 1]

input = sys.stdin.readline

N = int(input())
queue = CQueue(N+1)

for _ in range(N):
    command = input().strip()

    if command.startswith('push'):
        key, value = command.split()
        queue.push(int(value))
    elif command == 'pop':
        print(queue.pop())
    elif command == 'size':
        print(queue.size())
    elif command == 'empty':
        print(queue.empty())
    elif command == 'front':
        print(queue.front())
    elif command == 'back':
        print(queue.back())
