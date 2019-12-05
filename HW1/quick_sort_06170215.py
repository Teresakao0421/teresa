#!/usr/bin/env python
# coding: utf-8

# In[1]:


def quicksort(list):
    left=[]
    middle=[]
    right=[]
    #list=left + middle + right
    pivot = list[0]#第一個位置為基準點

    if len(list) <2 :
        pass
    else:
        for i in list:
            if i < pivot:
                left.append(i)
            elif i > pivot:
                right.append(i)
            elif i == pivot:
                middle.append(i)

    if len(left) > 1:
        left = quicksort(left)
    else:
        pass
    if len(right) > 1:
        right = quicksort(right)
    else:
        pass

    return left + middle + right

