class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value <= self.value:
      if isinstance(self.left, BinarySearchTree):
        self.left.insert(value)
      else:
        self.left = BinarySearchTree(value)
    else:
      if isinstance(self.right, BinarySearchTree):
        self.right.insert(value)
      else:
        self.right = BinarySearchTree(value)

  def contains(self, target):
    if self.value == target:
        return True
    elif self.left is None and self.right is None:
      return False
    elif target < self.value:
      return self.left.contains(target)
    else:
      return self.right.contains(target)


  def get_max(self):
    max_num = self.value
    def find_max(node):
      nonlocal max_num
      if node.value > max_num:
        max_num = node.value

      if node.right is None:
        return 

      find_max(node.right)

    find_max(self)
    return max_num



  @staticmethod
  def printVal(val):
    print(val)

  def for_each(self, cb):
    count_depth = 0
    height_arr = [[]]
    def nested(height,node):

      if isinstance(node,BinarySearchTree):
        if len(height_arr) == height:
          height_arr.append([])
        cb(node.value)
        height_arr[height].append(node.value)
        height += 1
        nested(height,node.left)
        nested(height,node.right)

    nested(count_depth,self)
    return height_arr

if __name__ == "__main__":
  root = BinarySearchTree(5)
  # print(root.for_each(BinarySearchTree.printVal))
  print(root.get_max())

  # root.insert(20)