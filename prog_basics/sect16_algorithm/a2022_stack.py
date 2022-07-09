class Stack:
    def __init__(self):
        self.stack_items = []

    # pop 기능 구현
    def pop(self):
        item_length = len(self.stack_items)

        # 스택이 비어있을때는 에러메세지 출력
        if item_length < 1:
            print("Stack is empty!")
            return False

        # 가장 위에 있는 item을 반환하며 삭제
        result = self.stack_items[item_length - 1]
        del self.stack_items[item_length - 1]
        return result

    # push 기능 구현
    def push(self, x):
        self.stack_items.append(x)

    # is_empty 기능 구현
    def is_empty(self):
        return not self.stack_items

    # stack 체크 구현
    def chk_state(self):
        print("Stack = {}".format(self.stack_items))


# 테스트 코드
testStack = Stack()
print(testStack.stack_items)
testStack.push(0)
print(testStack.stack_items)
testStack.push(2)
print(testStack.stack_items)
testStack.push(4)
testStack.push(6)
testStack.push(8)
print(testStack.stack_items)
print(testStack.is_empty())
print(testStack.pop())
print(testStack.pop())
print(testStack.pop())
print(testStack.pop())
print(testStack.pop())
print(testStack.pop())
print(testStack.is_empty())



