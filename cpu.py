import threading,time,sys,signal


cores = []
corenum = 0

class core(threading.Thread):
	def __init__(self,speed,FLAGS):
		super().__init__()
		self._stop_event = threading.Event()
		# self.daemon = True
		self.FLAGS = FLAGS
		self.speed = speed

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







