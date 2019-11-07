# Binary Tree
## 最廣義的樹(Tree)對於樹上的node之child數目沒有限制，因此，每個node可以有多個child。
![](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/binarytree%20-1.png)
## 若限制node只能有兩個child，等價於「樹上的每一個node之degree皆為2」，此即稱為Binary Tree(二元樹)，並稱兩個child pointer為left child和right child。
![](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/binarytree%20-2.png)
# Full & Complete Binary Tree
## 一棵Full Binary Tree(或稱作Perfect Binary Tree)具有以下性質：
### 1.所有internal node都有兩個subtree(也就是兩個child pointer)
### 2.所有leaf node具有相同的level(或相同的height)。所以，若一棵Full Binary Tree的leaf node之level為n，整棵樹共有2n−1個node。例如，若leaf node的level為4，整棵樹共有15個node。並且，每個node與其child有以下關係：第i個node的left child之index為 2i；第i個node的right child之index為 2i+1；除了root之parent為NULL之外，第i個node的parent之index為 [i2⌋。

![](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/binarytree%20-3.png)
## Complete Binary Tree:

### 若一棵樹的node按照Full Binary Tree的次序排列(由上至下，由左至右)，則稱此樹為Complete Binary Tree。以下這棵樹共有10個node，且這十個node正好填滿Full Binary Tree的前十個位置，則此樹為Complete Binary Tree。
![](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/binarytree%20-4.png)

### 以下這顆樹共有11個node，但是第11個node(K)應該要是第5個node(E)的child，因此，此樹並非Complete Binary Tree。
![](https://github.com/Teresakao0421/teresa/blob/master/binary%20tree/binary%20tree/binarytree%20-5.png)
