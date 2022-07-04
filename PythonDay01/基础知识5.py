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
alien_2 ={'x_position': 0, 'y_position': 25, 'speed': 'medium'}
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
    'cby': 'C',
    'hzh': 'html',
}
language =favorite_language['twy'].title()
print(f"twy最喜欢的语言是:{language}")
print(favorite_language['hzh'])
"""使用get()方法访问值"""