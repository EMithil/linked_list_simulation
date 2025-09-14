# linked_list.py
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    def display(self):
        temp = self.head
        result = []
        while temp:
            result.append(temp.data)
            temp = temp.next
        print("LinkedList:", result)

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(37)
    ll.insert(34)
    ll.insert(43)
    print("linked list after inserting 37, 34, 43")
    ll.display()
    ll.delete(37)
    print("linked list after deleting 37")
    ll.display()


