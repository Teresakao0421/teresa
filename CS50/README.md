# CS50 Learn

# Video
[2013week5](https://www.youtube.com/watch?v=IEuvKVjw2oM)

---
# 190927 Friday
> [CS502013wee5](https://www.youtube.com/watch?v=IEuvKVjw2oM)

## Notes
1. [Pointers]
2. [CGI]
3. [Debug]

### Pointers
> What does the `*` mean?  
  - `char*`: `*` 是一個指針，儲存一個實際在記憶體裡的某個地址。`char*` 表示指向記憶體內的一個字串的第一個位置。
  - `int* tmp`: 宣告一個叫做tmp的指標變數，這個變數的資料型態是int整數，存放一個地址。
  - [傳值vs傳址vs傳物件](https://e8859487.pixnet.net/blog/post/402632162-python-傳值%28pass-by-value%29-vs-傳址%28pass-by-address%29-vs-)
  
### CGI
 - CGI全名是computer-generated imagery，是由電腦生成的虛擬圖像。
 - 另一個CGI指的是common gateway interface，是一種協議，規範動態網頁請求資源的標準流程。user對網路伺服器發出request後，透過cgi協議啟動cgi程式要求資源，再回傳結果到網路伺服器，網路伺服器再返回結果呈現於瀏覽器上。
- [CGI編程](https://www.runoob.com/python/python-cgi.html)

### Debug
- help50：在發生邏輯上的衝突、導致編譯發生錯誤時使用。在下任何指令前，前面加上 help50 能夠幫助你找出錯誤的位置，或提供一些頭緒除錯。
- eprintf(“”)：比起 printf，eprintf 會提供是哪一行的資訊，更方便除錯。
- debug50：在編譯沒問題但結果不如預期，試圖找出設計上錯誤時使用，debug50 並無法直接幫你找出錯誤，畢竟電腦不知道你想要到結果是什麼，但可以幫助你更暸解程式運行的步驟，監控變數的變化，找出在哪一個環節出錯。
- [介紹簡單的Debug](http://markjong001.pixnet.net/blog/post/194793749)
