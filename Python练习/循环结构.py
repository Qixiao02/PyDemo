#for in循环
#求1-100偶数之和
num = 0
for x in range(2, 101, 2): #(开区间,闭区间,步长)
    num += x
print(num)
#求1-100奇数之和
num2 = 0
for y in range(1, 101, 2):
    num2 +=y
print(num2)