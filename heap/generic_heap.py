class Heap:
  def __init__(self, comparator=lambda x,y: x > y):
    self.storage = []
    self.comparator = comparator

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(self.get_size() - 1 )

  def delete(self):
    popped = self.storage[0]
    self.storage[0] = self.storage[self.get_size() - 1]
    self.storage.pop()
    self._sift_down(0)
    return popped

  def get_priority(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while(index > 0):
      parent = ( index - 1) // 2
      if self.comparator( self.storage[index], self.storage[parent] ):
        self.storage[parent],self.storage[index] = self.storage[index], self.storage[parent]
      index = parent

  def _sift_down(self, index):
    left_idx = lambda idx: idx*2 + 1
    right_idx = (lambda idx: idx*2 + 2 )if self.get_size() > 2 else (lambda idx: idx*2 + 1)
    while(right_idx(index) <= self.get_size() - 1):
      left = left_idx(index)
      right = right_idx(index)
      if self.comparator( self.storage[left] , self.storage[index]) and (self.comparator( self.storage[left] , self.storage[right]) or self.storage[left] == self.storage[right]):
        self.storage[index],self.storage[left] = self.storage[left], self.storage[index]
        index = left
      elif self.comparator( self.storage[right] , self.storage[index]) and (self.comparator( self.storage[right] , self.storage[left]) or self.storage[right] == self.storage[left]):
        self.storage[index],self.storage[right] = self.storage[right], self.storage[index]
        index = right
      else:
        break

if __name__ == "__main__":
  test = Heap(lambda x,y: x < y)
  test.storage = [10, 20, 30, 40] + [15, 25, 35] + [27, 29, 37, 48, 93] + [32, 33]
  # test_arr = [15, 25, 35] + [27, 29, 37, 48, 93] + [32, 33]
  # for i in test_arr:
  #   test.insert(i)
  print(test.storage)
  while test.get_size() > 0:
      print(test.delete())
