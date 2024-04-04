#Accessing items from a tuple

my_tuple = (9, 8, 7, 6)
print(my_tuple[0])
print(my_tuple[-1])

#Adding items in a tuple

#(i)using concatenation
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
new_tuple = tuple1 + tuple2
print(new_tuple)

#(ii)converting list into a tuple
my_list =[1, 2, 3, 4, 5, 6]
my_tuple = tuple(my_list)
print(my_tuple)

#(iii)adding one item
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4,)
print(new_tuple)


#Removing items from a tuple

fruit = ('apple', 'mango', 'orange')
removed_fruit = tuple(fruit for fruit in fruit if fruit !='orange')
print(removed_fruit)
