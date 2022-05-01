#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 03:43:49 2022

@author: matthewray
"""

import unittest
from linkedlist import LinkedList, Node

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

ll = LinkedList()
ll.head = a
a.next = b
b.next = c
c.next = d


class TestLList(unittest.TestCase):
  def test_init(self):
        a = Node('A')
        b = Node('B')
        c = Node('C')
        d = Node('D')

        ll = LinkedList()
        ll.head = a
        a.next = b
        b.next = c
        c.next = d
        
        self.assertEqual(ll.head,a)
        self.assertEqual(ll.head.next,b)
        self.assertEqual(ll.head.next.next,c)
        self.assertEqual(ll.head.next.next.next,d)
        self.assertIsNone(ll.head.next.next.next.next)
        
  def test_iter(self):
        a = Node('A')
        b = Node('B')
        c = Node('C')
        d = Node('D')

        ll = LinkedList()
        ll.head = a
        a.next = b
        b.next = c
        c.next = d
        
        self.assertEquals([lli for lli in ll], ['A', 'B', 'C', 'D'])

  def test_len(self):
        a = Node('A')
        b = Node('B')
        c = Node('C')
        d = Node('D')

        ll = LinkedList()
        ll.head = a
        a.next = b
        b.next = c
        c.next = d
        self.assertEquals(len(ll), 4)

  
  def test_insert(self):
    ll.insert('D', c)
    self.assertEqual(len(ll), 5)
    self.assertEqual(ll.getNum(2), 'D')


  def test_insert_empty(self):
    x = LinkedList()
    x.insert(a)
    self.assertEqual(len(x), 1)
    self.assertEqual(x.head.value.value, 'A')

  def test_insert_head(self):
    ll.insert('FIRST', a)
    self.assertEqual(ll.head.value, 'FIRST')

  def test_insert_tail(self):
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    ll = LinkedList()
    ll.head = a
    a.next = b
    b.next = c
    c.next = d
    ll.insert('d')

    self.assertEqual(ll.getNum(4), 'd')

  def test_remove(self):
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    ll = LinkedList()
    ll.head = a
    a.next = b
    b.next = c
    c.next = d

    ll.remove('B')
    self.assertEqual(len(ll), 3)
    self.assertEqual(ll.head.next.value, 'C')

  def test_remove_head(self):
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    ll = LinkedList()
    ll.head = a
    a.next = b
    b.next = c
    c.next = d

    ll.remove('A')
    self.assertEqual(len(ll), 3)
    self.assertEqual(ll.head.value, 'B')

  def test_remove_tail(self):
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    ll = LinkedList()
    ll.head = a
    a.next = b
    b.next = c
    c.next = d

    ll.remove('D')
    self.assertEqual(len(ll), 3)
    self.assertEqual(ll.getNum(2), 'C')


if __name__ == '__main__':
    unittest.main()

