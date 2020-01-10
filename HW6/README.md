## Code
### [Dijkstra&Kruskal](https://github.com/Teresakao0421/teresa/blob/master/HW6/Dijkstra_06170215.py)

## Learn
### [Dijkstra&Kruskal學習歷程](https://github.com/Teresakao0421/teresa/blob/master/HW6/Dijkstra與Kruskal流程圖%20程式碼學習歷程與Dijkstra與Kruskal原理說明.ipynb)

## Dijkstra&Kruskal:
Dijkstra's algorithm:
戴克斯特拉算法使用了廣度優先搜尋解決賦權有向圖的單源最短路徑問題。
該演算法存在很多變體；戴克斯特拉的原始版本找到兩個頂點之間的最短路徑，
但是更常見的變體固定了一個頂點作為源節點然後找到該頂點到圖中所有其它節點的最短路徑，
產生一個最短路徑樹。

最壞空間複雜度:O(|E|+|V|log|V|)

Kruskal's algorithm:
Kruskal演算法是一種用來尋找最小生成樹的演算法,
在圖中存在相同權值的邊時也有效。
是以增加邊的觀念做為出發點。
首先將所有的邊，依照權重的大小排序。
再來依序加入權重最小的邊，如果 造成cycle時，則必須捨棄，直到增加了n - 1條邊為止。
(假設有 n 個節點)

平均時間複雜度:O(|E|log|V|)
最壞空間複雜度:Ω(|E|+|V|)
