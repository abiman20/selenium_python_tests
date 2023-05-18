# Python is object oriented programming language 
# Almost everything in python is an object,with its properties and methods
# Class is like an object constructor or a blueprint for creating objects

# 1. Create class name, use the keyword class:
class myclass():
    x = 5

# 2. Create object, we can use the class name to create objects
print("--------2. Create object, we can use the class name to create objects--------")
obj = myclass()
print(obj.x)

# 3. Class Attributes , (name, age are the attributes in class student)
print("--------3. getattr method(get attributes from classs)--------")
class student():
    name = 'Ram'
    age = 25
print(getattr(student,'name'))
print(getattr(student,'age'))

#4. Dot notation to call class attributes
print("--------4. Dot notation to call attributes--------")
print(student.name)
print(student.age)

#5. To change or create new class attribute
print("--------5. To change or create new attribute--------")
setattr(student,'name','sam')
print(student.name)

setattr(student,'gender','male')
print(student.gender)

student.city = 'salem'
print(student.city)

#6. Delete class attribute
print("--------6. Delete attribute--------")
delattr(student,'city')
del student.gender
print(student.__dict__)

#7. Instance attribute
print("-------- 7. Instance attribute--------")
class user:
    course = 'java'
o = user()
print(user.__dict__)
print(user.course) #print class attribute
print(o.__dict__) # nothing in this object
print(o.course)
o.course = 'python'
print(o.__dict__)
print(o.course)
o1 = user()
print(o1.course)

#8. Class method
print("---------8. Class method-------")
class students:
    names = 'abi'
    age = 26
    def printall(): #function name
        print('names:',students.names)
        print('age:',students.age)
students.printall()

class maths:
    def add(a,b):
        c = a + b
        print("Add:",c)
maths.add(10,15)        