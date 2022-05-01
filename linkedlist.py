#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 02:30:48 2022

@author: matthewray
"""

class LinkedList:
    def init(self):
        self.head = None
        nodes = []
        for node in nodes:
            list.append(node)
   
    def __init__(self):
        self.head = None
         
    
    def insert(self, value, where = None):
    #------ Check if value for 'insert' is empty. if yes: create new list. if not: proceed with regular insert -------#
        if where == None:
            node  = Node(value)
            self.head = node
            return self
        else:
            node = Node(value)
            if self.head == where: #do we want to insert before head of list?
                self.head = node
                next = self.head
                next.next = where
                return self
            prev = None
            next = self.head
            while next != where: 
                prev = next
                next = next.next
                if next == where:
                    prev.next = node
                    node.next = where
            return self

    def remove(self, node):
        next = self.head
        prev = None
        while next:
            if next.value == node:
                if not prev:
                    self.head = self.head.next
                else:
                    prev.next = next.next
                break
            else:
                prev = next
                next = next.next
                
        return
        
    def printLL(self):
        current = self.head
        while(current):
            print(current.value)
            current = current.next
        
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

ll = LinkedList()
ll.head = a
a.next = b
b.next = c
c.next = d

ll.insert('P',b)

ll.remove('P')


ll.printLL()