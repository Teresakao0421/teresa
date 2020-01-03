#!/usr/bin/env python
# coding: utf-8

# In[3]:


import sys
from collections import defaultdict   
class Graph(): 
  
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.graph_dict = defaultdict(list)
        self.weight = {} 
        self.pair = [] 
        self.list = []
        self.set = [] 
        
    def addEdge(self,u,v,w): 
        self.graph.append([u,v,w])
  
    def printS(self, d): 
        print("Dijkstra{",end = '')
        for node in range(self.V): 
            print ("\'",node,"\'",":",d[node],',',end = "")
        print("\b","}")
  
    def mini(self, d, shortarr): 
  
        min = float("inf") 
        for v in range(self.V): 
            if d[v] < min and shortarr[v] == False: 
                min = d[v] 
                min_index = v 
        return min_index 

    def Dijkstra(self, s): 
  
        d = [float("inf")] * self.V
        d[s] = 0
        shortarr = [False] * self.V 
        for cout in range(self.V): 
            u = self.mini(d, shortarr) 
            shortarr[u] = True
            
            for v in range(self.V): 
                if self.graph[u][v] > 0 and shortarr[v] == False and d[v] > d[u] + self.graph[u][v]: 
                    d[v] = d[u] + self.graph[u][v] 

        result = {}
        for i in range(self.V):
            result[str(i)] = d[i]

        return result
    def transform(self, MST):
        temp_MST = {}
        for k in range(len(MST.keys())):
            key1 = list(MST.keys())[k][0]
            key2 = list(MST.keys())[k][1]
            value = list(MST.values())[k][0]

            if key1 <= key2:
                temp_MST.setdefault(str(key1)+'-'+str(key2), value)
            else:
                temp_MST.setdefault(str(key2)+'-'+str(key1), value)

        MST = temp_MST
        return MST

    def find_index(self, node):
        for set_index in range(len(self.set)):
            if node in self.set[set_index]:
                return set_index
    
    def sortset(self, u, v):
        temp_list = sorted(zip(self.graph_dict.values(), self.graph_dict.keys()))
        temp_list_2 = []
        
        for items in temp_list:
            temp_list_2.append(list(items))
        
        for edges in range(len(temp_list_2)):  
            key = temp_list_2[edges][1]
            value = temp_list_2[edges][0]
            self.weight.setdefault(key, value)
        
        return self.weight

    def addEdge(self, u, v, w): 
        self.graph_dict[u,v].append(w)        
        self.pair.append([u,v])
        if u not in self.list:
            self.list.append(u)
            self.set.append([u])
        if v not in self.list:
            self.list.append(v)
            self.set.append([v])
    def Kruskal(self):
        MST = {}
        for node in range(len(self.pair)):
            self.weight = self.sortset(self.pair[node][0], self.pair[node][1])
        
        for edge in range(len(list(self.weight.keys()))):
            node1 = list(self.weight.keys())[edge][0]
            node2 = list(self.weight.keys())[edge][1]

            node1_setidx = self.find_index(node1)
            node2_setidx = self.find_index(node2)
            
            len_node1_set = len(self.set[node1_setidx])
            len_node2_set = len(self.set[node2_setidx])           
            if len_node1_set >= len_node2_set:
                if node2 not in self.set[node1_setidx]:
                    self.set[node1_setidx] += self.set[node2_setidx]
                    self.set[node2_setidx] = []
                    MST.setdefault(list(self.weight.keys())[edge], list(self.weight.values())[edge])
            else:
                if node1 not in self.set[node2_setidx]:
                    self.set[node2_setidx] += self.set[node1_setidx]
                    self.set[node1_setidx] = []
                    MST.setdefault(list(self.weight.keys())[edge], list(self.weight.values())[edge])                    
        Kruskal_dict = self.transform(MST)
        return Kruskal_dict


# In[ ]:




