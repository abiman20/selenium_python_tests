# Dictionaries are used to store data values in key:value pairs
# Dictionary is a collection which is ordered, changeable and do not allow duplicates
# Keys : values

# 1.Dictinaries are written with curly brackets, and have key and values
user = {'name':'ram','age':25,'Ismarried': False}
print(user)
print(type(user))
print(len(user))

# 2.Duplicates not allowed
# Dictionaries cannot have two item with the same key
# Duplicate value will overwrite existing values
user1 = {'name':'ram','age':25,'Ismarried': False,'age':26}
print(user1)

# 3.Access item by refering to its key name, inside square brackets
print(user['name'])

# 4.get() method also give the same result
print(user.get('name'))

# 5.Get keys() method will return a list of all the keys in the dictionary
print(user.keys())

# 6.Add a new item to the dictionary and see that key list gets updated 
user['gender'] = 'male'
print(user.keys())

# 7.Get values() method wil return a list of all the values in dictonary
print(user.values())

# 8.Get items() method wil return each item in a dictionary, as tuples in a list
print(user.items())

# 9.Check if key exists
if 'age' in user:
    print('yes')
    
# 10. for loop :
# when looping through dictionary the return values are 'keys', there are methods to return values as well
for x in user:       # for x in user.keys()
    print(x)         # print(x)

for x in user:       # for x in user.values():
    print(user[x])   # print(x)

for x,y in user.items():
    print(x,y)

# 11.Change values 
# you can change the values of a specific item by refering its key name
user['age'] = '26'
print(user)

# 12.Update dictionary
#update() method will update the items with given argument 
#argument must be dictionary or any iterable object with key:value pairs
user.update({'age':28})
print(user)

# 13. pop() method removes the item with specified key name
user.pop('gender')
print(user)

# 14.popitem() method removes the last inserted item
user.popitem()
print(user)

# 15.clear() method empties the dictionary
user1.clear()
print(user1)

# 16.del keyword removes the item with specified key name
del user['age']
print(user)

# 17. del keyword can also delete the dictionary completely
del user1

# 18. Nested dictionary
users = {
    'user1' : {
        'name':'ram',
        'age':25
    },
    'user2' : {
        'name': 'sam',
        'age': 26
    }
}

print(users)

# 19.Access items in nested dictionaries
#use the name of the dictionary, starting with outer dictionary
print(users['user2']['name'])

# 20. Copy dictinary
#copy() method is used to copy, we cannot assign like user = user1, because user is only reference, changes made wil automatically link to one another
user3 = user.copy()
print(user)

# 21.Another way to copy using  buit in dict() function
user4 = dict(user)
print(user4)