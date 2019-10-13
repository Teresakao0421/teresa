def quicksort(nums):
      if len(nums) < 2:
          return nums
      else:
          pivot = nums[0]
          less = [i for i in nums[1:] if i <= pivot]
          more = [i for i in nums[1:] if i > pivot]
          return quicksort(less) +[pivot]+ quicksort(more) 

Teresa=[10,7,8,1,3]
quicksort(Teresa)
>>>[1,3,7,8,10]
