from math import (pi, tau, inf, e)

import unittest


class DuplicateError(Exception):

    def __init__(self):
        self.message = "Error adding Item, duplicate item"
        super().__init__(self.message)


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

    def __str__(self):
        return 'Node(value={value},next={next_value})'\
            .format(value=self.value, next_value=self.next)


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, value):

        if self.search(value):
             raise DuplicateError

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

    def search(self, value):
        curr = self.head
        
        while curr != None:
            if curr.get_value() == value:
                return curr
            else: 
                curr = curr.get_next()
    
        return None

    def remove(self, value):
        curr = self.head
        prev = None
        
        search_item = self.search(value)

        prev = search_item
        curr = search_item.get_next()
        
        if prev == None:
            self.head = curr.get_next()
        else:
            prev.set_next(curr.get_next())


class TestNodeMethods(unittest.TestCase):
    
    def setUp(self):
        self.node = Node(round(31.4 / 10, 2))
        
    def test_get_value(self):
        self.assertEqual(self.node.get_value(), round(pi, 2))
    
    def test_set_value(self):
        self.node.set_value(tau)
        self.assertEqual(self.node.get_value(), tau)
    
    def test_get_next_value_none(self):
        self.assertIsNone(self.node.get_next())
    
    def test_set_next_value(self):
        new_node = Node(e)
        self.node.set_next(new_node)
        self.assertEqual(self.node.get_next(), new_node)

    
class TestLinkedListMethods(unittest.TestCase):
    
    def setUp(self):
        self.linked_list = LinkedList()
    
    def test_is_empty_true(self):
        self.assertTrue(self.linked_list.is_empty())
    
    def test_is_empty_false(self):
        for i in range(2):
            self.linked_list.add(i)
        self.assertFalse(self.linked_list.is_empty())


if __name__ == '__main__':
    unittest.main()