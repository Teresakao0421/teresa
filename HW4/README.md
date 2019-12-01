# Hash Table:
## 是儲存 (key, value) 這種 mapping 關係的一種資料結構，從圖中可以很清楚地看到.
### 那為什麼他的時間複雜度這麼低呢? 舉例來說，如果我們有 n 個數字要儲存，一般大家常會用 array 來存。如果我們拿到另一個數字 A，要判斷這個數字 A 有沒有在 array 裡面，那我們勢必得跟 array 裡的元素一個個比較，時間複雜度是 O(n)。(先做過 sorting 的話，就可以用二分搜尋法比較快地找到，但還是需要 O(logn) 的時間複雜度)
但因為 hash function 的關係，如果先把 n 個數字儲存在 Hash Table 裡面，那如果要判斷這個數字 A 是不是已經被存在 Hash Table 裡面，只要先把這個數字丟進 hash function，就可以直接知道 A 對應到 Hash Table 中哪一格。所以其實是 hash function 幫我們省去了一個個比較的力氣。

## 缺點：
### 想要處理一些有時間順序的 data，希望可以丟掉最先進來的資料優先，queue 顯然就是一個更好的選擇。還有一個情況是，如果希望儲存的 data 可以被排序，那 Hash Table 就會不太好用。
