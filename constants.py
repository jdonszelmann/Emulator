# A = some register
# B = some register
# I = some immediate value
# P = some pointer to some value


IS = {
	0x0000	:	["NOP",[0]],

	0x0001	:	["ADDAB",[1,1,1]],		# in-progress
	0x0002	:	["ADDIB",[0]],
	0x0003	:	["ADDAI",[0]],
	0x0004	:	["ADDII",[0]],
	0x0005	:	["ADDPB",[0]],
	0x0006	:	["ADDAP",[0]],
	0x0007	:	["ADDPP",[0]],
	0x0008	:	["ADDPI",[0]],
	0x0009	:	["ADDIP",[0]],

	0x000a	:	["SUBAB",[0]],
	0x000b	:	["SUBIB",[0]],
	0x000c	:	["SUBAI",[0]],
	0x000d	:	["SUBII",[0]],
	0x000e	:	["SUBPB",[0]],
	0x000f	:	["SUBAP",[0]],
	0x0010	:	["SUBPP",[0]],
	0x0011	:	["SUBPI",[0]],
	0x0012	:	["SUBIP",[0]],

	0x0013	:	["CMPAB",[0]],
	0x0014	:	["CMPIB",[0]],
	0x0015	:	["CMPAI",[0]],
	0x0015	:	["CMPII",[0]],
	0x0017	:	["CMPPB",[0]],
	0x0018	:	["CMPAP",[0]],
	0x0019	:	["CMPPP",[0]],
	0x001a	:	["CMPPI",[0]],
	0x001b	:	["CMPIP",[0]],

	0x001c	:	["ALSAB",[0]],
	0x001d	:	["ALSIB",[0]],
	0x001e	:	["ALSAI",[0]],
	0x001f	:	["ALSII",[0]],
	0x0021	:	["ALSPB",[0]],
	0x0022	:	["ALSAP",[0]],
	0x0023	:	["ALSPP",[0]],
	0x0024	:	["ALSPI",[0]],
	0x0025	:	["ALSIP",[0]],

	0x0026	:	["ARSAB",[0]],
	0x0027	:	["ARSIB",[0]],
	0x0028	:	["ARSAI",[0]],
	0x0029	:	["ARSII",[0]],
	0x0020	:	["ARSPB",[0]],
	0x002a	:	["ARSAP",[0]],
	0x002b	:	["ARSPP",[0]],
	0x002c	:	["ARSPI",[0]],
	0x002d	:	["ARSIP",[0]],

	0x002e	:	["ANDAB",[0]],
	0x003f	:	["ANDIB",[0]],
	0x0030	:	["ANDAI",[0]],
	0x0031	:	["ANDII",[0]],
	0x0032	:	["ANDPB",[0]],
	0x0033	:	["ANDAP",[0]],
	0x0034	:	["ANDPP",[0]],
	0x0035	:	["ANDPI",[0]],
	0x0036	:	["ANDIP",[0]],

	0x0037	:	["ORAB",[0]],
	0x0038	:	["ORIB",[0]],
	0x0039	:	["ORAI",[0]],
	0x003a	:	["ORII",[0]],
	0x003b	:	["ORPB",[0]],
	0x003c	:	["ORAP",[0]],
	0x003d	:	["ORPP",[0]],
	0x004e	:	["ORPI",[0]],
	0x003f	:	["ORIP",[0]],

	0x0040	:	["XORAB",[0]],
	0x0041	:	["XORIB",[0]],
	0x0042	:	["XORAI",[0]],
	0x0043	:	["XORII",[0]],
	0x0044	:	["XORPB",[0]],
	0x0045	:	["XORAP",[0]],
	0x0046	:	["XORPP",[0]],
	0x0047	:	["XORPI",[0]],
	0x0048	:	["XORIP",[0]],

	0x0049	:	["NANDAB",[0]],
	0x004a	:	["NANDIB",[0]],
	0x004b	:	["NANDAI",[0]],
	0x004c	:	["NANDII",[0]],
	0x004d	:	["NANDPB",[0]],
	0x004e	:	["NANDAP",[0]],
	0x004f	:	["NANDPP",[0]],
	0x0050	:	["NANDPI",[0]],
	0x0051	:	["NANDIP",[0]],

	0x0052	:	["NORAB",[0]],
	0x0053	:	["NORIB",[0]],
	0x0054	:	["NORAI",[0]],
	0x0055	:	["NORII",[0]],
	0x0056	:	["NORPB",[0]],
	0x0057	:	["NORAP",[0]],
	0x0058	:	["NORPP",[0]],
	0x0059	:	["NORPI",[0]],
	0x005a	:	["NORIP",[0]],

	0x005b	:	["NOTA",[0]],
	0x005c	:	["NOTI",[0]],
	0x005d	:	["NOTP",[0]],

	0x005e	:	["POPA",[0]],
	0x005f	:	["POPI",[0]],
	0x0060	:	["POPP",[0]],
	
	0x0061	:	["PUSHA",[0]],
	0x0062	:	["PUSHI",[0]],
	0x0063	:	["PUSHP",[0]],

	0x0064	:	["RET",[0]],
	0x0065	:	["CALL",[0]],

	0x0066	:	["MOVAB",[1,1]],		# implemented
	0x0067	:	["MOVIB",[2,1]],		# implemented
	0x0068	:	["MOVPB",[0]],
	0x0069	:	["MOVAP",[0]],
	0x006a	:	["MOVIP",[0]],
	0x006b	:	["MOVPP",[0]],
	
	0x006c	:	["INT",[0]],
}




