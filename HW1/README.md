# Homework 10/18
## What is quick sort?
Quick Sort是一種「把大問題分成小問題處理」的Divide and Conquer方法，概念如下：

在數列中任意挑選一個數，稱為pivot，然後調整數列，使得「所有在pivot左邊的數，都比pivot還小」，而「在pivot右邊的數都比pivot大」。
接著，將所有在pivot左邊的數視為「新的數列」，所有在pivot右邊的數視為「另一個新的數列」，「分別」重複上述步驟(選pivot、調整數列)，直到分不出「新的數列」為止。

![](https://github.com/Teresakao0421/teresa/blob/master/quick%20sort/images/quick.png)
## Quick sort的概念圖：
![](https://github.com/Teresakao0421/teresa/blob/master/quick%20sort/images/概念圖.jpg)
## 流程圖：
![](https://github.com/Teresakao0421/teresa/blob/master/quick%20sort/images/第一個圖.jpg)

但是如果把基準點放在中間的話
[]裡面的位置要隨著數列長度做更改

上網搜尋解決辦法後，發現把基準點放在[0]
第一個位置上就沒有這個問題了。

![](https://github.com/Teresakao0421/teresa/blob/master/quick%20sort/images/第二個圖.jpg)

發現這樣左邊的數列並沒有按照大小排列，所以應該還要繼續找尋基準點。

![](https://github.com/Teresakao0421/teresa/blob/master/quick%20sort/images/第三張圖.jpg)


這樣問題就解決拉～～！
