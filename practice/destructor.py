# to deallocate memory , to clean up resources
# destrucotr called only when object is  destroyed
# constructor called only when object is created

# 1. sample
class test: #(two methods created)
    def __init__(self): #constructor
        print('object created')
    def __del__(self): #destructor
        print('object deleted')
obj = test() #object created for class test
del obj #object deleted

# 2. sample
class person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
        print('The name is :',self.name)
        print('The agr is:',self.age)
    def __del__(self):
        print('The destructor is called')
obj = person('sakthi', 20)
del obj

# 3. retains same eventhough destructor is written first
class person:
    def __del__(self):
        print('The destructor is called')
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('The name is :',self.name)
        print('The age is:',self.age)
obj = person('ram',22)
del obj