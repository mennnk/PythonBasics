# defining a class

class person:
	
	name=None
	age=None
	
	def say_name(self):
		print('my name is %s' % self.name)
		
	def say_age(self):
		print(f('My age is %d' % self.age)