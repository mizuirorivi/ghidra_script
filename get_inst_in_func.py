#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here
def get_insts_in_func(func):
	inst = getFirstInstruction(func)
	while inst is not None:
		if getFunctionContaining(inst.getAddress()) is func:
			yield inst
		inst = getInstructionAfter(inst)

entry_func = getFirstFunction()
insts = get_insts_in_func(entry_func)
for inst in insts:
	print('{} {}'.format(inst.getAddressString(True,True),inst))
