# youxiue
# createTime: 2026/1/21
import time

# 学生
class Student:
  def __init__(self, name, chinese, math, english):
    self.name = name
    self.chinese = chinese
    self.math = math
    self.english = english
    
  def __str__(self):
    return "姓名：%s, 中文：%d, 数学：%d, 英语：%d" % (self.name, self.chinese, self.math, self.english)
  
  
  def update_score(self, chinese =None, math = None, english = None):
    if chinese is not None:
      self.chinese = chinese
    if math is not None:
      self.math = math
    if english is not None:
      self.english = english
      

# 教务系统
class EduManagement:
  def __init__(self):
    self.students = []
    
  def input_student(self):
    name = input("请输入学生姓名：")
    # 判断学生姓名是否存在
    if self.query_student(name) is not None:
      print("学生已存在")
      return
    chinese = int(input("请输入学生语文成绩："))
    if not self.check_score(chinese):
      print("输入的语文成绩有误")
      return
    math = int(input("请输入学生数学成绩："))
    if not self.check_score(math):
      print("输入的数学成绩有误")
      return
    english = int(input("请输入学生英语成绩："))
    if not self.check_score(english):
      print("输入的英语成绩有误")
      return
    student = Student(name, chinese, math, english)
    self.add_student(student)
    print(student)
    
  def add_student(self, student):
    self.students.append(student)
    
  def input_query_student(self):
    name = input("请输入学生姓名：")
    stu = self.query_student(name)
    if stu is None:
      print("学生不存在")
      return
    print(stu)
    
  def query_student(self, name):
    for student in self.students:
      if student.name == name:
        return student
    return None
  
  def input_update_student(self):
    name = input("请输入学生姓名：")
    stu = self.query_student(name)
    if stu is None:
      print("学生不存在")
      return
    chinese = int(input("请输入学生语文成绩："))
    if not self.check_score(chinese):
      print("输入的语文成绩有误")
      return
    math = int(input("请输入学生数学成绩："))
    if not self.check_score(math):
      print("输入的数学成绩有误")
      return
    english = int(input("请输入学生英语成绩："))
    if not self.check_score(english):
      print("输入的英语成绩有误")
      return
    stu.update_score(chinese, math, english)
    
  def update_student(self, name, chinese = None, math = None, english = None):
    student = self.query_student(name)
    student.update_score(chinese, math, english)
    print(student)
    
  def check_score(self, score):
    return 0 <= score <= 100
  
  def input_delete_student(self):
    name = input("请输入学生姓名：")
    self.delete_student(name)
    print("删除成功")

  
  def delete_student(self, name):
    for i in range(len(self.students)):
      if self.students[i].name == name:
        del self.students[i]
        return
    print("学生不存在")
  
  # 运行系统的方法
  def run(self):
    print(f"欢迎使用教务系统，当前时间：{time.time()}")
    
    while True:
      print()
      print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
      print("# 1. 添加学生  2. 查询学生  3. 修改学生 4. 删除学生 5. 查询所有学生 6. 退出系统 #")
      print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # ")
      choice = input("请输入您要执行的操作：")
      try:
        match choice:
          case "1":
            self.input_student()
          case "2":
            self.input_query_student()
          case "3":
            self.input_update_student()
          case "4":
            self.input_delete_student()
          case "5":
            for student in self.students:
              print(student)
          case "6":
            print("退出系统")
            break
          case _:
            print("输入错误")
      except ValueError as e:
        print("输入数据有误，请检查后重新输入" ,e)
      except Exception as e:
        print("程序运行出错：", e)

    
if __name__ == "__main__":
  edu = EduManagement()
  edu.run()