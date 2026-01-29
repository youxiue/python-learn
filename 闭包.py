# youxiue
# createTime: 2026/1/19

'''
装饰器
本质上是一个闭包
作用: 在不改变原代码的基础上, 添加一些功能
场景: 切面日志

雏形:
  def wrapper(fn):
    def inner(*args, **kwargs):
      # 函数执行后
      ret = fn(*args, **kwargs)
      # 函数执行前
      return ret
    return inner

'''

def guanjia(game):
  def inner():
    print("打开外挂")
    game()
    print("关闭外挂")
    
  return inner

def play_dnf():
  print("玩DNF")
  
  
def play_lol():
  print("玩LOL")

play_dnf = guanjia(play_dnf) # 使用管家把dnf游戏封装一下, 自动开启关闭外挂
play_dnf()

play_lol = guanjia(play_lol)
play_lol()

# 使用@, 相当于: play_wow = guanjia(play_wow)
@guanjia 
def play_wow():
  print("玩WOW")
  
play_wow()

#  传参 和 响应
def super_waigua(game):
  # * ,** 接收所有位置参数和关键字参数, 打包成元组和字典
  def inner(*args, **kwargs):
    print("打开超级外挂")
    # 把元组和字典拆包
    ret =game(*args, **kwargs)
    print("关闭超级外挂")
    return ret
  return inner

@super_waigua
def play_nz(username, password):
  print("玩逆战, 登录账号: %s, 密码: %s" % (username, password))
  return "对局奖励" + str(100)
  
print(play_nz("admin", "123456"))

@super_waigua
def play_dota(username, password, hero):
  print("玩Dota, 登录账号: %s, 密码: %s, 英雄: %s" % (username, password, hero))

play_dota("admin", "123456", hero =  "小牛")




def guanfang(game):
  def inner(*args, **kwargs):
    print("官方游戏管理")
    ret = game(*args, **kwargs)
    print("官方游戏管理")
    return ret
  return inner


# 装饰器嵌套 :  顺序是 上面的在外层, 下面的在内层  
# super_waigua.guanfang.inner
@super_waigua
@guanfang
def play_qqfc():
  print("玩QQ飞车")
  
play_qqfc()
# 打开超级外挂
# 官方游戏管理
# 玩QQ飞车
# 官方游戏管理
# 关闭超级外挂


# 应用示例
login_flag = False
def login_verify(fn):
  def inner(*args, **kwargs):
    global login_flag
    while not login_flag:
      username = input("请输入用户名: ")
      password = input("请输入密码: ")
      if username == "admin" and password == "123456":
        print("登录成功")
        login_flag = True
      else:
        print("用户名或密码错误")
    ret = fn(*args, **kwargs)
    return ret
  return inner

@login_verify
def add_user(name, age):
  print("添加用户: %s, %s" % (name, age))

@login_verify
def update_user(id, name, age):
  print("修改用户: %s, %s, %s" % (id, name, age))

@login_verify
def query_user(id):
  print("查询用户: %s" % id)

@login_verify
def del_user(id):
  print("删除用户: %s" % id)
  
add_user("张三", 18)
update_user(1, "李四", 18)
query_user(1)
del_user(1)
