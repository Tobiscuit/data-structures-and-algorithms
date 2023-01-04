class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp


# my_stack = Stack(7)
# my_stack.push(23)
# my_stack.push(3)
# my_stack.push(11)
# print(my_stack.pop(), "\n")
# my_stack.print_stack()

# Queues
# FIFO - First in, First out
# When we add items to the queue, we use the term enqueue
# When we remove items from the queue, we use the term dequeue
# For something to be a queue, you add on one end, and remove from the other end. With a list, removing and adding from the end, is O(1), but on the other end of a list, removing, and adding, is O(n)
# So if you have a queue, let's say we're going to add on this end, (the end of the line, or the start of the queue, which begins at index 0), and we're gonna remove on this end (the end of the list), we have one way that is O(n), and one way that is O(1). Likewise, if we add on this end (the front of the line, or the end of the list), and remove on this end, the start or back of the line, we still have one end that is O(n) and one end that is O(1).
# In comparison to a linked list, linked lists are O(n) to remove at the end, but adding it back on is O(1). On the other end of the linked list, or the start, removing is O(1), and adding it back on is also O(1). So for a linked list we have three O(1)'s, and one O(n). And that means, what you don't want to do, is you don't want to dequeue from this end (the end of the linked list) because it's O(n). You want to enqueue from this end (the end of the linked list), and dequeue from this end (the start of the linked list). Because both of those, are O(1). With a linked list we call these head and tail, a change that we're gonna have for it to be a queue is we're just gonna call these 'first' and 'last'. And this, is our intro, to queues.

# In order to build this, the first thing we have to build is a Node


class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


my_queue = Queue(1)
my_queue.enqueue(2)

my_queue.print_queue()

print("Dequeued Succesful! \n")
print(my_queue.dequeue(), "\n")
print(my_queue.dequeue(), "\n")
print(my_queue.dequeue(), "\n")

my_queue.print_queue()
