# youxiue
# createTime: 2026/1/21

'''
自定义了一些功能, 被 模块.py 引用

'''

# 可以通过 __all__ 来指定模块中被导出的功能 , 默认导出所有功能
__all__ = ["p", "circle_perimeter", "circle_area"]


p = 3.14159265358979323846

# 计算圆的周长
def circle_perimeter(r):
    return 2 * p * r
  
# 计算圆的面积
def circle_area(r):
    return p * r * r

# 计算圆柱体的体积
def cylinder_volume(r, h):
    return circle_area(r) * h
  
def name():
  print("模块名: " + __name__)
  
name() # 模块名: __main__  在当前文件运行时, __name__ 为 __main__,  被其他模块引用时, __name__ 为文件名(不含.py后缀)