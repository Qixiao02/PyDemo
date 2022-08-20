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
    def __init__(self, factory, day, carmodel):
        #初始化属性
        self.factory = factory
        self.day = day
        self.carmodel = carmodel
        self.fill_gas_tank = 35
        self.car_kilometers = 0
    def get_car_info(self):
        car_info = f"车商:{self.factory} 车龄:{self.day}天 车型:{self.carmodel} 油箱容量:{self.fill_gas_tank}L 已行驶里程数:{self.car_kilometers}KM"
        return car_info.title()

    def auto_add_car_kilometers(self, car_kilometers):
        self.car_kilometers += car_kilometers

    def updata_car_kilometers(self, new_car_kilometers):
        #防止回调
        if new_car_kilometers <= self.car_kilometers:
            print(f"你不能把里程数进行回调！")
        else:
            self.car_kilometers = new_car_kilometers

    def car_fill_gas_tank(self, fill_gas_tanks):
        self.fill_gas_tank = fill_gas_tanks

my_car = Car('bwm', '756', 'Small Family Car')
#给属性指定默认值
# print(my_car.get_car_kilometers())
# print(my_car.get_car_info())
#修改属性值
# my_car.car_kilometers = 312
#通过方法修改属性值
my_car.updata_car_kilometers(43679)
my_car.car_fill_gas_tank(35)
# my_car.updata_car_kilometers(-2)
# my_car.auto_add_car_kilometers(200)
print(my_car.get_car_info())

#自增
my_new_car = Car('RollsRoyce', '3', 'Small Family Car')
my_new_car.updata_car_kilometers(8)
my_new_car.auto_add_car_kilometers(6)
my_new_car.car_fill_gas_tank(40)
print(my_new_car.get_car_info())

"类继承"
class Electriccar(Car):
    def __init__(self, factory, day, carmodel):
        #初始化父类的属性
        super().__init__(factory, day, carmodel)
        self.battery_size = 75
    def electric_car_battery(self):
        print(f"这辆电车的电池容量还剩余:{self.battery_size}kwh")
    def car_fill_gas_tank(self, fill_gas_tanks):
        fill_gas_tanks = f'这是辆电车！'
my_electric_car = Electriccar('tesla', '247','Small Family Car')
my_electric_car.updata_car_kilometers(16352)
my_electric_car.auto_add_car_kilometers(13)
my_electric_car.car_fill_gas_tank(38)
print(my_electric_car.get_car_info())
my_electric_car.electric_car_battery()

