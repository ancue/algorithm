'''
05-用两个栈实现队列

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''


class Queue():
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        self.stack1.append(node)

    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return None
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


q = Queue()
print('queue')
print(q.pop())
q.push(2)
q.push(3)
q.push(3)
q.push(5)
print(q.pop())
print(q.pop())
print(q.pop())

'''
两个队列实现栈
'''


class Stack():
    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        if self.queue1 == []:
            self.queue2.append(x)
        else:
            self.queue1.append(x)

    def pop(self):
        if not self.queue1 and not self.queue2:
            return
        if self.queue1 != []:
            for i in range(len(self.queue1) - 1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        else:
            for i in range(len(self.queue2) - 1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()


s = Stack()
print('\nstack')
print(s.pop())
s.push(0)
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.pop())
print(s.pop())
print(s.pop())

'''
20-包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''


class StackMin():
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            temp = self.min()
            self.minStack.append(temp)

    def pop(self):
        if self.stack == [] or self.minStack == []:
            return None
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.minStack[-1]


'''
21-栈的压入、弹出序列

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4，5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''


def isPopOrder(pushList, popList):
    if not pushList or not popList:
        return False
    stack = []
    for i in pushList:
        stack.append(i)
        # 发现与弹出序列第一个元素相同
        # 从stack和popList中pop掉
        while len(stack) and stack[-1] == popList[0]:
            stack.pop()
            popList.pop(0)
    # 只用栈抵消的题目，最后都是判断是否还有剩下的元素
    return len(stack) == 0


print('\nisPopOrder')
print(isPopOrder([], [1]))
print(isPopOrder([1], []))
print(isPopOrder([1, 2, 3, 4, 5], [4, 3, 5, 2, 1]))
