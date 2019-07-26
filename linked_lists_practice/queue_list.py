class Queue:
    def __init__(self):
        self.list = []

    def __repr__(self):
        if(self.len() == 0):
            return  "The queue is empty" 
        else:
            for i in reversed(self.list):
                print(f"{i}")
            return ""

    def enqueue(self, item):
        self.list.append(item)
  
    def dequeue(self):
        if( self.len() > 0 ):
            self.list.pop(0)
        else:
            print( "Cannot dequeue an element when the queue is empty" )
            return

    def len(self):
        return len(self.list)

if __name__ == "__main__":
    test_queue = Queue()
    test_queue.enqueue(3)
    test_queue.enqueue(4)
    test_queue.enqueue(5)
    print(test_queue)
    test_queue.dequeue()
    print(test_queue)
    test_queue.enqueue(6)
    print(test_queue)
    test_queue.dequeue()
    print(test_queue)
    test_queue.dequeue()
    print(test_queue)
    test_queue.dequeue()
    print(test_queue)
    test_queue.dequeue()

