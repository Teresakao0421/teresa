Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
def adjacentElementsProduct(inputArray):
    return max([inputArray[i]*inputArray[i+1] for i in range(len(inputArray)-1)])
    
#給定整數數組，找到具有最大乘積的相鄰元素對並返回該乘積。
#range(1,5)代表從1到5(不包含５)>>[1,2,3,4]
#range(1,5,2)代表從1到5(間隔2)>>[1,3]不包含5
    
