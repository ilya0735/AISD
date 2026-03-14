class QueueOverflowException(Exception):
    pass

class RingBufferQueue:

    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None for _ in range(self.capacity)]
        self.head = 0
        self.tail = 0
        self.length = 0

    def enqueue(self, value):
        if self.length == self.capacity:
            raise QueueOverflowException()

        self.queue[self.tail] = value
        self.tail = (self.tail + 1) % self.capacity
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None

        value = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.length -= 1
        return value

    def peek(self) -> int | None:
        return self.queue[self.head]

    def is_empty(self) -> bool:
        return all(x is None for x in self.queue)

    def is_full(self) -> bool:
        return all([type(x) is int for x in self.queue])

    def size(self) -> int:
        return self.length

    def to_list(self) -> list[int | None]:
        result = []
        for i in range(self.length):
            index = (self.head + i) % self.capacity
            result.append(self.queue[index])
        return result

    # Это для отслеживания хвоста и головы когда код писал
    def check(self):
        if self.tail == 0:
            return self.queue, self.head, self.capacity-1
        return self.queue, self.head, self.tail-1
