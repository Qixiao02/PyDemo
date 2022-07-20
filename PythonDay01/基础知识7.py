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
pets(name="黄智浩", AnimalType='cat')
print("\n")

"""等效的函数调用"""
def Animal(Animal_name, Animal_Type="dog"):
    print(Animal_name, Animal_Type)
Animal('ccc')
Animal('bbb', 'cat')
print("\n")

"""返回值"""
def language(name,language):
    return name, language
A = language('twy','python')
print(A)
print("\n")

"""让实参变成可选择的"""
def get_user_name(frist_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{frist_name} {middle_name} {last_name}"
    else:
        full_name = f"{frist_name} {last_name}"
    return full_name.title()
nba_star = get_user_name('kobe','bryant')
print(nba_star)
nba_star = get_user_name('wardell', 'curry', 'stephen')
print(nba_star)

"""返回字典"""
def buil_person(frist_name, last_name, middle_name= ''):
    if middle_name:
        full_name = {'frist_name': frist_name, 'middle_name': middle_name, 'last_name': last_name,}
    else:
        full_name = {'frist_name': frist_name, 'last_name': last_name}
    return full_name
B = buil_person('wardell', 'curry', 'stephen')
C = buil_person('kevin', 'durant', 'wayne')
print(B)
print(C)

"""传递列表并修改列表"""
import threading
import time
def models_3D():
    models_list = ['cat', 'mouse', 'tiger', "lion"]
    models = models_list
    user_select_models = []
    finish_models = []
    while models:
        print(f"可以打印这些模型")
        for i in models_list:
            print(i, end=" ")
        models = input(f"\n请输入要打印的模型,输入yes开始打印。\n")
        if models == "cat":
            user_select_models.append("cat")
            print(f"您选择打印的模型:{user_select_models}")
        if models == "mouse":
            user_select_models.append("mouse")
            print(f"您选择打印的模型:{user_select_models}")
        if models == "tiger":
            user_select_models.append("tiger")
            print(f"您选择打印的模型:{user_select_models}")
        if models == "lion":
            user_select_models.append("lion")
            print(f"您选择打印的模型:{user_select_models}")
        if models == "yes":
            printing_models = user_select_models
            while printing_models:
                printing_model = printing_models.pop()
                print(f"{printing_model}打印中....")
                time.sleep(3)
                finish_models.append(printing_model)
                print(f"{finish_models}打印完成！")
            print("已经打印好所有模型！")
            # print(printing_models)
            break
            # for finish_model in finish_models:
            #     print(finish_model)
# models_3D()
"""传递任意数量的实参"""
def user_name(*name):
    print(name)
user_name('twy', 'hzh', 'hlh', 'cby')
"""结合使用位置实参和任意数量实参"""
def size_pizza(size,*pizzas):
    print(f"{size}寸的披萨订单有:")
    for pizza in pizzas:
        print(f"- {pizza}")
size_pizza(17, 'htc', 'ljb')
size_pizza(10, 'sad', 'vc')
"""使用任意数量的关键字实参"""
# **user_info中的两个星号是创建一共名为user——info的空字典，并将所有接收到的名称值对都放进这个字典中
def build_profile(frist, last, **user_info):
    user_info['frist_name'] = frist
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('kobe','bryant',
                             location='princeton',
                             field='physics')
print(user_profile)