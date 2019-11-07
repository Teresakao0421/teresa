
# coding: utf-8

# In[1]:


class Solution(object):
    sequence = []
    
    def merge_sequence(self,begin,middle,end):
        left = self.sequence[begin:middle]
        right = self.sequence[middle:end]
        b = begin #整個sequence的首位
        l = 0 #左邊的首位
        r = 0 #右邊的首位
        while (begin + l < middle and middle + r < end):#以下可參考我的流程圖，有圖示說明
            if (left[l] < right[r]):
                self.sequence[b] = left[l]
                l = l + 1
            else:
                self.sequence[b] = right[r]
                r = r + 1
            b = b + 1
       
    
        if begin + l < middle:
            while b < end:
                self.sequence[b] = left[l]
                l = l + 1
                b = b + 1
        else:
            while b < end:
                self.sequence[b] = right[r]
                r = r + 1
                b = b + 1 
                
    def merge_sort_sub(self, begin, end):
         #從開始到結尾進行排序
        if end - begin > 1:#！！一開始沒想到這這點： 一個數列 應該要符合 end-begin 代表這個數列是向右增加的 而不是向左A[0]A[-1]A[-2]這樣
            middle = (begin + end)//2
            self.merge_sort_sub(begin, middle) #一個一個分開假設，對我來說會比較清楚，因為接下來的觀念就是這樣分開來看
            self.merge_sort_sub(middle, end)
            self.merge_sequence(begin, middle, end) #這是最終版
        print(self.sequence)
                
    def merge_sort(self,nums):
        self.sequence = nums
        self.merge_sort_sub(0, len(self.sequence))
        return self.sequence
        

