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
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    if self.head is None:
      self.head = ListNode(value)
      self.tail = self.head
      self.length += 1
    else: 
      self.head.insert_before(value)
      self.head = self.head.prev
      self.length += 1

  def remove_from_head(self):
    if self.head is None:
      return None
    else: 
      temp = self.head.value
      self.delete(self.head)
      return temp
    

  def add_to_tail(self, value):
    if self.head is None:
      self.head = ListNode(value)
      self.tail = self.head
      self.length += 1
    else: 
      self.tail.insert_after(value)
      self.tail = self.tail.next
      self.length += 1


  def remove_from_tail(self):
    if self.head == self.tail:
      temp = self.head.value
      self.head = None
      self.tail = None
      self.length = 0
      return temp
    else:
      temp = self.tail.value
      self.tail.delete()
      self.length -= 1
      return temp

  def move_to_front(self, node):
    found = self.delete(node)
    if found:
      self.add_to_head(node.value)

  def move_to_end(self, node):
    found = self.delete(node)
    if found is None:
      self.add_to_tail(node.value)
    elif found:
      self.add_to_tail(node.value)

  def delete(self, node):
    if self.head == node and self.head.next is not None:
      self.head = self.head.next
      self.head.prev = None
      self.length -= 1
    elif self.head == node and self.head == self.tail:
      self.head = None
      self.tail = None
      self.length -= 1
    else:
      headCopy = self.head
      found = False
      while(headCopy.next is not None):
        if(headCopy.next == node):
          headCopy = headCopy.next
          headCopy.delete()
          self.length -= 1
          found = True
          break
        else:
          headCopy = headCopy.next
      print(found,"delete")
      return found
      

    
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
