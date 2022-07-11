# """方法1"""
# age = int(input("你多少岁？"))
# if age >= 18:
#     print("你已经成年")
# else:
#     print("你还没成年")
# """方法2"""
# age = input("你多少岁？")
# age = int(age)
# if age >= 18:
#     print("你已经成年")
# else:
#     print("你还没成年")
#
# t1 = "\n请输入信息"
# t1 += "\n输入'quit' 退出。"
# ms = ""
# while ms != 'quit':
#     ms = input(t1)
#     if ms != 'quit':
#         print(ms)
# print("\n")
# """
# 优化
# 因为不需要在其中做任何比较——相关的逻辑由程序的其他部分处理。只要变量 active 为True,循环就将继续运行
# 将变量 active 设置为 True，让程序最初处于活动状态。这样做简化了while 语句
# """
# active = True
# while active:
#     ms1 = input(t1)
#     if ms1 == 'quit':
#         active = False
#     else:
#         print(ms1)
# """break"""
# while active:
#     ms1 = input(t1)
#     if ms1 == 'quit':
#         break
#     else:
#         print(ms1)
"""continue"""
#使用continue返回循环开头
i = 0
while i < 10:
    i = input("请输入数字")
    i = int(i)
    if i == 1:
        i += 1
        print(i)
        break
    else:
        continue
"""while循环字典和列表"""
#假设有一个列表包含新注册但还未验证的网站用户。
# 验证这些用户后，如何将他们移到另一个已验证用户列表中呢？
# 一种办法是使用一个while循环，在验证用户的同时将其从未验证用户列表中提取出来，再将其加入另一个已验证用户列表中。代码可能类似于下面这样：
"""
首先，创建一个待验证用户列表
和一个用于存储已验证用户的空列表。
"""
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []
"""
验证每个用户直到没有未验证用户为止。
将每个经过验证的用户都移到已验证用户列表中。
"""
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"验证用户：{current_user.title()}")
    confirmed_users.append(current_user)
