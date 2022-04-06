class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
    
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
    
    def get_next(self):
        return self.next
    
    def set_next(self, value):
        self.next = value


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, value):
        node = Node(value)
        node.set_next(self.head)
        self.head = node

    def size(self):
        count = 0
        curr = self.head

        while curr != None:
            count += 1
            curr = curr.get_next()
        
        return count


if __name__ == '__main__':
    linked_list = LinkedList()
    
    for i in range(10):
        linked_list.add(i)

    print('Is empty:', linked_list.is_empty())
    print('Size:', linked_list.size())