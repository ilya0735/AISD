from RingBufferQueue import RingBufferQueue, QueueOverflowException


def data_show(picked_queue):
    print("===========================================================================================================")
    print("Данные очереди:")
    print(f"Размер: {picked_queue.size()}")
    print(f"Голова: {picked_queue.peek()}")
    print(f"Пустота: {picked_queue.is_empty()}")
    print(f"Полнота: {picked_queue.is_full()}")
    print(f"Список: {picked_queue.to_list()}")
    print("===========================================================================================================")

def main():
    print("===========================================================================================================")
    print("создаем список длинной 4 и добавим туда 4 элемента")
    queue = RingBufferQueue(4)
    queue.enqueue(12)
    queue.enqueue(23)
    queue.enqueue(31)
    queue.enqueue(42)

    data_show(queue)


    print("===========================================================================================================")
    print("Удалим 2 элемента")
    queue.dequeue()
    queue.dequeue()

    data_show(queue)


    print("===========================================================================================================")
    print("добавим 1 элемент, что бы посмотреть на реализацию закольцованности")
    queue.enqueue(11)

    data_show(queue)

    print("===========================================================================================================")
    print("Удалим все элементы")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    data_show(queue)

    print("===========================================================================================================")
    print("Проверка переполнения")
    print("===========================================================================================================")
    try:
        queue.enqueue(21)
        queue.enqueue(12)
        queue.enqueue(23)
        queue.enqueue(31)
        queue.enqueue(42)
    except QueueOverflowException:
        print("Ошибка QueueOverflowException обработана")

    data_show(queue)

if __name__ == '__main__':
    main()