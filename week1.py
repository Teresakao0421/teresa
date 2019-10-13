 1.Write a function that returns the sum of two numbers:

def add(param1, param2):
    return param1+param2
param1=1
param2=2
add(param1, param2)

#基本的加法運算
# def-定義
# return-重新定義
# int{int(number)直接設定成整數，int(string,base)可以任意更換base進位計算十進位的相對值>>>int(10.23)>>>10
      

2.Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

def centuryFromYear(year):
    return int((year-1) / 100) + 1
#將年份轉成西元年
    

3.Given the string, check if it is a palindrome.
def checkPalindrome(inputString):
    a=inputString[::-1]#
    if(inputString==a):
        return True
    else:
        return False
#給定字符串，檢查他是否為回文
#palindrome 回文：順數及倒數都一樣的詞句
#adjacentElementsProduct:找出數列中相乘最大值
#len(a) a的長度
