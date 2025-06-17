# -*- coding: utf-8 -*-
#@author
#@category Decompilation
#@keybinding
#@menupath
#@toolbar

from ghidra.util.task import ConsoleTaskMonitor
from ghidra.app.decompiler import DecompInterface
from ghidra.program.model.symbol import RefType
import os

# Setup decompiler
def decompile(func):
    ifc = DecompInterface()
    ifc.openProgram(currentProgram)
    res = ifc.decompileFunction(func, 60, monitor)
    return res if res.decompileCompleted() else None

# Get functions called directly from a function
def get_called_functions(func):
    called = set()
    listing = currentProgram.getListing()
    refman = currentProgram.getReferenceManager()

    instructions = listing.getInstructions(func.getBody(), True)
    for instr in instructions:
        refs = refman.getReferencesFrom(instr.getAddress())
        for ref in refs:
            if ref.getReferenceType() == RefType.UNCONDITIONAL_CALL:
                called_func = getFunctionAt(ref.getToAddress())
                if called_func:
                    called.add(called_func)
    return called

# Try to find main-like function
def find_main_function():
    names_to_try = ["main", "mainCRTStartup", "__tmainCRTStartup"]
    for name in names_to_try:
        func = getGlobalFunctions(name)
        if func and len(func) > 0:
            return func[0]
    return getFunctionAt(currentProgram.getEntryPoint())

# 🔍 Find main function
monitor = ConsoleTaskMonitor()
main_func = find_main_function()
if not main_func:
    print("❌ Could not locate a main-like function.")
    exit()

# 🧠 Decompile main and its directly called functions
decompiled_main = decompile(main_func)
if not decompiled_main:
    print("❌ Decompilation of main function failed.")
    exit()

called_funcs = get_called_functions(main_func)

# 📝 Write to output.txt on Desktop
output_path = os.path.join(os.path.expanduser("~"), "Desktop", "BintoAssembled", "output.txt")
with open(output_path, "w") as f:
    f.write("// Function: {}\n\n".format(main_func.getName()))
    f.write(decompiled_main.getDecompiledFunction().getC())

    for called in called_funcs:
        f.write("\n\n// Function: {}\n".format(called.getName()))
        result = decompile(called)
        if result:
            f.write(result.getDecompiledFunction().getC())
        else:
            f.write("// Failed to decompile {}\n".format(called.getName()))
