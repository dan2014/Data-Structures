class Stack:
    def __init__(self):
        self.list = []

    def __repr__(self):
        if(self.len() == 0):
            return  "The stack is empty" 
        else:
            for i in reversed(self.list):
                print(f"{i}")
            return ""

    def push(self, item):
        self.list.append(item)
  
    def pop(self):
        if( self.len() > 0 ):
            self.list.pop()
        else:
            print( "Cannot pop an element off the stack when the stack is empty" )
            return

    def len(self):
        return len(self.list)

if __name__ == "__main__":
    test_stack = Stack()
    test_stack.push(3)
    test_stack.push(4)
    test_stack.push(5)
    print(test_stack)
    test_stack.pop()
    print(test_stack)
    test_stack.push(6)
    print(test_stack)
    test_stack.pop()
    print(test_stack)
    test_stack.pop()
    print(test_stack)
    test_stack.pop()
    print(test_stack)
    test_stack.pop()