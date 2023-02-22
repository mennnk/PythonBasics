# defining a funciton

def my_fun():
	print('This is function')

my_fun();

def my_func1(a,b):
	print(a+b)

my_func1(b=6,a=9)

# arguments/return
def my_func2(a,b):
	return(a+b)

print(my_func2(2,8))

# multiple returns

def square(a,b):
	return(a**2,b**2)

print(square(5,8))

def square(a,b):
	return(a**2,b**2)

result1,result2=square(7,9)
print(result1,result2)




	