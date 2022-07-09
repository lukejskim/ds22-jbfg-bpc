class Queue:
    def __init__(self):
        self.queue_items = []

    # enqueue 기능 구현
    def enqueue(self, x):
        self.queue_items.append(x)
        return None

    # dequeue 기능 구현
    def dequeue(self):
        item_length = len(self.queue_items)
        if item_length < 1:
            print("Queue is empty!")
            return False
        result = self.queue_items[0]
        del self.queue_items[0]
        return result

    # is_empty 기능 구현
    def is_empty(self):
        return not self.queue_items

    # state 체크 구현
    def chk_state(self):
        print("Queue = {}".format(self.queue_items))


# 테스트 코드
testQueue = Queue()
print(testQueue.queue_items)
testQueue.enqueue('찬영')
print(testQueue.queue_items)
print(testQueue.dequeue())
testQueue.enqueue('준영')
testQueue.enqueue('채영')
testQueue.enqueue('예영')
testQueue.enqueue('민영')
print(testQueue.queue_items)
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.queue_items)
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.dequeue())
print(testQueue.is_empty())


