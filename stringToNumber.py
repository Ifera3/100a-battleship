#!python3

def toNum(num):
    if type(num) == str or type(num) == int or type(num) == float:
        num = str(num)
        if num.isdigit:
            if num.find('.') == -1:
                num = int(num)
            else:
                num = float(num)
    return num