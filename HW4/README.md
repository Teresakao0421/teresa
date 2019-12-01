# Hash Table:
## 是儲存 (key, value) 這種 mapping 關係的一種資料結構，從圖中可以很清楚地看到.
#### 那為什麼他的時間複雜度這麼低呢? 舉例來說，如果我們有 n 個數字要儲存，一般大家常會用 array 來存。如果我們拿到另一個數字 A，要判斷這個數字 A 有沒有在 array 裡面，那我們勢必得跟 array 裡的元素一個個比較，時間複雜度是 O(n)。(先做過 sorting 的話，就可以用二分搜尋法比較快地找到，但還是需要 O(logn) 的時間複雜度)
#### 但因為 hash function 的關係，如果先把 n 個數字儲存在 Hash Table 裡面，那如果要判斷這個數字 A 是不是已經被存在 Hash Table 裡面，只要先把這個數字丟進 hash function，就可以直接知道 A 對應到 Hash Table 中哪一格。所以其實是 hash function 幫我們省去了一個個比較的力氣。
!()[]

### 缺點：
#### 想要處理一些有時間順序的 data，希望可以丟掉最先進來的資料優先，queue 顯然就是一個更好的選擇。還有一個情況是，如果希望儲存的 data 可以被排序，那 Hash Table 就會不太好用。

### Collision(碰撞):
#### Collision就是兩筆資料存進同一個Table之slot的情形，這將會使得查詢資料失敗(例如：使用item1的Key，卻回傳item2的資料)。若以Division Method實作Hash Function，定義h(Key)=Keymodm，Table大小為m=6，目前要處理的資料之Key有67,26,50,33,16,71，那麼各個Key將被對應到的index.

### collision解決方法:
#### 1.Chaining：使用Linked list把「Hashing到同一個slot」的資料串起來。
#### 2.Open Addressing：使用Probing Method來尋找Table中「空的slot」存放資料。
!()[]

### 應用：
#### Hash Table 的一個簡單應用就是搜尋引擎，在搜尋的時候輸入關鍵字，我們可以把這個關鍵字傳進 hash function，然後 hash function 就可以指出這個關鍵字對應到的桶子，這時候再到這個桶子裡搜尋網頁就可以了。

## Add:
### 1.hash table 的增量大小
### 2.使用hash function 計算鍵的索引
### 3.如果索引處的存儲桶為空。請創建一個新節點
### 4.否則，發生衝突：此索引處已經存在至少一個節點的鏈接列表。重複列表並在其中添加新節點

## Contains:
### 1.使用hash function 計算提供的鍵的索引
### 2.轉到該索引的存儲桶
### 3.重複該鏈接列表中的節點，直到找到密鑰或到達列表末尾為止
### 4.返回找到的節點的值，如果找不到則返回None

## Remove:
### 1.計算hash 以確定index的key
### 2.重複喜歡的節點列表。繼續直到列表末尾或找到密鑰為止。
### 3.如果找不到密鑰，請return None
### 4.否則，從鍊錶中刪除節點並返回節點值

# Hash Function：
## Hash Table 好不好用的關鍵跟這個神奇的 hash function 有很大的關係。讓我們想像一種情況，如果我們使用一個壞掉的 hash function，不管餵給這個 hash function 什麼內容他都會吐出同一個 index，那這樣的話就跟存一個 array 沒什麼兩樣。 搜尋的時間複雜度就會變成 O(n)。以實用的角度出發，在簡單認識 Hash Table 的時候並不需要理解 hash function 要怎麼實作，但是我們要知道，hash function沒有完美的，有可能會把兩個不同的 key 指到同一個桶子，這就是所謂的 collision。當 collision 發生的時候，除了最直觀地增加 Hash Table 的桶子數，在每個桶子中用一個 linked list 來儲存 value、或是 linear probe 都是常用的方法。

##### 參考資料:https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/






