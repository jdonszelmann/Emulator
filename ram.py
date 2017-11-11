import queue


class Ram:
	def __init__(self,size):
		# self.ram = [0]*size
		self.BOOTLOADER = [

		]
		self.ram = [0x02,0x26,0x0f,0x00,0x00,0x00,0x03,0x0f,0x00,0x01,0x0f,0x02,0x32,0x00,0x05]
		self.operations = queue.Queue()
		from status import STATUS
		self.STATUS = STATUS 

	def get(self,addr):
		try:
			return self.ram[addr]
		except IndexError:
			print("end of ram reached. attempting shutdown...")
			self.STATUS["INTERRUPT"] = True
			return 0

	def set(self,addr,value):
		try:
			self.ram[addr] = value
		except IndexError:
			print("end of ram reached. attempting shutdown...")
			self.STATUS["INTERRUPT"] = True

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
