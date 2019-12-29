#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:
    # Linked-list預設屬性
    def __init__(self):
        self.head = Node(-1) # linked-list開頭先設置一個虛node，後面才能啟用Node的Attribute
        self.length = 0
    
    # 查詢
    def get(self, index):
        if index >= self.length or index < 0:
            return -1
        else:
            current = self.head
            for i in range(index):
                current = current.next
            return current.val
    
    # 新增開頭
    def addAtHead(self, val):
        addhead = Node(val)
        if self.length == 0: # linked-list開頭有設置虛Node，要以length為判斷依據
            self.head = addhead
            addhead.next = None
        
        else:
            addhead.next = self.head
            self.head = addhead
        self.length += 1
        
    # 新增結尾
    def addAtTail(self, val):
        addtail = Node(val)
        if self.length == 0: # 等於是加在開頭
            self.head = addtail
            addtail.next = None
        else:
            current = self.head
            for i in range(self.length - 1): # current為目前linked-list的最後一個
                current = current.next
            current.next = addtail
        self.length += 1
    
    # 在linked-list的某一個位置新增Node
    def addAtIndex(self, index, val):
        if index > self.length:
            pass

        elif self.length >= 1 and index == self.length:
            self.addAtTail(val)
            
        elif index <= 0:
            self.addAtHead(val)
            
        else:
            addindex = Node(val)
            current = self.head
            for i in range(index - 1):
                current = current.next
            addindex.next = current.next
            current.next = addindex
            self.length += 1

    # 刪除某一Node
    def deleteAtIndex(self, index):
        if index >= self.length or index < 0:
            pass
        
        elif self.length >= 2 and index == self.length - 1:
            current = self.head
            for i in range(self.length - 2):
                current = current.next
            current.next = None
            self.length -= 1
            
        elif index == 0:
            if self.length == 1:
                self.head = None
            else:
                current = self.head
                self.head = current.next
            self.length -= 1
            
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            current.next = current.next.next
            self.length -= 1


# In[ ]:




