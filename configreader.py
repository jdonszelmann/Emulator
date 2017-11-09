import json,re
toLower = lambda x: " ".join(a if a in "m" else a.lower() for a in x.split())

multiplier = {
	"n":0.000000001,

	"u":0.000001,

	"mhz":0.001,
	"m":0.001,

	"":1,
	"hz":1,

	"khz":1000,
	"k":1000,

	"M":1000000,
	"Mhz":1000000,
}


def getconfig():
	config = {item:re.findall(r'(\d+)(\w+)?', key)[0] for item,key in json.load(open("./config.json")).items()}
	config = {key:int(item[0]) * multiplier[toLower(item[1])] for key,item in config.items()}
	return config





