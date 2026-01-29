# youxiue
# createTime: 2026/1/15

'''
函数

定义： 
def 函数名(参数列表):
    函数体
    
调用：
函数名(参数列表)
'''

def add(a, b):
    return a + b
  
print(add(1, 2))

'''
形参： 函数定义时，需要准备的参数
    1. 位置参数，按照位置一个个的声明变量
    2. 默认值参数，函数声明的时候给变量一个默认值，如果实参不传递信息，则使用默认值
    3. 动态传参
        *args, 表示接收所有位置参数的动态传参
        **kwargs, 表示接收所有关键字参数的动态传参
    4. 入参可以是一个函数
        
    顺序： 位置参数 -> *args -> 默认值参数  -> **kwargs
    可以随意搭配使用
    
实参： 调用函数时，传递的参数
    1. 位置参数：按照位置进行参数传递
    2. 关键字参数：通过参数名称来传递参数， 这时候顺序可改变
    3. 混合参数： 位置参数必须放前面， 关键字参数必须放后面
    
返回值： 函数执行完毕，返回一个结果
    1. 如果没有return， 则接收到的是None
    2. 如果return后面没有跟结果， 则接收到的也是None
    3. 如果return后面跟多个结果， return a, b, c....., 则外界收到的是一个元组，元组内存放所有的返回值
    4. 返回值 可以是一个函数
    
    
'''
def eat(zhu, cai, tang, tian):
    print('吃%s, %s, %s, %s' % (zhu, cai, tang, tian))


# 位置参数：按照位置进行参数传递
eat("米饭", "红烧肉", "番茄蛋汤", "冰淇淋")
# 关键字参数：通过参数名称来传递参数， 这时候顺序可改变
eat(cai="红烧肉", zhu="米饭", tian="冰淇淋", tang="番茄蛋汤")
# 混合方式， 位置参数必须放前面， 关键字参数必须放后面
eat("米饭", "红烧肉", tian="冰淇淋", tang="番茄蛋汤")
# 这种会报错 TypeError: eat() missing 1 required positional argument: 'tian'
# eat(zhu="米饭", "红烧肉", tian="冰淇淋", tang="番茄蛋汤")
    
# def drink(name, zhuliang= "奶茶", pinpai): # 报错
def drink(name, zhuliang= "奶茶", pinpai= "卡旺卡"):
    print('喝%s, %s, %s' % (name, zhuliang, pinpai))
    
def play(*toys): # *args, 表示接收所有位置参数的动态传参
    print(toys)
    
play("篮球", "足球", "乒乓球") # ('篮球', '足球', '乒乓球')

def youxi(**youxis):  # **kwargs, 表示接收所有关键字参数的动态传参
  print(youxis)
  
youxi(name="英雄联盟", level=10) # {'name': '英雄联盟', 'level': 10}
# youxi("篮球", "足球") # TypeError: youxi() takes 0 positional arguments but 2 were given

def hunhe(a, b, c = "hello", *args, **kwargs):
  print(a, b, c, args, kwargs)
  
hunhe(1, "2", "haha", "4", "5", "6", "7", "8") # 1 2 haha ('4', '5', '6', '7', '8') {}
hunhe(1, "2", "haha", "4", "5", name="youxiue", age=18) # 1 2 haha ('4', '5') {'name': 'youxiue', 'age': 18}
hunhe(1, "2",  name="youxiue", age=18) # 1 2 hello () {'name': 'youxiue', 'age': 18}


def hunhe2(a, b, *args,  c = "hello", **kwargs):
  print(a, b, args, c, kwargs)
  
hunhe2(1, "2", "haha", "4", "5", name="youxiue", age=18) # 1 2 ('haha', '4', '5') hello {'name': 'youxiue', 'age': 18}
hunhe2(1, "2", "haha", "4",  c = "5", name="youxiue", age=18) # 1 2 ('haha', '4') 5 {'name': 'youxiue', 'age': 18}

def eatDrink(*cai, **naicha):
  print(cai, naicha)

eatDrink() # () {}
eatDrink("包子") # ('包子',) {}
eatDrink("包子", "红烧肉", "青菜豆腐") # ('包子', '红烧肉', '青菜豆腐') {}
eatDrink("包子", "红烧肉", "青菜豆腐", name="全套奶茶", pinpai="卡旺卡") # ('包子', '红烧肉', '青菜豆腐') {'name': '全套奶茶', 'pinpai': '卡旺卡'}



stu_lst = ["流川枫", "樱木花道", "教练"]

def stu(*args):
  print(args)

# *在实参位置时，是把列表打散成位置参数进行传递
stu(*stu_lst) # ('流川枫', '樱木花道', '教练')


stu_lst2 = {"name": "流川枫", "age": 18}

# ** 在实参位置时，是把字典打散成关键字参数进行传递
def stu2(**kwargs):
  print(kwargs)
  
stu2(**stu_lst2) # {'name': '流川枫', 'age': 18}


def r1(a):
  print(a)
  
ret = r1(1)
print(ret) # None

def r2(a):
  print(a)
  return
  print(a) # 不会执行，到return就停止了

ret = r2(1)
print(ret) # None

def r3(a, b, c):
  return a, b, c 

ret = r3(1, 2, 3)
print(ret) # (1, 2, 3) 

    


# 嵌套函数
def outer():
  def inner():
    print("hello")
  inner()

outer()

# 返回一个函数
def outer():
  def inner():
    print("hello")
  return inner # 返回一个函数

ret = outer()
ret()

# 参数是一个函数
def func(an):
  an()
  
def paramFunc():
  print("hello")

func(paramFunc)

# 函数的作用域
a = 10
def func():
  a = 20 

func()
print(a) # 10 并没有改变a的值

def func():
  global a  # 把外面的全局变量引入到局部
  a = 20
  
func()
print(a) # 20


def func():
  b = 30
  def inner():
    nonlocal b # 向外找一层,如果有该变量则引入, 如果没有则继续向外层寻找, 直到全局,但不包括全局    a = 40
  inner()
  print(b) # 40

func()

'''
闭包
    1. 可以让一个变量常驻内存
    2. 可以避免全局变量被污染
    2. 可以通过返回一个内部函数, 让外界更改函数内的变量
'''

def func():
  a = 10
  def inner():
    nonlocal a
    a += 1
    return a
  return inner

ret = func()

# inner => ret => 什么时候执行
print(ret()) # 11
print(ret()) # 12
print(ret()) # 13

