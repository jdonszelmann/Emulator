import queue


class Ram:
	def __init__(self,size):
		# self.ram = [0]*size
		self.ram = [0x0000,0x0000,0x0000,0x0000]
		self.operations = queue.Queue()

	def get(self,addr):
		try:
			return self.ram[addr]
		except IndexError:
			return IndexError("end of ram reached")

	def set(self,addr,value):
		try:
			self.ram[addr] = value
		except IndexError:
			return IndexError("end of ram reached")

	def update(self):
		if not self.operations.empty():
			a = self.operations.get()
			if a["item"][0] == "READ":
				a["callback"](self.get(a["item"][1]))

			elif a["item"][0] == "WRITE":
				a["callback"](self.get(a["item"][1]),a["item"][2])
		else:
			return

	def new_operation(self,item,callback):
		self.operations.put({"item":item,"callback":callback})
