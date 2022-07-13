"""函数"""
def one_and_one():
    i = input('输入数字')
    i = int(i)
    i += 1
    print(i)
one_and_one()
"""形参和实参"""
def user_name(name):
    print(f"{name},你好！")
user_name('twy')
"""在定义方法中(name)是形参,而twy是实参"""
def pets(AnimalType,name):
    print(f"宠物的类型是:{AnimalType}")
    print(f"宠物的名字是:{name}")
pets('dog','黄智浩')