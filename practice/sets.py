# Sets are used to store multiple item in single variable
# Sets is a collection which is unchangeable, unordered, uninedexed
# Set items are unchangeable, but you can remove items and add new items
# Dplicates not allowed 
# You cannot access item by refering index : access item by loop

# 1.Sample test
my_set = {'apple','banana','cherry'}
print(my_set)

# 2.Duplicates not allowed: Sets cannot have two items with same value
# Duplicate values will be ignored
my_set1 = {'apple','banana','apple','cherry'}
print(my_set1)

# 3.True & 1 is considered as same value
my_set2 = {'apple','banana','cherry',1,True}
print(my_set2)

# 4.Access item by loop
for i in my_set:
    print(i) 
    
# 4.Add new element
my_set.add('papaya')
print(my_set)

# 5.Update another set of data : tojoin
my_set3 = {5}
my_set.update(my_set3)
print(my_set)

# 6.Add any iterables : add set to list, tuple, dictionary
my_list = [2,3,4]
my_set.update(my_list)
print(my_set)

# 7.Remove element from set(Give exception if item is not there)
my_set.remove(5)
print(my_set)

# 8.Discard element from set (Does not give any exception if it is not there)
my_set.discard('Papaya')
print(my_set)

# 9.Pop element from set (it remove value randomly)
my_set.pop()
print(my_set)

# 10.Clear set : to clear all the elements in set
my_set2.clear()
print(my_set2)

# 11.Join two sets : union() method , update()method
# union() method returns a new set with all items from both sets
# update() method inserts the items in one set to another set
my_set3 = my_set.union(my_set1)
print(my_set3)

# 12.Keep only duplicates : intersection
# intersection_update() method wil keep only items that are present in both sets
a = {1,2,3,4,5}
b = {1,3,5,7,9}
a.intersection_update(b)
print(a)

# intersection() method wil return a new set that only contains the items present in both sets
c = a.intersection(b)
print(c)

# 13.Keep all but not the duplicates
# symmetric_difference_update() method wil keep only the elements that are not present in both sets
a.symmetric_difference_update(b)
print(a)

# symmetric_difference() method will retuen a new set, only the elements that are not in both sets
d = a.symmetric_difference(b)
print(d)

# 14. isdisjoint() : returns whether two sets have intersection or not : true or false
c = a.isdisjoint(b)
print(c)

# 15. issubset() : Returns whether another set contains this set or not
c = a.issubset(b)
print(c)

# 16. issuperset() : Returns whether this set contains another set or not
c = a.issuperset(b)
print(c)

# 17. Delete set :
del c



