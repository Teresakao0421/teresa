#!/usr/bin/env python
# coding: utf-8

# In[1]:


from collections import defaultdict 
class Graph:
    
    def __init__(self): 
         
        self.graph = defaultdict(list) 

     
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    
    def BFS(self,s):#s=開始的那個點
        
        queue = []#數組
        queue.append(s)
        seen = []#看一下我們訪問了哪些節點:數組 #{}是一個集合
        seen.append(s)
        
        while len(queue) > 0:#當我這個隊列裡面有東西時
            vtx = queue.pop(0)#從隊列裡面拿出一個點
            nodes = self.graph[vtx]#找出所有臨節點
            #graph["A"]#A的臨節點
            for a in nodes:
                if a not in seen:#如果a還沒發掘過就把它放進來
                    seen.append(a)
                    queue.append(a)    
                else:
                    pass
                
        return seen
        
    
    def DFS(self,s):#s=開始的那個點
        stack = []#棧
        stack.append(s)
        
        seen = []#看一下我們訪問了哪些節點 {}是一個集合
        seen.append(s)
        
        while stack:#當我這個隊列裡面有東西時
            vtx = stack.pop()#棧的話是彈出最後一個元素
            #graph["A"]#A的臨節點
            for a in self.graph[vtx]:
                if (a not in stack) and (a not in seen):#如果w還沒發掘過就把它放進來
                    stack.append(a)
                else:
                    pass
            if vtx not in seen:
                seen.append(vtx)
            
        return seen          

