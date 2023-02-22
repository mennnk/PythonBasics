# A list is a group of data kept together.

#initialize
my_list=[1,2,'name',True,]

print(my_list)


# add items to the list
my_list.append('hello')

print(my_list)


# access items

print(my_list[4])

# change items
my_list[4]=False
print(my_list)

# remove items by index

del my_list[2]
print(my_list)

# iterate

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)
