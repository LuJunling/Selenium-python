try:
    print("aa")
    open("aa.txt",'r')
except FileNotFoundError:
    print("异常了")
except IndentationError:
    print("缩进异常")
except SyntaxError:
    print("语法错误")
except NameError:
    print("这是一个name异常")
except BaseException as msg:
    print(msg)