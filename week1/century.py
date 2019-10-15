Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

def centuryFromYear(year): #定義
    return int((year-1) / 100) + 1 #重新定義
#將年份轉成西元年
