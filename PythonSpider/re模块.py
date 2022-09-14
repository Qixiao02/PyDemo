import re

# findall匹配字符串中所有符合正则的内容
lst = re.findall('\d+', "我的电话号码是10086,第二个电话号码是10010")
# print(lst)

#finditer匹配字符串中所有内容[返回的是迭代器],从迭代器中拿到内容需要.group()
lst2 = re.finditer(r'\d+', '我的电话号码是10086,第二个电话号码是10010')
# for i in lst2:
#     print(i.group())

#search,找到一个结果就返回，返回对象是match对象,拿到内容需要.group()
lst3 = re.search(r'\d+', '我的电话号码是10086,第二个电话号码是10010')
# print(lst3.group())

#match是从头开始匹配
lst4 = re.match(r'\d+', '我的电话号码是10086,第二个电话号码是10010')
# print(lst4.group())

#预加载正则表达式
obj = re.compile(r'\d+')
ret = obj.finditer('我的电话号码是10086,第二个电话号码是10010')
# for i in ret:
#     print(i.group())

test = """
<div class='jay'><span id='1'>周杰伦</span><div>
<div class='jj'><span id='2'>林俊杰</span><div>
<div class='EasonChan'><span id='3'>陈奕迅</span><div>
<div class='EasonChan'><span id='3'>陈奕迅</span><div>
"""

# rule = re.compile(r"<div class='.*?'><span id='\d+'>.*?</span><div>", re.S)
# name1 = re.compile(r"<div class='.*?'><span id='\d+'>(?P<sss>.*?)</span><div>")
#
# list1 = name1.finditer(test)
# for i in list1:
#     print(i.group('sss'))



name = re.compile(r"<div class='(?P<classid>.*?')><span id='(?P<spanid>\d+)'>(?P<name>.*?)</span><div>", re.S)
select_name = name.finditer(test)
for i in select_name:
    print(i.group("name"))
    print(i.group("classid"))
    print(i.group("spanid"))
