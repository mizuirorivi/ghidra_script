#TODO write a description for this script
#@author mizuirorivi
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 
import ghidra


#TODO Add User Code Here
def getinst(func):
    inst = getFirstInstruction(func)
    while inst is not None:
        if getFunctionContaining(inst.getAddress()) is func:
            yield inst
            getInstructionAfter(inst)
        

entry = getFirstFunction()
insts = getinst(entry)

c = 0
for i in insts:
    if monitor.isCancelled() or c == 10:
        break
    if i.getFlowType() is not "FALL_THROUGH":
        print("inst => "+str(i))
        print("print value => " + str((i.getOpObjects(0)[0])))
        print("Pcode=>")
        for t in i.getPcode():
            print(t)
    c += 1