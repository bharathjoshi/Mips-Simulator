from BitArray import *
from json import load, dump

DMMemory, RFMemory, IMMemory = None, None, None
DataMemory, RegisterFile, InstructionMemory = "DataMemory.json", "RegisterFile.json", "InstructionMemory.json"

with open(DataMemory) as file:

    DMMemory = load(file)

with open(RegisterFile) as file:

    RFMemory = load(file)

with open(InstructionMemory) as file:

    IMMemory = load(file)

def RFController(address, data=0, RegWrite=0):
    if RegWrite:

        RFMemory[str(address)] = str(data)
        saveMemory()

    else:
        if not len(address)-5:
            return BitArray(str(RFMemory[str(address)]))
    

def DMController(address, data=0, MemRead=0, MemWrite=0):

    if MemWrite:

        DMMemory[str(address)] = str(data)
        saveMemory()

    if MemRead:

        return BitArray(str(DMMemory[str(address)]))

def IMController(pcounter):

    return BitArray(str(IMMemory[pcounter]))

def saveMemory():

    D = [{x : str(DMMemory[x]) for x in DMMemory}, {x : str(RFMemory[x]) for x in RFMemory}]
    M = [DataMemory, RegisterFile]

    for _ in xrange(len(M)):

        with open(M[_], "w+") as file:

            dump(D[_], file)

def resetMemory():

    D = [{}, dict.fromkeys(RFMemory, '0'*32), []]
    M = [DataMemory, RegisterFile, InstructionMemory]

    for _ in xrange(len(M)):

        with open(M[_], "w+") as file:

            dump(D[_], file)

resetMemory()