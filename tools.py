
def revdict(val:dict):
	val.update(dict(reversed(item) for item in val.items()))
	return val