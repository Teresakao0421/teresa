#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def findErrorNums(self, nums):
        dict1 = {}
        result = []
        for i in range(len(nums)):
            if nums[i] not in dict1:dict1[nums[i]] = nums[i]
            else:result.append(nums[i])
        for i in range(len(nums)):
            if i + 1 not in dict1:result.append(i+1)
        return result

