"""
练习3-8：放眼世界想出至少5个你涡望去旅游的地方
1.将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的
2.按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python 列表
3.使用 sorted()按字母顺序打印这个列表，同时不要修改它。再次打印该列表，核实排列顺序未变。
4.使用 sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它。再次打印该列表，核实排列顺序未变。
5.使用 reverse()修政列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
6使用 reverse()再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
7.使用 sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
"""
#1
World = ['shanghai', "beijing", 'nanjing', 'hangzhou', 'jiangmen']
#2
print(World)
#3
print(sorted(World))
print(World)
#4
print(sorted(World, reverse=True))
print(World)
#5
World.reverse()
print(World)
#6
World.reverse()
print(World)
#7
World.sort()
print(World)


