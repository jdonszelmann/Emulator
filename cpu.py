import threading,time,sys,signal


cores = []
corenum = 0


IS = {
	"NOP"	:0x0000,

	"ADDAB"	:0x0001,
	"ADDIB"	:0x0002,
	"ADDAI"	:0x0003,
	"ADDII"	:0x0004,
	"ADDPB"	:0x0005,
	"ADDAP"	:0x0006,
	"ADDPP"	:0x0007,
	"ADDPI"	:0x0008,
	"ADDIP"	:0x0009,

	"SUBAB"	:0x000a,
	"SUBIB"	:0x000b,
	"SUBAI"	:0x000c,
	"SUBII"	:0x000d,
	"SUBPB"	:0x000e,
	"SUBAP"	:0x000f,
	"SUBPP"	:0x0010,
	"SUBPI"	:0x0011,
	"SUBIP"	:0x0012,

	"SUBAB"	:0x000a,
	"SUBIB"	:0x000b,
	"SUBAI"	:0x000c,
	"SUBII"	:0x000d,
	"SUBPB"	:0x000e,
	"SUBAP"	:0x000f,
	"SUBPP"	:0x0010,
	"SUBPI"	:0x0011,
	"SUBIP"	:0x0012,

}


class core(threading.Thread):
	def __init__(self,speed,FLAGS):
		super().__init__()
		self._stop_event = threading.Event()
		# self.daemon = True
		self.FLAGS = FLAGS
		self.speed = speed

		

		self.start()

	def register_self(self):
		global cores, corenum
		self.corenum = corenum
		cores.append(self)
		corenum += 1

	def stop(self):
		global cores
		del cores[cores.index(self)]

	def run(self):
		try:
			while not self.FLAGS["INTERRUPT"]:
				start_time = time.time()

				#code

				halttime = (1/self.speed) - (time.time() - start_time)
				time.sleep(halttime if halttime > 0 else 0)
		except Exception as e:
			print("{}:'{}' in core #{}".format(type(e).__name__,e,self.corenum))
			self.stop()
			

def new_core(speed,FLAGS):
	core(speed,FLAGS)







