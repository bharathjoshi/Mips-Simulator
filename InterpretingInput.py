from sys import argv
from json import load, dump
from MemoryHandling import saveMemory, resetMemory

InstructionMemory = "InstructionMemory.json"

resetMemory()

if len(argv)-1:

    with open(argv[1]) as file:

        instructions = [_[:-1] for _ in list(file)]

    with open(InstructionMemory, "w+") as file:

        dump(instructions, file)

else:

    print "No input file."