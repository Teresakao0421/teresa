#!/usr/bin/env python
# coding: utf-8

# In[3]:


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
            #print('success!'+str(index))

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
                #print('success! link'+str(index))

            else:
                return
        
    def remove(self, key):
        
        if self.contains(key) == True:
            
            h = MD5.new()
            h.update(key.encode('utf-8'))
            key = int(h.hexdigest(), 16)
            index = key % self.capacity

            ptr = self.data[index]

            if ptr != None:
                if ptr.val == key:
                    self.data[index] = ptr.next
                    ptr = None
                    return
                
            while ptr != None:
                if ptr.val == key:
                    break
                prev = ptr
                ptr = ptr.next
                
            prev.next = ptr.next
            ptr = None
        
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

