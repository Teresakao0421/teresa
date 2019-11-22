# Binary Search Tree - Search.Insert.Delete.Modify功能介紹：
## binary search tree 原理介紹:
Binary Search Tree原理：

二叉查找樹是一種特殊的二叉樹。其樹結點的結構和普通二叉樹一樣。所不同的是，我們對二叉查找樹的建立和修改操作都需要使其始終滿足一個條件：對於樹中的每個結點X，它的左子樹中所有關鍵字值小於X的關鍵值，而它的右子樹中所有關鍵字大於X的關鍵值。

正是這個條件二叉查找樹的建立和修改操作和普通二叉樹不一樣，需要按照一定的規則。這一規則賦予二叉查找樹一些性質。

二叉查找樹具有的性質：

1、二叉查找樹具有較好的查找性質（如果構建正確的話）。

2、二叉查找樹的中序遍歷序列是正序排序。

3、最小元素在最左端。最大元素在最右端

第一種情況：root結點是葉子結點。那麼它可以直接被刪除。而不會影響其他結點。

第二種情況：root結點具有一個孩子（左或者右）。那麼把z的孩子接在z的雙親上，就不會破壞樹的性質。

第三種情況：root結點具有兩個孩子。對於這種情況，可能存在不同的處理方法。 
## Search
### 查詢/搜尋：BST的Search()操作，便是根據BST的特徵：Key(L)<Key(Current)<Key(R)，判斷Current應該往left subtree走，還是往right subtree走。


在二元搜尋樹b中查找x的過程為：

若b是空樹，則搜索失敗，否則：

若x等於b的根節點的數據域之值，則查找成功；否則：

若x小於b的根節點的數據域之值，則搜索左子樹；否則：

查找右子樹。

![Search搜尋過程](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/search-流程圖.jpg)
![Search介紹](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/search.png)
![Search介紹2](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/search1.png)

## Insert
### 新增/插入：函式InsertBST()的概念，可以視為Search()的延伸：根據BST對Key之規則，先找到將要新增之node「適合的位置」，再將欲新增的node接上BST。


向一個二元搜尋樹b中插入一個節點s的算法，過程為：

若b是空樹，則將s所指節點作為根節點插入，否則：

若s->data等於b的根節點的數據域之值，則返回，否則：

若s->data小於b的根節點的數據域之值，則把s所指節點插入到左子樹中，

否則：把s所指節點插入到右子樹中。（新插入節點總是葉子節點）

![Insert新增過程](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/insert-流程圖.jpg)
![insert介紹](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/inserttt.png)
## Delete
### 刪除/移除：要在BST上執行刪除資料(被刪除的node稱為A)，必須讓刪除A後的BST仍然維持BST的性質。因此，所有「具有指向A的pointer」之node(也就是A的parent、leftchild以及rightchild)都必須調整該pointer，使其指向新的記憶體位置。


在二叉查找樹刪去一個結點，分三種情況討論：

若*p結點為葉子結點，即PL（左子樹）和PR（右子樹）均為空樹。由於刪去葉子結點不破壞整棵樹的結構，則只需修改其雙親結點的指針即可。

若*p結點只有左子樹PL或右子樹PR，此時只要令PL或PR直接成為其雙親結點*f的左子樹（當*p是左子樹）或右子樹（當*p是右子樹）即可，作此修改也不破壞二叉查找樹的特性。

若*p結點的左子樹和右子樹均不空。在刪去*p之後，為保持其它元素之間的相對位置不變，可按中序遍歷保持有序進行調整，可以有兩種做法：其一是令*p的左子樹為*f的左/右（依*p是*f的左子樹還是右子樹而定）子樹，*s為*p左子樹的最右下的結點，而*p的右子樹為*s的右子樹；其二是令*p的直接前驅或直接後繼替代*p，然後再從二叉查找樹中刪去它的直接前驅（或直接後繼）。

![Delete刪除過程](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/delete.png)
![delete介紹](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/delete11.png)
![delete1介紹](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/delete12.png)
## Modify
### 修改/取代：將一個新的數字取代原先舊的數字，也將其舊的數字刪除。會運用到insert&delete的概念。


在這個tree當中，我想要將一個新的數字取代其中一個舊的數字，但這樣會打壞原本的BST所以我還要將被破壞的BST平衡回來。

只要符合左邊是小於或等於root，右邊是大於root即可。

![Modify修改過程](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/modify-流程圖.jpg)
![modify](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/modify1.png)

參考資料：

http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html

http://alrightchiu.github.io/SecondRound/binary-search-tree-sortpai-xu-deleteshan-chu-zi-liao.html

https://my.oschina.net/amince/blog/295618

https://blog.csdn.net/ojshilu/article/details/13766071
