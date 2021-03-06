## Code
### [BFS&DFS](https://github.com/Teresakao0421/teresa/blob/master/HW5/BFS_06170215.py)

## Learn
### [BFS&DFS學習歷程](https://github.com/Teresakao0421/teresa/blob/master/HW5/BFS%26DFS流程圖.程式碼學習歷程與BFS.DFS原理%26比較.ipynb)

## 簡介:
DFS(Depth-First Search)深度優先搜尋:
    遞迴方式，先遇到的鄰點就先訪問。
    DFS 用於找所有解的問題，它的空間效率高，而且找到的不一定是最優解，
    必須記錄並完成整個搜尋，故一般情況下，深搜需要非常高效的剪枝。
    DFS是與遞迴深度成正比的。一般與狀態數相比，遞迴深度並不會太大，所以DFS更加省記憶體。
BFS(Breath-First Search)廣度優先搜尋:
    雖然深度優先搜尋可以搜尋整個圖形，但是卻很可能繞了很久才找到目標，
    於是從起點到目標可能會花費很久的時間 (或說路徑長度過長)。
    如果我們想找出到達目標最少的步驟，那麼就可以採用BFS。
    BFS 是從一個節點開始，將每個鄰居節點都一層一層的拜訪下去，深度最淺的節點會優先被拜訪的方式。
DFS & BFS 比較:
    DFS使用遞迴函式程式可以簡潔地進行書寫，並且狀態管理也很簡單，所以大多數情況還是用DFS來實現相關問題。
    反之，在求最短路問題時，DFS需要反覆經過同樣的狀態，所以此時使用BFS為好。
    BFS會把狀態逐個加入佇列，因此通常需要與狀態數成正比的記憶體空間。
    反之，DFS是與遞迴深度成正比的。一般與狀態數相比，遞迴深度並不會太大，所以DFS更加省記憶體。
![](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/BFS/BFS%20VS%20DFS%20.png)
