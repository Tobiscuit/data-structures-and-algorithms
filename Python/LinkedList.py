# class LinkedList:
#     def __init__(self, value):
#         create new Node

#     def append(self, value):
#         create new Node
#         add Node to end

#     def prepend(self, value):
#         create new Node
#         add Node to the beginning

#     def insert(self, index, value):
#         create new Node
#         insert Node


# So as we can see, these all create a new node
# We don't want to write the code for creating a new node 4 diffferent times for each method, as shown above. So we're going to create a class, that does nothing, but create nodes. And we're gonna call that class: Node
# ^ If any of the four methods above needs to create a node, it will call on, the Node class, to create it.
# The only thing it's going to contain, is a constructor, which we're gonna pass a value, so we can assign it, to the node
# As for the rest of the constructor, let's look again at what a node is.
# When you have values that apply to a specific instance, remember you use the self keyword. self.value, and self.next
# ^ So the constructor, for the node, is going to look like this:
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


# Now that we have a way of creating Nodes, we can build out our LinkedList constructor.


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


my_linked_list = LinkedList(4)

# print(my_linked_list.head.value)

# Append Method


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while (temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp  # add .value at the end to access the node's value. we typically want to return the whole node however, this .value is just for testing purposes.

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp # not true, because we are returning a Node

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


# reverse
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list()

# set method
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# my_linked_list.set_value(1, 4)

# my_linked_list.print_list()

        
# my_linked_list = LinkedList(0)
# my_linked_list.append(1)
# my_linked_list.append(2)
# my_linked_list.append(3)

# print(my_linked_list.get(2))
# my_linked_list = LinkedList(2)
# my_linked_list.append(1)

# my_linked_list.append(3)

# my_linked_list.prepend(1)

# my_linked_list.print_list()

# (2) Items - Returns 2 Node
# print(my_linked_list.pop())
# # (1) Item - Returns 1 Node
# print(my_linked_list.pop())
# # (0) Items - Returns None
# print(my_linked_list.pop())

# // .pop_first()
# (2) Items - Returns 2 Node
# print(my_linked_list.pop_first())
# # (1) Items - Returns 1 Node
# print(my_linked_list.pop_first())
# # (0) Items - Returns None
# print(my_linked_list.pop_first())

# Insert Method test cases
# my_linked_list = LinkedList(0)
# my_linked_list.append(2)
# my_linked_list.insert(1, 1)
# # print(my_linked_list)

# my_linked_list.print_list()

# Linked List Remove Test Case
# my_linked_list = LinkedList(11)
# my_linked_list.append(3)
# my_linked_list.append(23)
# my_linked_list.append(7)

# print(my_linked_list.remove(2), '\n')

# my_linked_list.print_list()
