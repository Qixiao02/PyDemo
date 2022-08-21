"""
比较运算符和逻辑运算符的使用
"""

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not(1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False

#保留小数方法1
x = 1.2342121
print(round(x, 4))
#保留小数方法2
print("%.2f" % x)


#Exercise
#华氏温度转摄氏温度
#公式C = (F - 32 ) /1.8
def Temperature ():
    f = float(input("请输入华氏温度:"))
    # C = round((f - 32) / 1.8, 2)
    C = (f - 32) / 1.8
    return C

print("%.2f" % Temperature())
