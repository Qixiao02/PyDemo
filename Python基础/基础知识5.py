"""
字典
"""
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
"""
添加键值对
字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可依次指定字典名、用方括号括起的键和相关联的值。
"""
alien_0['x_position'] = 0
alien_0['y_position'] = 0
print(alien_0)
"""
修改键值对
"""
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = '20'
print(alien_1)
alien_1 = {'color': 'red'}
print(alien_1['color'])
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"原来的 x_position:{alien_2['x_position']}")
"""删除键值对"""
print(alien_0)
del alien_0['points']
print(alien_0)
"""
6.2.6由类似对象组成的字典
在前面的示例中，字典存储的是一个对象（游戏中的一个外星人）的多种信息，但你也1使用字典来存储众多对象的同一种信息。
例如，假设你要调查很多人，询问他们最喜欢的编言，可使用一个字典来存储这种简单调查的结果。
"""
favorite_language = {
    'twy': 'python',
    'cby': 'c',
    'hzh': 'java',
    'hlh': 'c++',
}
language =favorite_language['twy'].title()
print(f"twy最喜欢的语言是:{language}")
print(favorite_language['hzh'])
"""使用get()方法访问值"""
#如果访问的字典有键但没有值则系统会显示traceback keyError
#如何方法无值的键
alien_3 = {'color': 'green', 'speed': 'slow', 'points': 7}
point_value = alien_3.get('points', "这个键没有值")
print(point_value)
"""如果这个键有值则打印值"""
"""如果指点的键可能没有值则使用get()方法"""
alien_3 = {'color': 'green', 'speed': 'slow', }
point_value = alien_3.get('points', "这个键没有值")
print(point_value)
"""遍历键值对"""
user_0 = {
    'username': 'zyj',
    'frist': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nkey:{key}")
    print(f"Value:{value}")
print("\n")
"""遍历字典中所有键与值"""
for name in favorite_language.keys():
    print(name.title())
print("\n")
for value in favorite_language.values():
    print(value.title())
print("\n")
"""按照特定顺序遍历字典中的所有键"""
for name in sorted(favorite_language.keys()):
    print(f"{name.title()},认为你参加了投票")
"""按照特定顺序遍历字典中的所有值"""
print("\n")
for value in sorted(favorite_language.values()):
    print(f"{value.title()},是一种编程语言")
print("\n")
"""set()方法找出列表中独一无二的元素，并用这些元素来创建一个集合"""
for language in set(favorite_language.values()):
    print(language.title())
print("\n")
languages = {'python', 'c', 'java'}
print(languages)
"""练习项目"""
river = {
    'nile': 'egypt',
    'yellow river': 'china',
    'mississippi river': 'America'
}
"""6-5"""
for key, value in river.items():
    print(f"{key.title()},流经{value.title()}")
for river, nation in river.items():
    print(f"键:{river.title()}")
    print(f"值:{nation.title()}")
print("\n")
"""6.4嵌套"""
#创建30个绿色外星人
aliens = []
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#显示前五
for alien in aliens[:5]:
    print(alien)
#查看一共有多少个外星人
print(f"一共有{len(aliens)}个外星人")
print("\n")
"""使用for循环与if,elif修改外星人信息"""
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'
for alien in aliens[:5]:
    print(f"新的外星人信息:{alien}")
"""在字典中存储列表"""
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}
print(f'你点了一个{pizza["crust"]}- crust pizza')