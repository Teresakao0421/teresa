# Binary Tree
二元樹(Binary tree)是資料結構中樹狀結構的一種，也是常使用的一種資料結構，很多其他的樹種也是基於二元樹發展出來，所以是很重要的一種資料結構。
定義：
- 每個節點最多有兩個子節點。
- 子節點有左右之分。
![](https://github.com/Teresakao0421/teresa/blob/master/code/code%20image/bt.png)


## [Code](https://github.com/Teresakao0421/teresa/blob/master/code/Binary%20Tree.py)

# Red Black Tree
BST的進階版Red Black Tree(RBT，紅黑樹)，RBT其實也是BST(滿足Key(L)<Key(Current)<Key(R))，不過RBT的node比BST多加了「顏色」(紅色或黑色)，而正因為多了「顏色」，便能修正BST有可能退化成Linked list的潛在缺陷。
![](https://github.com/Teresakao0421/teresa/blob/master/code/code%20image/rb.png)

## [Code](https://github.com/Teresakao0421/teresa/blob/master/code/RedBlackTree.py)

# Set Mismatch
先使用Hash Table解題，第一遍遍歷dict[數字]=次數，第二遍遍歷找1~n的數字出現的次數是2和0的即可。
先排序，再遍歷一次。
nums只存在1~n之間的數，那-1就可以作為下標。
遍歷數n時把abs(n)作為下標，nums[n]取反，重複的下標會發現之前已經變負，缺失的下標。
## [Code](https://github.com/Teresakao0421/teresa/blob/master/code/Set%20Mismatch.py)

# Insertion sort
插入排序法(Insertion Sort)是排序演算法的一種，他是一種簡單容易理解的排序演算法，其概念是利用另一個數列來存放已排序部分，逐一取出未排序數列中元素，從已排序數列由後往前找到適當的位置插入。

- 從未排序數列取出一元素。
- 由後往前和已排序數列元素比較，直到遇到不大於自己的元素並插入此元素之後；若都沒有則插入在最前面。
- 重複以上動作直到未排序數列全部處理完成。

![](https://github.com/Teresakao0421/teresa/blob/master/code/code%20image/in.png)
## [Code](https://github.com/Teresakao0421/teresa/blob/master/code/insertionSort.py)
