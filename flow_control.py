#if/else/elif

age=1

if(age>=18):
	print('is an adult')
elif(age<5):
	print('is a baby')
else:
	print('is not an adult')

# while loops

while(age<50):
	print('not old enough, current age is '+str(age))
	age+=1

# ternery

age=18

result='old enough' if age>=18 else 'not old enough'
print(result)
