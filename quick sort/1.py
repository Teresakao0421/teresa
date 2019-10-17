def quicksort(nums):
      if len(nums) < 2: #如果這個數列的長度小於2
          return nums。#則不用排序所以把他丟回去
      else:
          pivot = nums[0]#將基準點放在每個數列的第一個
          less = [i for i in nums[1:] if i <= pivot] #告訴這個迴圈如果從第二個位置以後開始跑，如果小於基準點就放在左邊
          more = [i for i in nums[1:] if i > pivot] #告訴這個迴圈如果從第二個位置以後開始跑，如果大於基準點就放在右邊
          return quicksort(less) +[pivot]+ quicksort(more) #重新定義 把三個合併就完成了！
Teresa=[10,7,8,1,3]
quicksort(Teresa)
>>>[1,3,7,8,10]
