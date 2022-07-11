"""
练习7-4:比萨配料编写一个循环，提示用户输入一系列比萨配料，并在用户输入'quit'时结束循环。
每当用户输入一种配料后，都打印一条消息，指出我们会在比萨中添加这种配料。
"""
pizza_ingredients_list = ['1.egg', '2.ham', '3.pork chop', '4.onion']
user_pizza_ingredients_list = []
while pizza_ingredients_list:
    print(f"我们现在有这些配料可选择:{pizza_ingredients_list},输入5退出选择")
    i = input("请输入编号加入配料:")
    i = int(i)
    if i == 1:
        user_pizza_ingredients_list.append('egg')
    elif i == 2:
        user_pizza_ingredients_list.append('ham')
    elif i == 3:
        user_pizza_ingredients_list.append('pork chop')
    elif i == 4:
        user_pizza_ingredients_list.append('onion')
    elif i == 5:
        break
    else:
        print("没有此配料,请重新选择")
        continue
    print(f"你现在已经加入了这些配料:{user_pizza_ingredients_list}")
"""
练习 7-5：电影票有家电影院根据观众的年龄收取不同的票价：
不到3岁的观众免费；3～12岁的观众收费 10 美元；
超过 12 岁的观众收费 15美元。
请编写一个循环,在其中询问用户的年龄，并指出其票价。
"""

"""
练习 7-6：三种出路以不同的方式完成练习7-4或练习7-5,在程序中采取如下做法。
在while 循环中使用条件测试来结束循环。

使用变量 active 来控制循环结束的时机。

使用 break 语句在用户输入'quit'时退出循环。
"""
"""练习 7-7：无限循环编写一个没完没了的循环，并运行它（要结束该循环，可按Ctrl+C，也可关闭显示输出的窗口)。"""