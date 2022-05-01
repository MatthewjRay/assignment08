#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 03:43:49 2022

@author: matthewray
"""

import unittest
from linkedlist import LinkedList, Node



def test_LinkedList_instance():
   a = Node('A')
   b = Node('B')
   c = Node('C')
   d = Node('D')

   ll = LinkedList()
   ll.head = a
   a.next = b
   b.next = c
   c.next = d

   return ll

class TestLinkedList(unittest.TestCase):
    
    #def test_iter(self):
	#	x = test_LList_instance()
	#	self.assertEquals([xi for xi in x], [1.11, 2.22, 3.33])

    def test_insert_first(self):
        linked_list, inpt = self.make_five_elements_linked_list()
        linked_list.insert("Hello", 0)
        self.assertEqual(linked_list.to_list(), ["Hello"] + inpt)
        self.assertEqual(linked_list.size(), len(inpt) + 1)

    def test_insert_last(self):
        linked_list, inpt = self.make_five_elements_linked_list()
        linked_list.insert("Hello", len(inpt))
        self.assertEqual(linked_list.to_list(), inpt + ["Hello"])
        self.assertEqual(linked_list.size(), len(inpt) + 1)

    def test_insert_middle(self):
        linked_list, inpt = self.make_five_elements_linked_list()
        index_to_insert = 2
        linked_list.insert("Hello", index_to_insert)
        self.assertEqual(linked_list.to_list(), inpt[:index_to_insert] + ["Hello"] + inpt[index_to_insert:])
        self.assertEqual(linked_list.size(), len(inpt) + 1)



     def test_insert(self):
        ll = test_LinkedList_instance()
        ll.insert('D', 'c')
        self.assertEquals(len(ll), 4)
        self.assertEquals(ll[0], 'A')
        self.assertEquals(ll[1], 'B')
        self.assertEquals(ll[2], 'C')
        
     def test_remove(self):
        ll = test_LinkedList_instance()
         self.assertEqual(ll.delete_node('B'), (len(ll), 2), "Deleting 2 from [3,2,1] should return the node with value 2")
        


if __name__ == '__main__':
    unittest.main()