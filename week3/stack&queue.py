#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Stack:

    def __init__(self):
        self.stack = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)
    
    def pop(self) -> None:
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
    
    def IsEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def getSize(self):
        return len(self.stack)


# In[2]:


s = Stack()
s.push(5)
s.push(4)
s.pop()
print(s.top())
print(s.IsEmpty())
print(s.getSize())


# In[3]:


class Queue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(0)
        
    def getFront(self) -> int:
        return self.stack[0]
    
    def getBack(self):
        return self.stack[-1]
        
    def IsEmpty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def getSize(self):
        return len(self.stack)


# In[4]:


q = Queue()
q.push(5)
q.push(6)
q.push(4)
q.pop()
print(q.getFront())
print(q.getBack())
print(q.IsEmpty())
print(q.getSize())


# In[ ]:




