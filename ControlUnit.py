R_FORMAT_SIGNALS = {"RegDst" : 1, "ALUSrc" : 0, "MemReg" : 0, "RegWr" : 1, "MemRd" : 0, "MemWr" : 0, "Branch":0, "AluOp1":1, "AluOp0" :0 }

LW_SIGNALS       =  {"RegDst" : 0, "ALUSrc" : 1, "MemReg" : 1, "RegWr" : 1, "MemRd" : 1, "MemWr" : 0, "Branch":0, "AluOp1":0, "AluOp0" :0 }

SW_SIGNALS       =  {"RegDst" : -1, "ALUSrc" : 1, "MemReg" : -1, "RegWr" : 0, "MemRd" : 0, "MemWr" : 1, "Branch":0, "AluOp1":0, "AluOp0" :0 }

BRC_SIGNALS      =  {"RegDst" : -1, "ALUSrc" : 0, "MemReg" : -1, "RegWr" : 0, "MemRd" : 0, "MemWr" : 0, "Branch":1, "AluOp1":0, "AluOp0" :1 }

ADDI_SIGNALS     = {"RegDst" : 0, "ALUSrc" : 1, "MemReg" : 0, "RegWr" : 1, "MemRd" : 0, "MemWr" : 0, "Branch":0, "AluOp1":0, "AluOp0" : 0 }
