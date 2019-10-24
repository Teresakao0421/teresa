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
![]()

圖一(a)：黑色數字是index，藍色數字是value。

特徵二：若將位於index(i)之node視為subtree之root，那麼，可將此Binary Heap分為兩類：

#### Max Heap：在每一個subtree中，root之「數值」要比兩個child之「數值」還要大，見圖一(a)：

value(i)>value(2i)
value(i)>value(2i+1)

#### Min Heap：在每一個subtree中，root之「數值」要比兩個child之「數值」還要小，見圖一(b)：

value(i)<value(2i)
value(i)<value(2i+1)

### 圖一(b):
![]()

特別注意：在同一個subtree裡，leftchild(index(2i))與rightchild(index(2i+1))的「數值」大小順序不重要，只要和root(index(i))比較即可。
這也是Binary Heap與Binary Search Tree其中一項區別。

要滿足Binary Heap特有的「parent-child」之關係，只要讓矩陣中index(0)的位置閒置，從index(1)開始存放資料，即可使用矩陣(array)來表示Binary Heap。

接著介紹兩個函式，把任意矩陣轉換成Max Heap。
