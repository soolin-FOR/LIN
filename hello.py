"""我的第一个 Python 程序。

用来练习基本语法：打印、循环、函数。
"""


def say_hello(name):
    """跟指定的人打招呼。"""
    print(f"你好，{name}！")


def count_learning(times):
    """数一数学习了多少次。"""
    for i in range(1, times + 1):
        print(f"这是第 {i} 次学习")


def add(a, b):
    """两个数相加。"""
    return a + b


def main():
    """程序入口。"""
    say_hello("世界")
    count_learning(5)

    result = add(3, 5)
    print(f"3 + 5 = {result}")


if __name__ == "__main__":
    main()
