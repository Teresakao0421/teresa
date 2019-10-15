Given the string, check if it is a palindrome.
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
