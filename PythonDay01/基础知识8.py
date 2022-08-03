"""类"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        #模拟小狗收到命令蹲下
        print(f"{self.name}现在坐下了。")
    def roll_over(self):
        #打滚
        print(f"{self.name}在打滚。")
my_dog = Dog('威廉姆斯', 4)
print(f"我的狗名字叫{my_dog.name}。")
print(f"我的狗已经{my_dog.age}岁。")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('吉姆', 7)
print(f"你的狗名字叫{your_dog.name}。")
print(f"你的狗已经{your_dog.age}岁。")
your_dog.roll_over()

"""car"""
class Car:
    def __init__(self, factory, year, power):
        #初始化属性
        self.factory = factory
        self.year = year
        self.power = power
        self.car_kilometers = 0

    def get_car_info(self):
        car_info = f"车商:{self.factory} 车龄:{self.year} 动力:{self.power}"
        return car_info.title()

    def get_car_kilometers(self):
        print(f"已经行驶了{self.car_kilometers}KM")

my_car = Car('bwm', '4','2.0T')
#给属性指定默认值
print(my_car.get_car_kilometers())
print(my_car.get_car_info())
#修改属性值
my_car.car_kilometers = 312
print(my_car.get_car_kilometers())