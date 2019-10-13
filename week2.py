4.Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
def adjacentElementsProduct(inputArray):
    return max([inputArray[i]*inputArray[i+1] for i in range(len(inputArray)-1)])
    
    
    
5.Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

def shapeArea(n):
    return n*n+(n-1)*(n-1)
    
6.Ratiorg got statues of different sizes as a present from CodeMaster for his birthday, each statue having an non-negative integer size. Since he likes to make things perfect, he wants to arrange them from smallest to largest so that each statue will be bigger than the previous one exactly by 1. He may need some additional statues to be able to accomplish that. Help him figure out the minimum number of additional statues needed.

def makeArrayConsecutive2(statues):
