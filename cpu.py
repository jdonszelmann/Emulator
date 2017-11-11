import threading,time,sys,signal
import configreader,harddisk_interface, tools

from ram import Ram
from constants import IS
from register import RegisterSet

config = configreader.getconfig()

cores = []
corenum = 0

ram  = Ram(config["ram-size"])
try: hdd = harddisk_interface.HDD(sys.argv[1])
except IndexError: hdd = harddisk_interface.HDD("disk.hdd")
# vram = Ram(config["vram_size"])


class core(threading.Thread):
	def __init__(self,speed):
		super().__init__()
		self._stop_event = threading.Event()
		# self.daemon = True

		from status import STATUS
		self.STATUS = STATUS
		self.speed = speed

		self.enabled = True

		self.registers = RegisterSet(config["register-num"])
		
		self.register_self()
		self.start()

	def register_self(self):
		global cores, corenum
		self.corenum = corenum
		cores.append(self)
		corenum += 1

	def stop(self):
		global cores
		del cores[cores.index(self)]

	def ram_to_register(self,addr,register):
		def callback(value):
			self.enabled = True
			self.registers[register] = value
		self.enabled = False
		ram.new_operation(["READ",addr],callback)

	def register_to_ram(self,addr,register):
		def callback(value):
			self.enabled = True
		self.enabled = False
		ram.new_operation(["WRITE",addr,self.registers[register].value],callback)

	def ram_synchronous_read(self,addr):
		val = None
		e = threading.Event()
		def callback(value):
			nonlocal val, e
			val = value
			e.set()
		ram.new_operation(["READ",addr],callback)	
		e.wait(0.5)
		return val

	def NOP(self,*args):
		pass

	def ADDABC(self,reg1,reg2,reg3):
		self.registers[reg3] = self.registers[reg2] + self.registers[reg1]

	def ADDAIC(self,reg1,imm1,reg3):
		print(reg1,imm1,reg3)
		self.registers[reg3] = imm1 + self.registers[reg1]

	def MOVAB(self,reg1,reg2):
		self.registers[reg1] = self.registers[reg2]

	def MOVAI(self,reg,val):
		self.registers[reg] = val


	def JMPI(self,val):
		self.registers.PC = val

	def run(self):
		try:
			while not self.STATUS["INTERRUPT"]:
				if self.enabled:
					start_time = time.time()

					instruction = IS.get((self.ram_synchronous_read(self.registers.PC)<< 8) + self.ram_synchronous_read(self.registers.PC+1),"NOP")
					self.registers.PC += 2
					args = []
					for i in instruction[1]:
						val = 0
						for _ in range(i):
							val <<= 8
							val += (self.ram_synchronous_read(self.registers.PC))
							self.registers.PC += 1
						args.append(val)
					print(args)

					getattr(self,instruction[0])(*args)

					if self.STATUS["DEBUG"]:
						print(self.registers,end="")
						print(str(instruction[0]) + " " + str(args) + "\n",end="")

					halttime = (1/self.speed) - (time.time() - start_time)
					time.sleep(halttime if halttime > 0 else 0)
		
		except Exception as e:
			if not self.STATUS["INTERRUPT"]:
				print("{}:'{}' in core #{}".format(type(e).__name__,e,self.corenum))
				self.stop()
			

def new_core(speed):
	core(speed)


def update():
	hdd.update()
	ram.update()



