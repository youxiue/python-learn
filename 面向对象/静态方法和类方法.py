class Triangle(object):
  def __init__(self, a, b, c):
    self.a = a
    self.b = b
    self.c = c
  
  # 静态方法
  @staticmethod
  def is_valid(a, b, c):
    return a + b > c and b + c > a and a + c > b  
  
  # 类方法 , 第一个参数必须是cls
  @classmethod
  def is_equilateral(cls, a, b, c):
    return a == b == c

  def perimeter(self):
    return self.a + self.b + self.c
  
  def area(self):
    p = self.perimeter() / 2
    return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5
  

# 调用静态方法
print(Triangle.is_valid(3, 4, 5))


t = Triangle(3, 4, 5)
print(t.perimeter())
print(t.area())
print(t.is_valid(3, 4, 5))

# 调用类方法
print(Triangle.is_equilateral(3, 3, 3))
print(t.is_equilateral(3, 3, 3))
