class QueueOverflowException(Exception):
    pass


class RingBufferQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None for _ in range(self.capacity)]
        self.head = None
        self.tail = None

    # тоже добавленая от себя функция, которая проверяет положение нашей очереди и определяет хвост и голову.
    def auto_detection(self):
            if self.queue[0] is None:
                for index in range(len(self.queue)-1):
                    self.queue[index] = self.queue[index+1]
                if all([type(x) is int for x in self.queue]):
                    self.queue[self.capacity-1] = None


            index = 0
            for element in self.queue:
                if element is not None:
                    self.head = index
                    break
                index += 1
            if self.queue[0] is None:
                self.head = None

            index = 0
            for element in self.queue:
                if element is None:
                    self.tail = index-1
                    break
                index += 1
            if self.tail == -1:
                self.tail = None
            if all([type(x) is int for x in self.queue]):
                self.tail = self.capacity-1


    def enqueue(self, value: int) -> None:
        if all([type(x) is int for x in self.queue]):
            raise QueueOverflowException("Очередь переполнена")
        for element in self.queue:
            if element is None:
                if self.head is None:
                    self.queue[0] = value
                else:
                    self.queue[self.tail+1] = value
        self.auto_detection()


    def dequeue(self) -> int | None:
        deleted_element = self.queue[self.head]
        self.queue[self.head] = None
        self.auto_detection()
        return deleted_element


    def peek(self) -> int | None:
        return self.queue[self.head]

    def is_empty(self) -> bool:
        return all([type(x).__name__ == "NoneType" for x in self.queue])

    def is_full(self) -> bool:
        return all([type(x) is int for x in self.queue])

    def size(self) -> int:
        count = 0
        for element in self.queue:
            if element is not None:
                count += 1
        return count

    def to_list(self) -> list[int | None]:
        return [x for x in self.queue if x is not None]

    # Это для отслеживания хвоста и головы когда код писал
    def check(self):
        return self.queue, self.head, self.tail

    # От себя добавил то что на проге проходили
    def __iter__(self):
        return iter([x for x in self.queue if x is not None])





# ТЕСТЫ
try:
    RBQ = RingBufferQueue(capacity=4)
    RBQ.enqueue(1)
    RBQ.enqueue(2)
    RBQ.enqueue(3)
    RBQ.enqueue(4)
    RBQ.dequeue()
    RBQ.dequeue()
    RBQ.dequeue()
    RBQ.enqueue(5)

    print(RBQ.is_empty())
    print(RBQ.is_full())
    print(RBQ.size())
    print(RBQ.to_list())
    print(RBQ.check())
except QueueOverflowException as e:
    print(e)

RBQ = RingBufferQueue(capacity=5)
RBQ.enqueue(123)
RBQ.enqueue(2)
RBQ.enqueue(3)
RBQ.enqueue(4)
RBQ.enqueue(5)
RBQ.dequeue()
for element in RBQ:
    print(element)






