def Triangle():
    global a
    global b
    global c
    a = float(input("输入第一条边长:\n"))
    b = float(input("输入第二条边长:\n"))
    c = float(input("输入第三条边长:\n"))
    if a+b > c and a+c > b and c+a > b and b+c > a:
        print("您输入的三条边的长度构成三角形,三条边长度分别为:%.3f,%.3f,%.3f" % (a, b, c))
        C = a + b + c
        P = C / 2
        S = (P * (P - a) * (P - b) * (P - c)) ** 0.5
        print("请选择要计算的方法:\n\t1.计算周长\n\t2.计算面积\n")
        x = int(input())
        if x == 1:
            print("这个三角形周长为:" + "%f" % (C))
        elif x == 2:
            print("这个三角形面积为:" + "%f" % (S))
        else:
            print("您输入的选项无效！请出现选择")
    else:
        print("您输入的三条边的长度无法构成三角形！")

Triangle()