"""
sort()方法
对列表永久排序
"""
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)
"""反向"""
# cars.sort(reverse=True)
# print(cars)
"""
sorted()方法
临时排序
"""
print(cars)
print(sorted(cars))
print(cars)

"""
reverse()
不是按字母排序而且直接反转列表
永久修改但可随时修改恢复原来的排序。
"""
cars.reverse()
print(cars)
print(len(cars))