#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 03:43:49 2022

@author: matthewray
"""

import os 
os.chdir ('/Users/matthewray/Desktop/Northeastern/PythonProjects/assignment08-MatthewjRay')

import unittest
from linked_list import LinkedList, Node



def test_LinkedList_instance():
    first_node = Node('A')
    second_node = Node('B')
    third_node = Node('C')
    fourth_node = Node('D')

    l_list = LinkedList()
    l_list.head = first_node
    first_node.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    return l_list

class TestLinkedList(unittest.TestCase):
    
    def test_init(self):
        l_list = test_LinkedList_instance()
        self.assertEqual(l_list.head, 'A')
        self.assertEqual(len(l_list), 1)

    def test_iter(self):
     node1 = Node("A")
     node2 = Node("B")
     node3 = Node("C")
     node4 = Node("D")

     node1.next = node2
     node2.next = node3
     node3.next = node4

     l_list = LinkedList()
     l_list.head = node1

     self.assertEqual(l_list.head, node1)
     self.assertEqual(l_list.head.next, node2)
     self.assertEqual(l_list.head.next.next, node3)
     self.assertEqual(l_list.head.next.next.next, node4)
     self.assertIsNone(l_list.head.next.next.next.next)
        
  
        
   # def test_insert(self):
    #    ll = test_linked_list_instance()
     #   ll.append_node('D')
      #  self.assertEquals(len(ll), 4)
        #self.assertEquals(ll[0], 'A')
        #self.assertEquals(ll[1], 'B')
        #self.assertEquals(ll[2], 'C')
        
   # def test_remove(self):
    #    ll = test_linked_list_instance()
     #   self.assertEqual(ll.delete_node('B'), (len(ll), 2), "Deleting 2 from [3,2,1] should return the node with value 2")
        


if __name__ == '__main__':
    unittest.main()