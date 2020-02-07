#class as Object

'''
All classes have a method which is __init__
All methods in a class have self as the first argument
__init__ is the constructor in object orientd language this method is called when an object is created from the class and initializes the class
'''

class Student:
    variable = "something"

    def run(self):
        print("this is a mesage inside a class")

    def walk(self):
        print("walk")

def main():
    sam = Student()
    sam.run()

#__name is a built invariable wich evaluates to the name of the current module, this is a level 0 instruction to the interpreter
if __name__== "__main__":
    main()