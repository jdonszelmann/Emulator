
import signal,sys

import configreader,cpu,flags

config = configreader.getconfig()

for i in range(config["cores"]):
	cpu.new_core(config["corespeed"],flags.FLAGS)


def signal_handler(signal, frame):
	print('\r\rInterrupt detected! attempting shutdown...\n',end="")
	flags.FLAGS["INTERRUPT"] = True

def exit(message = "Interrupt detected! attempting shutdown..."):
	print('\r\r{}\n'.format(message),end="")
	flags.FLAGS["INTERRUPT"] = True

signal.signal(signal.SIGINT, signal_handler)


while not flags.FLAGS["INTERRUPT"]:
	if len(cpu.cores) < config["cores"]:
		exit("one or more cores have failed. attempting shutdown...")

