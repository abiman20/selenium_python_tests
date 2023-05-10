# Function is a block of code which only runs when it is called
# You can pass data, known as parameters into a function
# A function can return data as a result

# 1.cerating a function - using def as a keyword
print('-----------','1.Creating a function - using def as a keyword','--------')
def welcome():
    print('welcome to python')
# calling a function - function name followed by parenthesis
welcome()
welcome()
welcome()

# 2.No return type without argument function
print('--------','2.No return type without argument function','--------')
def add():
    a = int(input('Enter the value of a:'))
    b = int(input('Enter the value of b:'))
    c = a+b
    print('Total:',c)
add()

# 3.No return type with argument function 
print('--------','3.No return type with argument function','--------')
def sub(a,b):
    c = a-b
    print('Difference:',c)
sub(25,3)

# 4.Return type without argument function
print('--------','4.Return type without argument function','--------')
def mul():
    a = int(input('Enter the value of a:'))
    b = int(input('Enter the value of b:'))
    c = a*b
    return c
x = mul()
print('Mul:',x)

# 5.Return type with argument function
print('--------','5.Return type with argument function','--------')
def div(a,b):
    c = a/b
    return(c)
x = div(6,2)
print('Div:',x)
print('Div:',div(12,2))

# 6.Arbitrary arguments function(*)
# we can pass n number of arguments
print('--------','6.Arbitrary arguments function(*)','--------')
def class_1(*students):
    print(students)
class_1('ram','sam','raj','krish')
print(type(class_1))

# 7.using for loop 
print('--------','7.Using for loop','--------')
def class_1(*students):
    print(students)
    for user in students:
        print(user)
class_1('ram','sam','raj','krish')

# 8.Keyword argument function
#using variable name as keyword
print('--------','8.Keyword argument function','--------')
def student(name,age):
    print(name,' age is ',age)
student(age=25,name='ram')

# 9.Arbitrary keyword arguments in python(**)
print('----------','9.Arbitrary keyword arguments in python(**)','--------')
def class_10(**data):
    print(data)
class_10(name='ram',age=25,gender='male')

# 10.Default parameter value
# if we call the function without argument, it uses the default value
print('----------','10.default parameter value','--------')
def user(name,city='salem'):
    print(name,' is from ',city)
user('ram','erode')
user('sam')

# 11.Passing list as argument
print('----------','11.Passing list as argument','--------')
def total(marks):
    return sum(marks)
print('Total:',total([55,67,89,76,98]))

# 12.Recursive function - a function can call itself
# a defined function can call itself
print('----------','12.Recursive function - a function can call itself','--------')
def factorial(x):
    if x == 1:
        return 1
    else:
        return(x*factorial(x-1))
print('factorial:',factorial(5))

"""
factorial(5)
5*factorial(4)
5*4*factorial(3)
5*4*3*factorial(2)
5*4*3*2*factorial(1)
5*4*3*2*1
120
"""
