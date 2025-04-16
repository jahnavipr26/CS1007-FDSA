class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def delete_node(self, data):
        current = self.head

        while current:
            if current.data == data:
              
                if current.prev is None:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                else:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                return  
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_beginning(20)
    dll.insert_at_beginning(30)
    print("List after insertions:")
    dll.print_list()

    dll.delete_node(20)
    print("List after deleting node with data 20:")
    dll.print_list()
