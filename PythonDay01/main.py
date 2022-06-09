def print_hi(name):
    print(f'Hi, {name}')

def test():
    a = 10
    b = 3
    a += b
    a *= a + 2
    return a
def Π ():
    Π = 3.1415926535
    return Π

def Square(num):#平方
    return num**2

def Round(r): #圆的面积
    S = Π() * (r**2)
    return S

def Round_CIR(r):
    C = 2 * Π() * r
    return C

def Leap_Year(year):
    if year % 4 == 0 and year % 100 != 0:
        print("此年是闰年")
    else:
        print("此年不是闰年")

if __name__ == '__main__':
    # print_hi('谭文彦')
    # print(test())
    # print(Square(5))
    print("%.2f" % Round(float(input("这是一个求圆面积的方法,请输入圆的半径:"))))
    print("%.2f" % Round_CIR(float(input("这是一个求圆周长的方法，请输入圆的半径:"))))

    # Leap_Year(int(input("请输入年份:")))
