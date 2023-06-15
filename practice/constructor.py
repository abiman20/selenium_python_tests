#constructor is to initialize(assign values) to the data members of the class when an object of class is created
#types of constructor - default, parameterised
# __init__ is default method of class
# no need to call, it is automatically called
class test:
    def __init__(self):
        print('hai')
obj = test()
        
class student:
    def __init__(self):
        name = 'sakthi'
        age = 23
        print('My name:',name)
        print('My age:',age)
stu1 = student()
stu2 = student()


# overwrite previous result
class person:
    def __init__(self):
        print('1')
    def __init__(self):
        print('2')
p1 = person()

class person:
    def __init__(self):
        print('1')
    def __init__(self):
        print('2')
p1 = person()
p2 = person()
