 #reusability of code
 #single, multiple, multi level, hybrid , hirerarichal 
 # obj create only for child class
 
 # 1. single inheritance
 # we can access two different class with one object name 
class parent:
    def function1(self):
         print('hello i am from parent class')
         
class child(parent):
    def function2(self):
        print('hello i am from child class')

obj = child()
obj.function1()
obj.function2()


class person:
    def details(self):
        name = 'john'
        age = 25
        gender = 'male'
        print('emp name:',name)
        print('emp age:',age)
        print('emp gender:',gender)
class update(person):
    def details_update(self):
        city = 'chennai'
        print('emp city:',city)

obj = update()
obj.details()
obj.details_update()

# 2. multi level inheritance
class one:
    def function1(self):
        print('i am from class 1')
class two(one):
    def function2(self):
        print('i am from class 2')
class three(two):
    def function3(self):
        print('i am from class 3')
obj = three()
obj.function1()
obj.function2()
obj.function3()


class personal():
    def personal_details(self,name,age,gender):
        print('Emp name:',name,'Emp age:',age,'Emp gender:',gender)
class company(personal):
    def company_details(self):
        cmp_name = 'tcs'
        location = 'chennai'
        print('Company name:',cmp_name)
        print('Company location:',location)
class others(company):
    def other_detail(self):
        salary = 20000
        destination = 'tester'
        print('Salary:',salary)
        print('Destination:',destination)

obj = others()
obj.personal_details('john',23,'male')
obj.company_details()
obj.other_detail()
        
# 3. Multiple inheritance
# one child class derived from two parent class

#this program is just 3 base class
class personal():
    def personal_details(self,name,age,gender):
        print('Emp name:',name,'Emp age:',age,'Emp gender:',gender)
class company:
    def company_details(self):
        cmp_name = 'tcs'
        location = 'chennai'
        print('Company name:',cmp_name)
        print('Company location:',location)
class others:
    def other_detail(self):
        salary = 20000
        destination = 'tester'
        print('Salary:',salary)
        print('Destination:',destination)

obj1 = personal()
obj1.personal_details('john',23,'male')
obj2 = company()
obj2.company_details()
obj3 = others()
obj3.other_detail()

 # this program is added child class from previous program
class personal():
    def personal_details(self,name,age,gender):
        print('Emp name:',name,'Emp age:',age,'Emp gender:',gender)
class company:
    def company_details(self):
        cmp_name = 'tcs'
        location = 'chennai'
        print('Company name:',cmp_name)
        print('Company location:',location)
class others:
    def other_detail(self):
        salary = 20000
        destination = 'tester'
        print('Salary:',salary)
        print('Destination:',destination)
        
class all_details(personal,company,others):
    print('printing the employee detail:',end ='\n\n')
    

obj = all_details()
obj.personal_details('john',23,'male')
obj.company_details()
obj.other_detail()


# 4.Hirearchial inheritance
# direct opposite to multiple inheritance
# one base class two derived class
class parent():
    def name(self):
        print('Father name: shiva')
        print('Mother name: kavitha')
class child1(parent):
    def child_name1(self):
        print('Child 1 name: john')
class child2(parent):
    def child_name2(self):
        print('Child 2 name: riya')

obj1 = child1()
obj2 = child2()

obj1.name()
obj1.child_name1()

obj2.name()
obj2.child_name2()

