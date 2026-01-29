# youxiue
# createTime: 2026/1/21

'''
类型注解

类型注解只是起到语法提示作用，并不会影响程序运行的结果

好处: 代码的可读性更高

类型注解的语法：
变量名: 类型 = 值

'''

# 指定变量类型
a: int = 675
b: int = "好" # 类型不一致也无所谓
c: str = "hello"
d: bool = True
print(b)

# 还可以指定多种类型
e: int | float | str = 1.5


lst: list[str] = ["a", "b", "c"]
lst.append(100)
print(lst)

s: set[int] = {1, 2, 3}
di: dict[str, int] = {"a": 1, "b": 2}

# 给函数添加类型注解
def add(a: int, b: int) -> int:
    return a + b
  
  
def calc(scores: list[int]) -> float:
    return sum(scores) / len(scores)
  
  
def calc_data(scores: list[int]) -> tuple[int, int, float]:
  return min(scores), max(scores), calc(scores)