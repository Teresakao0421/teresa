#!/usr/bin/env python
# coding: utf-8

# In[19]:


from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.data = [None] * capacity

    def add(self, key):

        h = MD5.new()
        h.update(key.encode('utf-8'))
        key = int(h.hexdigest(), 16)
        index = key % self.capacity

        new_node = ListNode(key)
        new_node.next = None

        data = self.data

        if data[index] == None:
            data[index] = new_node

        elif data[index] != None:
            ptr = data[index]
            try:
                while (ptr.val != key):
                    ptr = ptr.next
            except:
                pass

            if ptr == None:
                new_node.next = data[index]
                data[index] = new_node

            else:
                return

    def remove(self, key):
        def delete(ptr):

            if ptr.val != key:
                return delete(ptr.next)

            elif ptr.val == key:

                if ptr.next == None:
                    ptr = None

            elif ptr.next != None:
                ptr = ptr.next

            return ptr

        if self.contains(key) == True:

            h = MD5.new()
            h.update(key.encode('utf-8'))
            key = int(h.hexdigest(), 16)
            index = key % self.capacity

            ptr = self.data[index]        
            self.data[index] = delete(ptr)
        else:
            pass
        
    def contains(self, key):

        h = MD5.new()
        h.update(key.encode('utf-8'))
        key = int(h.hexdigest(), 16)
        index = key % self.capacity

        ptr = self.data[index]
        try:
            while (ptr.val != key):
                ptr = ptr.next
        except:
            pass

        if ptr == None:
            return False

        elif ptr.val == key:
            return True

