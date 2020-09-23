import random
import time
class Group:

	def __init__(self):
		self.num_grp = 0
		self.names = []
		
	def input_num(self):
		int_met = False
		while not int_met:
			try:
				self.num_grp = int(input('How many people do you want in a group? '))
				int_met = True
			except:
				print('Please enter an integer value!')
				
	def input_name(self):
		print("Enter name(s) here, then 'x' when finished: ")
		while True:
			name = input().title()
			if name == 'X':
				print('\n')
				break
			elif not name.isspace():
				self.names.append(name)
			else:
				print('That is an invalid entry')
				
	def check_names(self):
		while len(self.names) < self.num_grp:
			print(f'Not enough names to make a group of {self.num_grp}!')
			print(f'Need at least {self.num_grp-len(self.names)} more name(s)\n')
			self.input_name()
			
	def gen_group(self):
		for i in range(int(len(self.names)/self.num_grp)):
			group = random.sample(self.names,self.num_grp)
			print(f'Group {i+1}:',*group,sep='\n')
			print()
			self.names = [n for n in self.names if n not in group]
			del group
			if len(self.names) < self.num_grp and self.names:
				print(f'Group {i+2}:',*self.names,sep='\n')
t1 = time.time()
t2 = time.time()
res = t2 - t1
res *= 1000
def gen():
	group = Group()
	group.input_num()
	group.input_name()
	group.check_names()
	t1
	group.gen_group()
	t2
	print('\nTime taken to compute: %1.5fms'%res)
gen()

