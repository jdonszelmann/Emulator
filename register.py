
class register:
	def __init__(self):
		self.value = 0


class RegisterSet:
	def __init__(self, ammount):
		self.registers = [register() for i in range(ammount)]
		self.defaultregisters = [register() for i in range(3)]

	def __getitem__(self,item):
		return self.registers[item].value
	
	def __setitem__(self,item,value):
		self.registers[item].value = value

	def __setattr__(self,attr,value):
		if attr in ["PC","BP","SP"]:
			self.defaultregisters[["PC","BP","SP"].index(attr)].value = value
		else:
			self.__dict__[attr] = value

	def __getattr__(self,attr):
		if attr in ["PC","BP","SP"]:
			return self.defaultregisters[["PC","BP","SP"].index(attr)].value
		else:
			return self.__dict__[attr]

	def __repr__(self):
		print("===================================================================\n",end="")
		print("PC:{}, BP:{}, SP:{}\n".format(self.defaultregisters[0].value,self.defaultregisters[1].value,self.defaultregisters[2].value),end="")
		for index,i in enumerate(self.registers):
			print("{}:{} ".format(index,i.value),end="")
		print()
		print("===================================================================",end="")
		return "\n"







