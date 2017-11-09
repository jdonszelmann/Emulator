
import signal,sys

import configreader,cpu,status,harddisk_interface

config = configreader.getconfig()

for i in range(config["cores"]):
	cpu.new_core(config["corespeed"])


def signal_handler(signal, frame):
	print('\r\rInterrupt detected! attempting shutdown...\n',end="")
	status.STATUS["INTERRUPT"] = True

def exit(message = "Interrupt detected! attempting shutdown..."):
	print('\r\r{}\n'.format(message),end="")
	status.STATUS["INTERRUPT"] = True

signal.signal(signal.SIGINT, signal_handler)


while not status.STATUS["INTERRUPT"]:
	cpu.update()
	if len(cpu.cores) < config["cores"]:
		exit("one or more cores have failed. attempting shutdown...")

