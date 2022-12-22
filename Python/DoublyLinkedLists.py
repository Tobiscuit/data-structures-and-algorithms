class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

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

    def append(self, value):
        new_node = Node(value)
        # temp = self.head
        # self.head =

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self):
        # if self.length == 0:
        #     return None
        # temp = self.tail
        # self.tail = self.tail.prev
        # self.tail.next = None
        # temp.prev = None
        # self.length -= 1
        # if self.length == 0:
        #     self.head = None
        #     self.tail = None
        # return temp
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head == None
            self.tail == None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
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
        before = self.get(index - 1)
        after = before.next
        # You got it right, it might (or is) be more semantically correct to start with the two arrows on the new node
        # before.next = new_node
        # new_node.prev = before
        # new_node.next = after
        # after.prev = new_node
        # See below
        new_node.prev = before
        new_node.next = after
        # then we adjust the "before" to point to the new_node we are inserting
        before.next = new_node
        after.prev = new_node
        # These four lines of code redirected these four arrows
        # Then we need to increase the length by 1
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp

# testing remove()
my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)

print(my_doubly_linked_list.remove(1), "\n")

my_doubly_linked_list.print_list()


# my_doubly_linked_list = DoublyLinkedList(11)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.append(23)
# my_doubly_linked_list.append(7)

# my_doubly_linked_list.set_value(1, 4)

# my_doubly_linked_list = DoublyLinkedList(1)
# my_doubly_linked_list.append(3)
# my_doubly_linked_list.insert(1, 2)

# print(my_doubly_linked_list.get(1))
# print(my_doubly_linked_list.get(2))

# # (2) Items - Returns 2 Node
# print(my_doubly_linked_list.pop())
# # (1) Item - Returns 1 Node
# print(my_doubly_linked_list.pop())
# # (0) Items - Returns None
# print(my_doubly_linked_list.pop())

# my_doubly_linked_list.print_list()

