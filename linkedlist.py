#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  1 02:30:48 2022

@author: matthewray
"""

class LinkedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        return " -> ".join([str(x) for x in self])
    
    def __iter__(self): #iterate through list 
        current_node = self.head
        while current_node:
            value = current_node.value
            current_node = current_node.next
            yield value  
    
    def insert(self, where, value):
        node = Node(value)
        node.next = where
        prev = None
        next = self.head
        while next != where: 
            prev = next
            next = next.next
            if prev: prev.next = node
            else: self.head = node
            return self
        
    def remove(self,value):
        node = Node(value)
        prev = None
        next = self.head
        while next != node: 
            prev = next
            next = next.next
            if prev: prev.next = node.next
            else: self.head = node.next
            node.next = None
            return self
        
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
first_node = Node('A')
second_node = Node('B')
third_node = Node('C')
fourth_node = Node('D')

ll = LinkedList()
ll.head = first_node
first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node


print(ll)