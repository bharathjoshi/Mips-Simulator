import time
from Alu import *
from Decode import *
from BitArray import *
from ControlUnit import *
from ControlUnit import * 
from MemoryHandling import *

instructions = {}
ADD  = BitArray("100000")
ADDI = BitArray("001000")
MULT = BitArray("011000")
SUB  = BitArray("100010")
BEQ  = BitArray("000100")
BNE  = BitArray("000101")
LW   = BitArray("100011")
SW   = BitArray("101011")
SLL  = BitArray("000000")
J    = BitArray("000010")
HALT = BitArray("111111")
#ADD, ADDI, MULT, SUB, BEQ, BNE, LW, SW, SLL, J
PC = 0 
CLOCK_CYCLES = 0

while(1):
    CLOCK_CYCLES = CLOCK_CYCLES + 1 


    i = IMController(PC)
    
    ALUObject = Alu()
    instructionArray =[]
    signals = {}
    opcode = i[0:6]
    if (opcode == HALT):
        break
    if (opcode == ADD or opcode == MULT or opcode == SUB  or opcode == SLL ):
        format = 'r'
        instructionArray = rFormat(i)
        signals = R_FORMAT_SIGNALS

    
    elif (opcode == ADDI):
        format = 'i' 
        instructionArray = iFormat(i)
        signals = ADDI_SIGNALS

    elif (opcode == LW) :
        format = 'i'
        instructionArray = iFormat(i)
        signals = LW_SIGNALS
    
    elif ( opcode == BEQ ) :
        format = 'i'
        instructionArray = iFormat(i)
        signals = BRC_SIGNALS

    elif (opcode == SW) :
        format = 'i'
        instructionArray = iFormat(i)
        signals = SW_SIGNALS

    elif (opcode == BNE) :
        format = 'i'
        instructionArray = iFormat(i)
        signals = BRC_SIGNALS

    
# Read from Register

    readRegister_1 = RFController(address = instructionArray[1])  #rs
    readRegister_2 = RFController(address = instructionArray[2])  #rt
    writeRegister = instructionArray[3]  if (signals["RegDst"]) else instructionArray[2]  #rt or rd based on the first mux
    signExtend = instructionArray[3] #only when it is in i format else it will take some random thing and we shalln't care :p
    func = instructionArray[5]    if (signals["AluOp1"] and not signals["AluOp0"]) else   BitArray("111111")  #fuction is available only when ALUOp1 and ALUOp
    
    #ALU
    alu_input_code = ALUObject.alucontrol(aluop1 = signals["AluOp1"],aluop0 = signals["AluOp0"],function = func) #to get ALU input code
    alu_input_2 = instructionArray[3].extend() if (signals["ALUSrc"]) else readRegister_2   #signextended or rt based on signal
    ALU_OUTPUT = ALUObject.aluoperation(opernd1 = readRegister_1,opernd2 = alu_input_2,aluop = alu_input_code)    #output from ALU
    
    if (ALU_OUTPUT == BitArray("00000000000000000000000000000000") and signals["Branch"] and opcode == BEQ):
        PC = int(instructionArray[3])       
        continue
    elif (ALU_OUTPUT  == BitArray("00000000000000000000000000000000") and signals["Branch"] and opcode == BNE):
        PC = PC + 1 
        continue
    elif (ALU_OUTPUT != BitArray("00000000000000000000000000000000") and signals["Branch"] and opcode == BNE):
        PC = int(instructionArray[3])
        continue
    else :

        #Memory Stage

        DMController(address = ALU_OUTPUT,data = readRegister_2, MemWrite = signals["MemWr"], MemRead = signals["MemRd"])   #MemoryHandling Takes care i.e when MemRead == 1 it will write or else no
                            
        value_to_be_stored = DMController(address = ALU_OUTPUT, MemWrite = signals["MemWr"], MemRead = signals["MemRd"])
    
        data_to_be_stored =   value_to_be_stored if (signals["MemReg"]) else ALU_OUTPUT

        # Writeback Stage

        RFController(address = writeRegister, data = data_to_be_stored, RegWrite = signals["RegWr"])


    PC = PC + 1 


print 'The answer is stored in S0, i.e "10000" in RegisterFile.json'
print "Number of clock cycles = ", CLOCK_CYCLES