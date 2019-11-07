
# coding: utf-8

# In[1]:


class Solution(object):
    def heap_sort(self, nums):
        self.build_heap(nums)  # 建立一個堆
        i = len(nums) - 1  # 補上i=len(nums)-1&i>=0
        for i in range(i, 0, -1):  # i從最後一個節點出發所以是n-1，一直到第0個節點
            nums[0], nums[i] = nums[i], nums[0]  # 一樣做一個根結點跟後節點交換的動作，交換完畢砍斷再做一次heapify
            self.heapify(nums, i, 0)  # 由於原本的節點是由n來決定，但到後面其實節點數是不斷在減少的，所以其實是由i(剩下的節點數量)去主導。

        return nums

    def build_heap(self, nums):
        n = len(nums)
        last_node = n - 1
        parent = (n - 1 - 1) // 2  # 這棵樹最後一個節點，然後求他的parent #向下取整數法
        for parent in range(parent, -1, -1):  # parent從這個節點出發！開始往回跑！
            self.heapify(nums, n, parent)  # 這邊就不用改成parent了

    def heapify(self, nums, n, i):
        if i >= n:  # i一定要小於n，這是一個出口必須定義。
            return nums

        c1 = 2 * i + 1
        c2 = 2 * i + 2
        max = i

        if c1 < n and nums[c1] > nums[max]:  # c1<n是為了保證c1不會出界
            max = c1
        if c2 < n and nums[c2] > nums[max]:  # c2<n是為了保證c2不會出界
            max = c2
            # 這段就可以找到最大值
        if max != i:  # 如果max不等於i的話要進行交換順序
            nums[max], nums[i] = nums[i], nums[max]  # 交換順序#由n改成max才對
            self.heapify(nums, n, max)  # 這邊應該改成n節點，max代表操作的index。剛剛寫反很離譜！

