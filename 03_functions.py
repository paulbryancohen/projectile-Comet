# a function is a logical block of code with a name
def func1():
    print("I am Learning functions")

func1()

#functions with args

def func2(arg1,arg2):
    print(arg1,"",arg2)

func2(10,20)

def func3(x):
    return x*x

print(func3(4))

def func4(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print("learning n-args", func4(1,2,3,4,5,6))