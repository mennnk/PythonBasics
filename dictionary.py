# initializing

my_dict={}

#adding items

my_dict['name']='jimmy'
my_dict['age']=77
my_dict['state']='UK'

print(my_dict)

#access items

print(my_dict['age'])

# changing items

my_dict['name']='Brian'
print(my_dict['name'])

# remove items by index
del my_dict['state']
print(my_dict)

# iterate
for k in my_dict:
	print(k)