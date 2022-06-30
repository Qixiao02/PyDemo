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
print(My_OldPhone)
#删除
del My_OldPhone[0]
print(My_OldPhone)
