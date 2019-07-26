class Queue:
  def __init__(self):
    self.size = 0
    # what data structure should we
    # use to store queue elements?
    self.storage = []

  def __repr__(self):
    if(self.len() == 0):
        return  "The queue is empty" 
    else:
        for i in reversed(self.storage):
            print(f"{i}")
        return ""

  def enqueue(self, item):
    self.storage.append(item)
    self.size += 1
  
  def dequeue(self):
      if( self.len() > 0 ):
        temp = self.storage[0]
        self.storage.pop(0)
        self.size -= 1
        return temp
      else:
        pass

  def len(self):
    return self.size

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