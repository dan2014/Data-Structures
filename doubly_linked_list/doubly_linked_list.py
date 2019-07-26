"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
import functools

class DoublyLinkedList:

  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def empty_check(func):
    def wrapper(self,value):
      if self.head is None:
        self.head = ListNode(value)
        self.tail = self.head
        self.length += 1
      else:
          func(self,value)
    return wrapper

  @empty_check
  def add_to_head(self, value):
    self.head.insert_before(value)
    self.head = self.head.prev
    self.length += 1

  def remove_from_head(self):
    if self.head is None:
      return None
    elif self.length == 1:
      temp = self.head.value
      self.head = None
      self.tail = None
      self.length = 0
      return temp
    else: 
      temp = self.head.value
      self.head = self.head.next
      self.head.prev = None
      self.length -= 1
      return temp
    
  @empty_check
  def add_to_tail(self, value):
    self.tail.insert_after(value)
    self.tail = self.tail.next
    self.length += 1


  def remove_from_tail(self):
    if self.tail is None:
      return None
    elif self.length == 1:
      temp = self.tail.value
      self.head = None
      self.tail = None
      self.length = 0
      return temp
    else:
      temp = self.tail.value
      self.tail = self.tail.prev
      self.tail.next = None
      self.length -= 1
      return temp

  def move_to_front(self, node):
    if node is self.head:
      return node
    self.delete(node)
    self.add_to_head(node.value)

  def move_to_end(self, node):
    if node is self.tail:
      return node
    self.delete(node)
    self.add_to_tail(node.value)

  def delete(self, node):
    if self.length == 0:
      pass 
    elif node == self.head:
      self.remove_from_head()
    elif node is self.tail:
      self.remove_from_tail()
    else:
      node.delete()
      self.length -=1 # this assumes that the node exists in the dll
    
  def get_max(self):
    maxVal = self.head.value
    headCopy = self.head
    while(headCopy.next is not None):
      if(headCopy.next.value > maxVal):
        maxVal = headCopy.next.value
        headCopy = headCopy.next
      else:
        headCopy = headCopy.next
    return maxVal

