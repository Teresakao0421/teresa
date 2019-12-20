#!/usr/bin/env python
# coding: utf-8

# In[ ]:


List Node


# In[1]:


class ListNode:
    def __init__(self, data): 
    # store data
        self.data = data
    # store the reference (next item)
        self.next = None
        return


# In[2]:


node1 = ListNode(15)


# In[ ]:


Single linked list


# In[3]:


class SingleLinkedList:
      def __init__(self): 
        self.head = None
        self.tail = None
        return


# In[ ]:


在建立list的一開始，我們預設裡面是沒有節點的。而linked-list本身帶有head跟tail兩個屬性。
當我們加入一個新的節點時：
1.若list本身還沒有任何節點，則head以及tail都會變成新的結點。
2.若list已經包含有其他節點，則新加入的節點變成新的tail（本來的tail指向新的節點）。


# In[8]:


def add_list_item(self, item):
  # make sure item is a proper node  
    if not isinstance(item, ListNode):
        item = ListNode(item)
    if self.head is None:
        self.head = item
    else:
        self.tail.next = item

        self.tail = item
        return


# In[ ]:


其中比較需要注意的是，在取得item之後，要檢查item是否是一個結點，
若不是的話則使用ListNode(item)建立一個帶有item資料的節點。


# In[ ]:


list1 = SingleLinkedList()
list1.add_list_item(node1)
list1.add_list_item(12)


# In[ ]:


這樣子就建立一個名為list1的linked-list，裡面包含了帶有資料15以及12的節點了。


# In[ ]:





# In[ ]:




