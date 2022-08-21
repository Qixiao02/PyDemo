list_1 = ['twy', 'jack', 'lrj', 'hbq']
print(list_1)
print(list_1[0])
print(list_1[1])
print(list_1[2].title())
print(list_1[3].upper())
print(list_1[-2].upper())
Friends = f"my bester friends is .title(), {list_1[2].title()}"
print(Friends)
My_OldPhone = ['xiaomi 6', 'redmi 2s', 'redmi note 3', 'redmi K20', 'redmi k30', 'redmi k40']
print(My_OldPhone)
xiaomi_6 = f'{My_OldPhone[0].title()} 晓龙835处理器,6+128'
print(xiaomi_6)
#修改 添加删除列表元素
#append ([]) 后面加多一个括号是将多个元素看作成一个整体输出结果为：
# ['sony xperia 2', 'meizu 16thp', 'samsung s10']
#当然,如果希望不将被追加的列表或元组当成一个整体，而是只追加列表中的元素，则可使用列表提供的 extend() 方法.
# My_OldPhone.append(['sony xperia 2', 'meizu 16thp', 'samsung s10'])
My_OldPhone.extend(['sony xperia 2', 'meizu 16thp', 'samsung s10'])
print(My_OldPhone)
#insert 插入
My_OldPhone.insert(0, 'huawei honer ')
My_OldPhone.insert(-1, 'iphone 5s')
print(My_OldPhone)
"""
删除
del 可以删除任意位置
pop 删除后的元素 可以接着使用
remove 不知道要删除的元素下标可但知道值。可以使用remove 删除后同样可以接着使用被删除的值
remove只能删除第一个特定的值 多个删除得使用循环
"""
japanese_manga = ['鬼灭之刃', '一拳超人', '进击的巨人', '刀剑神域', '偷星九月天', '中国惊奇先生', '星辰变']
print(japanese_manga)
"""del"""
del japanese_manga[-1]
print(japanese_manga)

"""pop"""
japanese_manga_pop = japanese_manga.pop()
print(japanese_manga)
print("pop删除的值："+japanese_manga_pop)

"""remove"""
japanese_manga_remove = "偷星九月天"
japanese_manga.remove(japanese_manga_remove)
print(japanese_manga)
print("remove删除的值：" + japanese_manga_remove)

"""补充"""
list1 = ['a', 'b', 'c', 'd']
str2 = ['a', 'b', 'c', 'd']
list1
['a', 'b', 'c', 'd']
# 解决方法一：
# 使用join()
print(' '.join(list1))

list1 = ['a', 'b', 'c', 'd']
str = '-'
print(str.join(list1))
# 解决方法二：
# 如果list存放的是数字，则：将其转为int即可，原来存放的是string型。
# for i in str2:
#     int(i)
# print(i)

# 如果想同行输出在使用print时，添加end = ‘ ’即可（末尾不换行，加空格）。
for i in str2:
    print(int(i), end=' ')



