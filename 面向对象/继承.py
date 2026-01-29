class Animal:
  def __init__(self, name):
    self.name = name
  def eat(self):
    print("吃吃吃")
  def drink(self):
    print("喝喝喝")
  def sleep(self):
    print("睡觉")
  def run(self):
    print("跑跑跑")
    

class Dog(Animal):
  def __init__(self, name, color):
    super().__init__(name)
    self.color = color
  def eat(self):
    print("汪汪吃吃吃")
  def bark(self):
    print("汪汪汪")
    
class XiaoTianQuan(Dog):
  def __init__(self, name, color):
    super().__init__(name, color)
  def fly(self):
    print("飞飞飞")
    
  def bark(self):
    # 调用父类的方法
    # super().bark()

    # 另一种调用父类方法的方式
    Dog.bark(self)
    print("我还会说人话")

xtq= XiaoTianQuan("哮天犬", "黑色")
xtq.fly()
xtq.bark()
xtq.eat()

class Robot:
  def charge(self):
    print("充电")
    
  def drink(self):
    print("喝机油")

# 多继承
class Cyberpunk(Robot, Animal ):
  def __init__(self, name):
    super().__init__(name)
  
    
    
c = Cyberpunk("赛博机器人阿宾")
c.run()
c.charge()
c.drink() # Animal 中有drink()方法, Robot也有drink()方法 , 调用哪个和继承顺序有关系
# !!! 如果在多继承的情况下发现父类中的方法有重名, 应该尽量避免使用多继承

# 可以使用 __mro__ 查看继承顺序
print(Cyberpunk.__mro__)