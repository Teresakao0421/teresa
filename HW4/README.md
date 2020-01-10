## Code
### [Hash Table](https://github.com/Teresakao0421/teresa/blob/master/HW4/hash_table_06170215.py)

## Learn
### [Hash Table學習歷程](https://github.com/Teresakao0421/teresa/blob/master/HW4/hash%20table學習歷程.流程圖.Hash%20table%26Hash%20function原理.ipynb)

## Hash Table簡介:
是儲存 (key, value) 這種 mapping 關係的一種資料結構，從圖中可以很清楚地看到.
那為什麼他的時間複雜度這麼低呢? 舉例來說，如果我們有 n 個數字要儲存，一般大家常會用 array 來存。
如果我們拿到另一個數字 A，要判斷這個數字 A 有沒有在 array 裡面，那我們勢必得跟 array 裡的元素一個個比較，
時間複雜度是 O(n)。(先做過 sorting 的話，就可以用二分搜尋法比較快地找到，但還是需要 O(logn) 的時間複雜度)

但因為 hash function 的關係，如果先把 n 個數字儲存在 Hash Table 裡面，那如果要判斷這個數字 A 是不是已經被存在 Hash Table 裡面，
只要先把這個數字丟進 hash function，就可以直接知道 A 對應到 Hash Table 中哪一格。
所以其實是 hash function 幫我們省去了一個個比較的力氣。

Hash Function：
一種從任何一種資料中建立小的數字「指紋」的方法。
雜湊函式 把訊息或資料 (key) 壓縮成摘要，使得資料量變小，將資料的格式固定下來。
該函式將資料打亂混合，重新建立一個叫做 雜湊值（hash values，hash codes，hash sums，或hashes） 的指紋。
這個雜湊值就當作是陣列的索引，資料就儲存在這個索引的位置中。雜湊值通常用一個短的隨機字
![](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/hashtable/hashtable-1.png)
