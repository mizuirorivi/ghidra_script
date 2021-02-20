#show all func by using flat api
#@author mizuiro_rivi
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


#TODO Add User Code Here

def get_all_func():
        func = getFirstFunction()
        while func is not None:
            yield func
            func = getFunctionAfter(func)
            
funcs = get_all_func()
for func in funcs:
    print('func:{}@{}'.format(func.getName(),func.getEntryPoint()))