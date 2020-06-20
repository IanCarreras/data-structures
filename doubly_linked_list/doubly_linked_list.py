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
        self.max = None

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value)
        # add new node to head of list and set prev and next
        # if list is empty new node is max
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.max = new_node.value
        elif self.length == 1:
            new_node.next = self.head
            self.head = new_node
            self.tail = new_node.next
            self.tail.prev = self.head
        elif self.length > 1:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # compare new node with prev head and set max
        if (self.length > 0 and self.head.value > self.head.next.value):
            self.max = self.head.value
        self.length += 1

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.length == 0 or self.length == 1:
            self.head = None
            self.max = None
        # if list has more than one element; set new head and delete prev head
        if self.length > 1:
            self.head = self.head.next
            self.head.prev.delete()
            # compare new head and next value, return greater value
            if (self.length == 2 or self.head.value > self.head.next.value):
                self.max = self.head.value
            else:
                self.max = self.head.next.value
        self.length -=1

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.max = self.head.value
        elif self.length == 1:
            new_node.prev = self.head
            self.head.next = new_node
            self.tail = new_node
        elif self.length > 1:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        if (self.length > 0 and self.tail.value > self.tail.prev.value):
            self.max = self.tail.value
        self.length += 1

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.length == 0 or self.length == 1:
            self.head = None
            self.max = None
        if self.length > 1:
            self.tail = self.tail.prev
            self.tail.next.delete()
            if (self.length == 2 or self.tail.value > self.tail.prev.value):
                self.max = self.tail.value
            else:
                self.max = self.tail.next.value
        self.length -= 1

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        pass

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        pass

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        current = self.head
        while current:
            if current.value == node:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                current.delete()
            current = current.next
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        print(self.max)

    def print_list(self):
        output = ''
        current = self.head
        while current:
            output += f'<- {current.value} ->'
            current = current.next
        print(output)

x = DoublyLinkedList()

x.add_to_head(3)
x.print_list()
x.get_max() 

x.add_to_head(6)
x.print_list()
x.get_max() 

x.add_to_head(7)
x.print_list()
x.get_max()

x.add_to_head(6)
x.print_list()
x.get_max() 

print('delete')
x.delete(3)
x.print_list()