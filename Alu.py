from BitArray import *

class Alu:
    def alucontrol(self,aluop1,aluop0,function=BitArray('222222')):
        if(aluop1 == 0 and aluop0 == 0):
            return BitArray('010')
        elif(aluop1 == 0 and aluop0 == 1 ):
            return BitArray('011')
        elif(aluop1 == 1 and aluop0 == 0):
            if(function == BitArray('100000')):
                return BitArray('010')
            elif(function == BitArray('100010')):
                return BitArray('011')
            elif(function == BitArray('100100')):
                return BitArray('000')
            elif(function == BitArray('100101')):
                return BitArray('001')
            elif(function == BitArray('101010')):
                return BitArray('100')
            elif(function == BitArray('111111')):
                    return BitArray('101')
    def aluoperation(self,aluop,opernd1=None,opernd2=None):
        if(aluop == BitArray('010')):
            return (opernd1+opernd2).extend(val = 0)
        if(aluop == BitArray('011')):
            
            return (opernd1-opernd2).extend(val = 0)
        if(aluop == BitArray('000')):
            return (opernd1&opernd2).extend(val = 0)
        if(aluop == BitArray('001')):
            return (opernd1|opernd2).extend(val = 0)
        if(aluop == BitArray('101')):
            return (opernd1*opernd2).extend(val = 0)
        if(aluop == BitArray('100')):
            if(opernd1<opernd2):
                return BitArray('1')
            else:
                return BitArray('0')

# if __name__ == "__main__":
#     a = Alu()
#     k = a.alucontrol(0,1,100010)
#     l = a.aluoperation(k,BitArray('010'),BitArray('000'))
#     print (l)