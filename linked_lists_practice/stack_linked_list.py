class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

    
class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            # self.head.next = self.head
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next

    def remove(self):
        if self.head is None:
            return "There are no nodes to remove"
        
        elif self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            # print(self.head.next,"self.head.next")


if __name__ == "__main__":
    test = Stack()
    test.append(6)
    print(test.head.value)
    print(test.tail.value)
    print(test.head.next is test.head)
    test.append(5)
    print(test.head.value)
    print(test.tail.value)
    print(test.head.next is test.head)
    print(test.head.next is test.tail)
    test.append(4)
    print(test.head.value)
    print(test.tail.value)
    print(test.head.next is test.head)
    print(test.head.next is test.tail)
    print(test.head.next.next is test.tail)
    print("==========================")
    test.remove()
    print(test.head.value)
    print(test.tail.value)
    print("==========================")
    test.remove()
    print(test.head.value)
    print(test.tail.value)
    print("==========================")
    test.remove()
    print(test.head)
    print(test.tail)
    test.append(7)
    print(test.head.value)
    print(test.tail.value)
    print(test.head is test.tail)
    test.append(8)
    print(test.head.value)
    print(test.tail.value)
    print(test.head is test.tail)
    # print(test.tail.value)
    # test.append(5)
