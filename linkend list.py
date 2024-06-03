class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def insert(self, prev_node, new_data):
        if prev_node is None:
            print("Error")
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node


    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def check(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            if last.next == new_node:
                return last.next
            last = last.next

l_list = LinkedList()
a = Node(25)
b = Node(20)
c = Node(53)
d = Node(12)
e = Node(67)
f = Node(84)
h = Node(36)
l_list.head = a
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = h
print("Dastlabki: ", l_list.printList())

l_list.append(25)
print("Append: ", l_list.printList())

l_list.insert(Node(12), 30)
print("Insert: ", l_list.printList())

l_list.check(12)
print("Check: ", l_list.printList())

l_list.push(13)
print("Push: ", l_list.printList())

print(l_list.printList())