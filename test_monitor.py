#TODO write a description for this script
#@author 
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here

from org.apache.commons.io import monitor
from aQute.bnd.osgi import Instruction
instructions = currentProgram.getListing().getInstructions(True)
while instructions.hasNext():
    if monitor.isCancelled():
        break
    instruction = instructions.next()
    print(instruction)