
def rFormat(i):
    opcode = i[0:6]
    rs = i[6:11]
    rt = i[11:16]
    rd = i[16:21]
    shamt = i[21:26]
    funct = i[26:32]
    return [opcode, rs, rt, rd, shamt, funct]

def iFormat(i):
    opcode = i[0:6]
    rs = i[6:11]
    rt = i[11:16]
    immediate = i[16:32]
    return [opcode, rs ,rt, immediate]



