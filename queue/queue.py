"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

class Node:
  def __init__(self, value = None, next_node = None):
    self.value = value
    self.next_node = next_node

class LinkedList:
  def __init__(self):
    self.head = None 
    self.tail = None 
  
  def add_to_head(self, value):
    new_node = Node(value)
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next_node = self.head
      self.head = new_node

  def add_to_tail(self, value):
    new_node = Node(value)
    if self.head is None and self.tail is None:
      self.head = new_node
      self.tail = new_node
    else:
      self.tail.next_node = new_node
      self.tail = new_node

  def remove_head(self):
    if not self.head:
      return None
    if self.head.next_node is None:
      head_value = self.head.value
      self.head = None
      self.tail = None
      return head_value
    head_value = self.head.value
    self.head = self.head.next_node
    return head_value     

  def contains(self, value):
    if self.head is None:
      return False
    
    current_node = self.head

    while current_node is not None:
      if current_node.value == value:
        return True

      current_node = current_node.next_node
    return False 

  def print_list(self):
    current = self.head
    while current:
      print(f'{current.value} ->')
      current = current.next_node

linked list
class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size +=1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size == 0:
            return None
        else:
            self.size -= 1
            value = self.storage.remove_head()
            return value

# array
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)
#         return self.storage

#     def dequeue(self):
#         if len(self.storage) == 0:
#             return None
#         else:
#             return self.storage.pop(0)