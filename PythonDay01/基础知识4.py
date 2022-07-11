magicians = ['tony', 'lili', 'steven', 'david']
for magician in magicians:
    print(magician)
for magician in magicians:
    print(f"{magician.title()},是一个优秀的魔术师")
"""
range()
"""
for i in range(1, 5):
    print(i)
print("\n")
for i in range(0, 5):
    print(i)
print("\n")
for i in range(1, 6):
    print(i)
print("\n")
for i in range(0, 6):
    print(i)
"""
使用range创建数字列表
"""
list_of_numbers = list(range(0, 10, 3))
print(list_of_numbers)
squares = []

for value in range(1, 11):
    #方法1
    # square = value ** 2
    # squares.append(square)
    #方法2
    squares.append(value ** 2)
print(squares)
"""
对列表进行简单计算
"""
num_list = []
for y in range(1, 11):
    num_list.append(y)
print(num_list)
print(min(num_list))
print(max(num_list))
print(sum(num_list))
"""
列表解析
上面的方法都包含三四段代码，实际上生成一个列表只需要一段代码就足够
"""
num_list_two = [c ** 2 for c in range(1, 11)]
print(num_list_two)

"""练习"""
#使用for循环打印1-20(包含20)
for v in range(1, 21):
    print(v)
# #创建一个包含数1-1000000的列表，再使用for打印
# a_million_list = [z for z in range(1, 1000001)]
# print(a_million_list)
#一百万求和
# print(min(a_million_list))
# print(max(a_million_list))
# print(sum(a_million_list))
#通过range指定第三个参数创建一个列表，其中包含1-20的奇数再使用for打印
oddNumber_list = [o for o in range(1, 21, 2)]
print(oddNumber_list)
#3的倍数
num_list
num_list_three = [b for b in range(3, 31, 3)]
print(num_list_three)
#立方
cube = []
for l in range(1, 11):
    cube.append(l**3)
print(cube)
"""列表解析法"""
# cube = [l**3 for l in range(1, 11)]
# print(cube)

"""
切片
要创建切片，可指定要使用的第一个元素和最后一个元素的索引。
与函数 range()一样Python在到达第二个索引之前的元素后停止。
要输出列表中的前三个元素，需要指定索引0和这将返回素引为0、1和2的元素。
"""
players = ['twy', 'lkj', 'dsa', 'plk', 'xck']
print(players[0:3])
print(players[:4])
print(players[2:])
"""遍历切片"""
for player in players[:3]:
    print(player.title())
"""复制列表"""
one_players = players[:]
two_players = players[1:4]
print(one_players)
print(two_players)
"""元组"""
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#遍历元组
for dimension in dimensions:
    print(dimension)
print("\n")
#修改元组变量
"""虽然不能修改元组的元素但是可以给储存元组的变量赋值"""
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)