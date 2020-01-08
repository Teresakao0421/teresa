#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def countAndSay(self, n):
        def readString(s):
            curr, next = 0, 1
            res = ''
            while next < len(s):
                count = 1
                while next < len(s) and s[curr] == s[next]:
                    count += 1
                    next += 1
                res += str(count) + s[curr]
                curr = next
                next += 1
            if curr == len(s) - 1:
                res += '1' + s[curr]                
            return res                
                    
            
        known = {1: '1', 2: '11'}
        if n in known:
            return known[n]
        for i in range(3, n+1):
            known[i] = readString(known[i-1])
        return known[n]

