# Tuple items are ordered, unchangeable, allow duplicate values
# ordered - items have defined order, that order will not change
# unchangeable - we cannot change,add or remove the item from tuple once created
# Allow duplicates - since tuples are indexed, they can have items with the same value
# It remain write protected

mytuple = (1,2.5,True,'Ram')
print(mytuple)
print(type(mytuple))
print(mytuple[1])
print(mytuple[-1])
print(mytuple[0:2])


# 1.Convert tuple into list using list()constructor - to change values
tuple_list = list(mytuple)
print(tuple_list)

# 2.Add element to list - append()
tuple_list.append('Raja')
print(tuple_list)

# 3.Again list is converted into tuple using tuple()constructor 
mytuple= tuple(tuple_list)
print(mytuple)

# 4.For, if else condition
for i in mytuple:
    print(i)
    
if 'Raja' in mytuple:
    print('raja is found')
else:
    print('raja is not found')

# 5.Length of tuple
print(len(mytuple))

# 6.If you Use single item in tuple need to add comma , else it not consider as tuple
mytuple1 = (1)
print(type(mytuple1))
mytuple1 = (1,)
print(type(mytuple1))

# 7.Join using + operator
mytuple2 = mytuple + mytuple1
print(mytuple2)
mytuple2 = mytuple * 2 
print(mytuple2)

# 8.Delete tuple completely usinf 'del' keyword
del mytuple2

# 9.Nested tuple :c = (a,b)
nested_tuple = (mytuple, mytuple1)
print(nested_tuple)
print(nested_tuple[0][0])