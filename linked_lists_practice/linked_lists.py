class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    node_count = 0

    def __init__(self):
        self.head = None

    @classmethod
    def increment_node_count(cls):
        cls.node_count += 1
        return cls.node_count

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
            LinkedList.increment_node_count()
        else:
            temp = self.head
            while(self.head.next != None):
                self.head = self.head.next
            self.head.next = Node(value)
            LinkedList.increment_node_count()
            self.head = temp

    def prepend(self):
        pass

    def find(self,value):
        temp = self.head
        count = 0
        found_val = None
        if(self.head is None):
            return(f"There are no nodes in the Linked List")
        else:
            while( self.head.value != value ):
                if self.head.next is None:
                    return(f"{value} was not found in the Linked List")
                count += 1
                self.head = self.head.next
        found_val = self.head.value
        self.head = temp
        return(f"{found_val} was found and is the {count}th node in Linked List")


if __name__ == "__main__":
    test = LinkedList()
    test.append(6)
    test.append(5)
    test.append(4)
    print(test.find(4))
    # test.append(5)
