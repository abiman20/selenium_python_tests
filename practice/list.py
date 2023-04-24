# List -- used to store multiple items in single variable(store collection of data)
# List items can be of any data type
# List is collection which is ordered & changeable, allow duplicate members
# List is one column multiple rows

fruits = ["apple", "banana", "cherry"]
print('Fruits:',fruits)

# Negative indexing(-1 refers to last item)
print(fruits[-3])

# Range of index(item in position 2 is not included)
print(fruits[1:2])

# Range to end([1:])
print(fruits[1:])

# 1.Add apple to the list(append)
fruits.append("apple")
print('Added apple:',fruits)

# 2.count no of apples(count)
count=fruits.count("apple")
print('Get count of appples:',count)

# 3.extended list(extend)
# you can extend any literal objects like tuples, dicitionaries,sets
veg = ["tomato","cucumber"]
fruits.extend(veg)
print('Extended list:',fruits)

# 4.copy list(copy)
fruits1=fruits.copy()
print('Copied list from fruits to fruits1:',fruits1)

# 5.reverse list(reverse)
fruits1.reverse()
print('Reversed list:',fruits1)

# 6.remove item from list(remove)
fruits1.remove('apple')
print('Item removed:',fruits1)

# 7.remove item from the specified position(pop)
# to remove the last item -- pop()
# 'del' keyword also removes specific index & also deletes the entire list
fruits1.pop(1)
print('Pop :',fruits1)

# 8.sort list by ascending(sort)
fruits1.sort()
print('Sorted list:',fruits1)
# sort descending
fruits1.sort(reverse=True)
print('Sorted Descending:',fruits1)

# 9.print the index of the given element(index)
print('Index of cucumber is :',fruits1.index('cucumber'))

# 10.insert element in list by index number(insert)
fruits1.insert(1,'avocado')
print('Inserted:',fruits1)

# 11.To find data type of list[type()function]
# default data type of list is LIST
print(type(fruits1))

# 12.To find number of items in list [len()function]
print('Length of list:',len(fruits1))

# 13.Check if specified item is present in list use 'in'keyword(in)
if 'apple' in fruits:
    print('yes')


# 14.Change items value(refer index number)
fruits1[1]='strawberry'
print('Changed item:',fruits1)

# 15.Change range of items value
fruits1[3:]= 'blueberry','rasberry'
print('Changed items:',fruits1)

# 16.Clear method empties the list [clear()]
# clear only items , list remains exist
fruits1.clear()
print('Cleared List:',fruits1)

# 17.Using while loop
i=0
while i < len(fruits):
    print(fruits[i])
    i=i+1
    
# 18.List comprehension
# offers shorter syntax when you want to create a new list based on the value of an existing list
# without comprehension,have to write a for statment with conditional test:
newfruits = []
for x in fruits:
    if 'a' in x:
        newfruits.append(x)
print(newfruits)

# 19. with list comprehension, we can do with only one line of code
newfruits = [x for x in fruits if 'a' in x]
print(newfruits)

# 20. Nested list 
a = [1,True,2.3,'ram',[1,2,3,4,5]]
print(type(a[0]))
print(a[4][0]) 

# 21.list constructors
print(list(range(5)))
print(list("Abirami"))

# 22.Join two list using + operator
fruits2 = fruits + fruits1
print(fruits2)
