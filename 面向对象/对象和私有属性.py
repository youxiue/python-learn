class Student:
  # 类属性
  school_name = "自学成才"
  
  
  # 初始化方法
  def __init__(self, name, age, salary):
    # 实例属性
    self.name = name
    self.age = age
    # 私有属性, 通过属性前面加__ 进行标识
    self.__salary = salary
  
  # 通过@property 获取私有属性
  @property
  def salary(self):
    return self.__salary
  
  # 修改私有属性
  @salary.setter
  def salary(self, value):
    self.__salary = value or 0
    
  def study(self, course_name):
    print("{}正在学习{}".format(self.name, course_name))
    
  def play(self):
    print("{}正在玩".format(self.name))
  
  def show_salary(self):
    print("{}的工资是{}".format(self.name, self.__salary))

# Student.play('李四', 28) # 报错 未实例化, Student.play() missing 1 required positional argument: 'self'
# Student('李四', 28).play()

# 实例化对象
# stu1 = Student('张三',18)
# print(id(stu1))
# stu1.study("python")

stu2 = Student('张三',18, 1000)
stu2.show_salary()
print(stu2.name)
# print(stu2.__salary)# 报错, 因为__标识的是私有属性,只能内部访问
print(stu2._Student__salary) # 1000  可以通过实例._类名__属性名 去获取
print(stu2.salary)
stu2.salary = 2000
print(stu2.salary)

# 类可以直接调用类属性, 但是不能调用实例属性
print(Student.school_name)
# print(Student.name)
print(stu2.school_name)