#猜素数
import random
answer = random.randint(1, 101)
num = 0
while True:
    num += 1
    number = int(input('请输入:'))
    if number < answer:
        print('大一点')
    elif number > answer:
        print('小一点')
    else:
        print('猜对了')
        break
print("你一共猜了%d次" % num)
if num > 7:
    print('你的智商余额明显不足')
