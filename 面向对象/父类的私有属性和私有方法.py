class Parent:
  def __init__(self):
    self.num_1 = 1
    self.__num_2 = 2
  
  def __test(self):
    print(f"私有属性与公有属性的值: {self.num_1}, {self.__num_2}")
    
  def test(self):
    self.__test()
    
  
    
class Child(Parent):
  pass

child = Child()
print(child.num_1)
# print(child.__num_2) # 报错, 访问不了父类的私有属性
# child.__test() # 报错, 访问不了父类的私有方法
child.test() # 子类可以通过父类中的公有方法间接访问父类的私有属性和私有方法
 