

class flags:
	f = {"INTERRUPT":False}

	def __init__(self):
		pass

	def __getitem__(self,attr):
		return self.f[attr]

	def __setitem__(self,attr,item):
		self.f[attr] = item

FLAGS = flags()


