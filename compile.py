import re, argparse
import constants,tools

parser = argparse.ArgumentParser(description='compile asm to bytecode')
parser.add_argument("filename", help="input file",type=str)
# parser.add_argument("-r","--run", help="increase output verbosity",action="store_true")
argvs = parser.parse_args()


operation = re.compile(r"(\w+) +(?:(.*?) *[,;] *)?(?:(.*?) *[,;] *)?(?:(.*?) *[,;] *)?")
label = re.compile(r":(\w+)")

P1 = re.compile(r"\[[Rr](\d+)\]")
P2 = re.compile(r"\[(?<![Rr\n])(\d+)\]")
I = re.compile(r"(?<![Rr\n\[])(\d+)")
R = re.compile(r"[Rr](?<![\n\[])(\d+)")
LABELNAME = re.compile(r"(?<![\n\[Rr])(\w+)")
labels = {}
PC = 0

with open(argvs.filename,"r") as f:
	program = []
	for i in (i+";" for i in f.read().replace('\n',';').split(";")):
		instruction = ""
		args = []
		argc = 0
		matches = operation.search(i)
		islabel = label.search(i)
		if islabel:
			labels.update({islabel.groups()[0]:PC})
		elif matches:
			# print(matches.groups[0])
			instruction += matches.groups()[0].upper()
			for i in matches.groups()[1:]:
				if i == None:
					continue
				temp = P1.match(i)
				if temp:
					# print("P + Register ",temp.group(1))
					instruction += "P1"
					args.append(int(temp.groups()[0]))
					argc+=1
					continue
				temp = P2.match(i)
				if temp:
					# print("P + Immediate ",temp.group(1))
					instruction += "P2"
					args.append(int(temp.groups()[0]))
					argc+=1
					continue
				temp = I.match(i)
				if temp:
					# print("I ",temp.group(1))
					instruction += "I"
					args.append(int(temp.groups()[0]))
					argc+=1
					continue
				temp = R.match(i)
				if temp:
					# print("R ",temp.group(1))
					instruction += list("ABC")[argc]
					args.append(int(temp.groups()[0]))
					argc+=1
					continue
				temp = LABELNAME.match(i)
				if temp:
					try:
						instruction += "I"
						args.append(labels[temp.groups()[0]])
						argc+=1		
					except:
						try:
							raise SystemExit("LABEL {} DOES NOT EXIST".format(temp.groups()[0]))		
						except:
							raise SystemExit("LABEL DOES NOT EXIST")
					continue

			# print(instruction,args)
			# print(constants.IS[tools.revdict(constants.IS,0)[instruction]][1])
			instruction = tools.revdict(constants.IS,0)[instruction]
			t = "{0:#0{1}x}".format(int(instruction),6)[2:]
			lines = [int(t[:2],16),int(t[2:],16)]
			for index,i in enumerate(constants.IS[instruction][1]):
				line = "{0:#0{1}x}".format(args[index],i*2+2)[2:]
				lines += [int(line[j:j+2],16) for j in range(0, len(line), 2)]
			program += lines
			PC += len(lines)


	print("program = [{}]".format(",".join("{0:#0{1}x}".format(i,4) for i in program)))













