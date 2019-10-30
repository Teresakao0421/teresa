# HEAP SORT 介紹:
## 前言:Sorting(排序)是基本的資料處理，舉例來說，進入圖書館的查詢系統，不論是想按照「出版日期」或是「相關程度」找書，都會得到「排序過」的結果。
## Binary Heap(二元堆積)

Binary Heap有兩項基本特徵：
特徵一：Binary Heap之結構可以視作Complete Binary Tree。

如圖一(a)，數值1~9，一共有9個元素，按照Complete Binary Tree之順序規則，填滿位置1~9，以index(1)~index(9)表示。
這樣的優點是方便尋找「parent-child」之關係，以index(i)的node為例：
其left child必定位在index(2i)；
其right child必定位在index(2i+1)；
其parent必定位在index([i/2])。
以圖一(a)中位於index(3)之node(8)為例：
其left child為index(6)之node(2)；
其right child為index(7)之node(3)；
其parent為index(1)之node(9)。
### 圖一(a):
![](https://github.com/Teresakao0421/teresa/blob/master/heap%20sort/圖片/圖1(a).png)

圖一(a)：黑色數字是index，藍色數字是value。

特徵二：若將位於index(i)之node視為subtree之root，那麼，可將此Binary Heap分為兩類：

#### Max Heap：在每一個subtree中，root之「數值」要比兩個child之「數值」還要大，見圖一(a)：

value(i)>value(2i)
value(i)>value(2i+1)

#### Min Heap：在每一個subtree中，root之「數值」要比兩個child之「數值」還要小，見圖一(b)：

value(i)<value(2i)
value(i)<value(2i+1)

### 圖一(b):
![](https://github.com/Teresakao0421/teresa/blob/master/heap%20sort/圖片/圖1(b).png)

特別注意：在同一個subtree裡，leftchild(index(2i))與rightchild(index(2i+1))的「數值」大小順序不重要，只要和root(index(i))比較即可。
這也是Binary Heap與Binary Search Tree其中一項區別。

要滿足Binary Heap特有的「parent-child」之關係，只要讓矩陣中index(0)的位置閒置，從index(1)開始存放資料，即可使用矩陣(array)來表示Binary Heap。

接著介紹兩個函式，把任意矩陣轉換成Max Heap。

經過BuildMaxHeap()之後，便能將任意矩陣調整成Max Heap。

## 那麼要如何將此Max Heap做排序呢？

Max Heap的特徵是「第一個node具有最大值」，如果要將資料「由小到大」排序，步驟如下：

### 1.把「第一個node」和「最後一個node」互換位置。
### 2.假裝heap的「最後一個node」從此消失不見。
### 3.對「第一個node」進行MaxHeapify()。
### 4.重複以上步驟，從heap的最後一個node開始，一路往上，直到root，便能得到排好序的矩陣。

以圖四(a)的Max Heap為例，現要將其調整成「由小到大」排好序的矩陣。
![](https://github.com/Teresakao0421/teresa/blob/master/heap%20sort/圖片/圖四.png)

首先，從「最後一個位置」開始，將index(9)的node與index(1)的node互換位置，見圖四(b)。
![](https://github.com/Teresakao0421/teresa/blob/master/heap%20sort/圖片/圖四Ｂ.png)
如此，便把「最大值」的node(9)給放到最後一個位置，以及「不是最大值」的node(1)換到第一個位置。

# 最重要的概念就是「假裝最後一個node消失不見」：

因為此時，heap的「最後一個node」一定是「最大值」的node，也就表示，如果要得到「由小到大」的排序，那麼，此時便已經完成「最大值node」的調整。
同時，目前的index(1)的node一定不是「最大值」，所以要利用MaxHeapify()重新調整「矩陣」，使其符合Max Heap規則。

又因為「假裝最後一個node消失不見」，所以，接下來要調整的「矩陣」，是「忽略index(9)」的矩陣，因此只要考慮由「index(1)~index(8)」所形成的矩陣即可。

圖四(c)中的size，即表示MaxHeapify()要處理的矩陣之size。
此次的MaxHeapify()將會碰到subtree(index(1)-index(2)-index(3))與subtree(index(3)-index(6)-index(7))。
![](https://github.com/Teresakao0421/teresa/blob/master/heap%20sort/圖片/圖四Ｃ.png)

經過圖四(c)的MaxHeapify()調整，由「index(1)~index(8)」形成的矩陣，又再次滿足Max Heap，見圖四(d)。
![](https://github.com/Teresakao0421/teresa/blob/master/heap%20sort/圖片/圖四Ｄ.png)

接著，再繼續重複上述步驟：

交換「目前考慮的矩陣」的「最後一個位置node」與「第一個node，以MaxHeapify()調整「目前考慮的矩陣」。
便能得到「由小到大」排好序的矩陣，見圖四(e)。
![](https://github.com/Teresakao0421/teresa/blob/master/heap%20sort/圖片/圖四Ｅ.png)
