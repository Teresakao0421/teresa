# CS50 Learn
CS50（Introduction to Computer Science）是一堂美國哈佛大學自 1989 年開始教授的計算機概論課，即使在網路科技起飛的 2002 年，走在時代尖端的哈佛大學選修這堂課的人數一樣慘兮兮，低於 100 人。但是現在修課人數卻高達800人！CS50 課程為期十二週，一週上課兩次，一次一小時。上課內容從最基本的二進位、ASCII、演算法、偽代碼、C 語言語法及應用、排序法、哈希表等，到 TCP/IP、HTTP、HTML、CSS、PHP、SQL、JavaScript、Ajax，一直到網路安全性（Cybersecurity）；不但將電腦科學裡最重要的基礎都帶了一次，還會結合歷史和新聞時事來講授，對初學者來說，內容是滿有分量的。
現在以 818 名大學部學生選修的驚人數字，成為常春藤聯盟大學裡最受歡迎的選修課，其原因有二：

1.趨勢所致：電腦科學可以說是現在最夯的學科，畢業後工作穩定、薪水高。
2.授課教授 David Malan 跟他強大的 TA 軍團。

最重要的是：CS50將資源開放給全世界，只要上youtube就能找到高清版學習影片那我還不快把握學習！！
- [超過800人選修,魅力何在？](https://www.inside.com.tw/article/4209-harvard-cs50)

## Web
[About CS50](http://cs50.tv/2013/fall/#about,lectures)

---
## 190927 Friday
> [CS502013wee5](https://www.youtube.com/watch?v=IEuvKVjw2oM)

### Notes
1. [Pointers]
2. [CGI]
3. [Debug]

#### Pointers
> What does the `*` mean?  
  - `char*`: `*` 是一個指針，儲存一個實際在記憶體裡的某個地址。`char*` 表示指向記憶體內的一個字串的第一個位置。
  - `int* tmp`: 宣告一個叫做tmp的指標變數，這個變數的資料型態是int整數，存放一個地址。
  - [傳值vs傳址vs傳物件](https://e8859487.pixnet.net/blog/post/402632162-python-傳值%28pass-by-value%29-vs-傳址%28pass-by-address%29-vs-)
  
#### CGI
 - CGI全名是computer-generated imagery，是由電腦生成的虛擬圖像。
 - 另一個CGI指的是common gateway interface，是一種協議，規範動態網頁請求資源的標準流程。user對網路伺服器發出request後，透過cgi協議啟動cgi程式要求資源，再回傳結果到網路伺服器，網路伺服器再返回結果呈現於瀏覽器上。
- [CGI編程](https://www.runoob.com/python/python-cgi.html)

#### Debug
- help50：在發生邏輯上的衝突、導致編譯發生錯誤時使用。在下任何指令前，前面加上 help50 能夠幫助你找出錯誤的位置，或提供一些頭緒除錯。
- eprintf(“”)：比起 printf，eprintf 會提供是哪一行的資訊，更方便除錯。
- debug50：在編譯沒問題但結果不如預期，試圖找出設計上錯誤時使用，debug50 並無法直接幫你找出錯誤，畢竟電腦不知道你想要到結果是什麼，但可以幫助你更暸解程式運行的步驟，監控變數的變化，找出在哪一個環節出錯。
- [介紹簡單的Debug](http://markjong001.pixnet.net/blog/post/194793749)

###### Reference
- https://e8859487.pixnet.net/blog/post/402632162-python-傳值%28pass-by-value%29-vs-傳址%28pass-by-address%29-vs-
- https://www.runoob.com/python/python-cgi.html
- http://markjong001.pixnet.net/blog/post/194793749
- https://blog.kdchang.cc/2016/10/30/python101-tutorial/
- https://www.inside.com.tw/article/4209-harvard-cs50
