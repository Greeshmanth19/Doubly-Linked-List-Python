class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # inserting at the beginning of the DLL
    def insert_at_beginning(self, data):    # time complexity O(1)
        node = Node(data=data)
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = node
            self.tail = node

    # inserting at the ending of the DLL
    def insert_at_end(self, data):      # time complexity O(1)
        node = Node(data=data)
        if self.tail:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        else:
            self.head, self.tail = node, node

    # inserting a set of values into DLL
    def insert_values(self, datalist):      # time complexity O(n), where n = len(datalist)
        for i in datalist:
            self.insert_at_end(i)

    # inserting at particular index
    def insert_at(self, index, data):       # time complexity O(n), where n is no.of elements in DLL
        node = Node(data=data)
        if self.head and self.length() >= index >= 0:
            i = 0
            itr = self.head
            while itr:
                if i == index - 1:
                    node.prev = itr
                    node.next = itr.next
                    itr.next.prev, itr.next = node, node
                    return
                itr = itr.next
                i += 1
        else:
            print("index out of range.")

    # return the length of the DLL
    def length(self):       # time complexity O(n), where n is no.of elements in DLL
        itr = self.head
        l = 0
        if itr:
            while itr:
                l += 1
                itr = itr.next
            return l
        else:
            return l

    # removing the recent element for DLL
    def pop(self):      # time complexity O(1)
        if self.tail:
            data = self.tail.data
            self.tail = self.tail.prev
            self.tail.next = None
            return data
        else:
            print("Double LinkedList is empty.")

    def remove_by_value(self, value):
        if self.length() > 0:
            if self.head.data == value:
                self.head = self.head.next
            else:
                itr = self.head
                prev = self.head
                c = 0
                while itr:
                    if itr.data == value:
                        if c == self.length()-1:
                            self.pop()
                        else:
                            prev.next = itr.next
                            itr.next.prev = prev
                        return
                    prev = itr
                    itr = itr.next
                    c += 1
                print("Value not found in the list.")
        else:
            print("LinkedList is empty.")

    # removes an element for the given index
    def remove_at(self, index):     # O(n), where n = index
        if self.length() > index >= 0:
            if index == 0:
                self.head = self.head.next
                self.head.prev = None
            elif index == self.length()-1:
                self.pop()
            else:
                prev = self.head
                itr = self.head
                c = 0
                while itr:
                    if c == index:
                        break
                    prev = itr
                    itr = itr.next
                    c += 1
                prev.next = itr.next
                itr.next.prev = itr.prev
        else:
            print("Invalid index received.")

    # clearing the DLL data
    def clear(self):        # time complexity O(1)
        self.head, self.tail = None, None

    # printing the elements in forward direction
    def forward_print(self):        # time complexity O(n), where n is no.of elements in DLL
        if self.head:
            dll = ""
            itr = self.head
            while itr:
                dll += str(itr.data)
                dll += " <==> "
                itr = itr.next
            print("Forward traversal : ", dll)
        else:
            print("Double LinkedList is empty.")

    # prints the elements in backward direction
    def backward_print(self):       # time complexity O(n), where n is no.of elements in DLL
        if self.tail:
            dll = ""
            itr = self.tail
            while itr:
                dll += str(itr.data)
                dll += " <==> "
                itr = itr.prev
            print("Backward traversal : ", dll)
        else:
            print("Double LinkedList is empty.")


if __name__ == "__main__":

    # -------------- TESTING MODULE ---------------------
    
    dll = DoubleLinkedList()
    print("Object created for the class.")
    print('Inserting data into dll form beginning')
    dll.insert_at_beginning(1)
    dll.insert_at_beginning(2)
    dll.insert_at_beginning(3)
    dll.forward_print()
    dll.backward_print()
    print("Inserting data for end")
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.forward_print()
    print("Inserting list of elements into data")
    dll.insert_values([5, 6, 7, 8])
    dll.forward_print()
    dll.remove_by_value(4)
    dll.remove_by_value(5)
    print("4, 5 got deleted")
    dll.forward_print()
    print(dll.pop(), " got deleted using pop()")
    print(dll.pop(), " got deleted using pop()")
    dll.forward_print()
    dll.remove_at(0)
    print("Removed elements at 0 indexes")
    dll.forward_print()
    dll.remove_at(1)
    print("Removed elements at 1 indexes")
    dll.forward_print()
    print("Length of DLL : ", dll.length())
    dll.clear()
    print("Cleared the complete data.")
    dll.forward_print()
