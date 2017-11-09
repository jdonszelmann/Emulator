
import queue

class HDD:
	def __init__(self, filename):
		self.file = open(filename,"rb+")
		self.moveto()
		self.operations = queue.Queue()

	def moveto(self,pos=1):
		self.file.seek(pos,0)
	
	def move(self,pos=1):
		try:
			self.file.seek(pos-1,1)
		except:
			return IOError()

	def read(self):
		try:
			return int.from_bytes(self.file.read(1),byteorder='little')
		except IndexError:
			return IndexError("end of hdd reached")

	def write(self,value):
		try:
			self.file.write(bytes([value]))
		except IndexError:
			return IndexError("end of hdd reached")
			
	def update(self):
		if not self.operations.empty():
			a = self.operations.get()
			if a["item"][0] == "READ":
				self.moveto(a["item"][1])
				a["callback"](self.read())
			elif a["item"][0] == "READNEXT":
				self.move(1)
				a["callback"](self.read())
			elif a["item"][0] == "WRITE":
				self.moveto(a["item"][1])
				self.write(a["item"][2])
		else:
			return


	def new_operation(self,item,callback):
		self.operations.put({"item":item,"callback":callback})
