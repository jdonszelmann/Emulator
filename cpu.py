import threading,time,sys,signal
import configreader,harddisk_interface

from ram import Ram
from register import RegisterSet

config = configreader.getconfig()

cores = []
corenum = 0

ram  = Ram(config["ram-size"])
try: hdd = harddisk_interface.HDD(sys.argv[1])
except IndexError: hdd = harddisk_interface.HDD("disk.hdd")
# vram = Ram(config["vram_size"])


class core(threading.Thread):
	def __init__(self,speed,FLAGS):
		super().__init__()
		self._stop_event = threading.Event()
		# self.daemon = True
		self.FLAGS = FLAGS
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
			if(type(value) == Exception):
				print("EXCEPTION")
			val = value
			e.set()
		
		ram.new_operation(["READ",addr],callback)	
		e.wait()
		return val


	def run(self):
		try:
			while not self.FLAGS["INTERRUPT"]:
				if self.enabled:
					start_time = time.time()

					self.registers.PC += 1
					instruction = self.ram_synchronous_read(self.registers.PC)

					print(instruction)

					halttime = (1/self.speed) - (time.time() - start_time)
					time.sleep(halttime if halttime > 0 else 0)
		
		except Exception as e:
			print("{}:'{}' in core #{}".format(type(e).__name__,e,self.corenum))
			self.stop()
			

def new_core(speed,FLAGS):
	core(speed,FLAGS)


def update():
	hdd.update()
	ram.update()



