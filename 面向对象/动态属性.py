class Student:
  # 限制动态属性添加
  __slots__ = ("name", "age")
  def __init__(self, name, age):
    self.name = name
    self.age = age
    

stu = Student("小王", 18)

# 添加一个动态属性
stu.sex = "男"
print(stu.__dict__) # {'name': '小王', 'age': 18, 'sex': '男'}

