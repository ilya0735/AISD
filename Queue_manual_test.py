import pytest

from RingBufferQueue import RingBufferQueue, QueueOverflowException


def enqueue_test():
    obj = RingBufferQueue(10)
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(123123)

    assert obj.tail == 2 + 1
    assert obj.length == 3
    return obj.to_list(), obj.queue

def dequeue_test():
    obj = RingBufferQueue(4)
    obj.enqueue(1213)
    obj.enqueue(2312)
    obj.enqueue(123123)
    obj.dequeue()

    assert obj.queue[obj.tail-1] == 123123
    assert obj.queue[obj.head] == 2312
    return obj.to_list(), obj.queue

def peek_test():
    obj = RingBufferQueue(4)

    assert obj.is_empty()
    obj.enqueue(1)
    obj.enqueue(2)
    assert obj.peek() == 1

def is_empty_test():
    obj = RingBufferQueue(4)

    assert obj.is_empty()
    obj.enqueue(1)
    assert not obj.is_empty()

def is_full_test():
    obj = RingBufferQueue(3)

    assert not obj.is_full()
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    assert obj.is_full()

def size_test():
    obj = RingBufferQueue(4)
    obj.enqueue(1)
    obj.enqueue(2)
    obj.enqueue(3)
    obj.dequeue()
    assert obj.length == 2

def to_list_test():
    obj = RingBufferQueue(4)
    obj.enqueue(12)
    obj.enqueue(23)
    obj.enqueue(123123)
    obj.dequeue()
    assert obj.to_list() == [23, 123123]

def test_overflow():
    with pytest.raises(QueueOverflowException):
        obj = RingBufferQueue(1)
        obj.enqueue(1)
        obj.enqueue(2)


enqueue_test()
dequeue_test()
peek_test()
is_empty_test()
is_full_test()
size_test()
to_list_test()