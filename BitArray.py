from array import array
from random import randint

WORDSIZE = 32

class BitArray(object):

    # function override - s

    def __len__(self):

        return self.length

    def __str__(self):

        return "{}".format("".join("{:d}".format(value) for value in self.value))

    def __int__(self):

        return int(str(self), 2)

    def __init__(self, lst):

        self.length = len(lst)
        self.value = array('b', [0 if(str(_) == '0') else randint(0, 1) if(str(_).lower() == 'x') else 1 for _ in lst])

    def __getitem__(self, key):

        if isinstance(key, slice):

            return BitArray(self.value[key.start:key.stop].tolist())

        return BitArray(str(self.value[key]))

    def __getslice__(self, i, j):

        return self.__getitem__(slice(i, j))

    # function override - e

    # operator override - s

    def __eq__(self, ot):

        return str(self) == str(ot)

    def __lt__(self, ot):

        return int(str(self), 2) < int(str(ot), 2)

    def __gt__(self, ot):

        return int(str(self), 2) > int(str(ot), 2)

    def __le__(self, ot):

        return int(str(self), 2) <= int(str(ot), 2)

    def __ge__(self, ot):

        return int(str(self), 2) >= int(str(ot), 2)

    def __or__(self, ot):

        return BitArray(bin(int(str(self), 2)|int(str(ot), 2))[2::])

    def __and__(self, ot):

        return BitArray(bin(int(str(self), 2)&int(str(ot), 2))[2::])

    def __add__(self, ot): 

        return BitArray(bin(int(str(self), 2)+int(str(ot), 2))[2::])

    def __sub__(self, ot):

        return BitArray(bin(int(str(self), 2)-int(str(ot), 2))[2::])

    def __mul__(self, ot):

        return BitArray(bin(int(str(self), 2)*int(str(ot), 2))[2::])

    def __lshift__(self, ot):

        return BitArray(bin(int(str(self), 2)<<int(str(ot), 2))[2::])

    def __rshift__(self, ot):

        return BitArray(bin(int(str(self), 2)>>int(str(ot), 2))[2::])

    # operator override - e

    # user methods - s

    def extend(self, val=None):

        if val != None:

            if not int(val):

                lst = str(0)

            else:

                lst = str(1)

        else:

            lst = str(self[0])

        return BitArray((lst*(WORDSIZE-len(self)))+str(self))

    # user methods - e

# if __name__ == "__main__":

#     C = BitArray("101")
#     D = BitArray("000")
#     E = BitArray("110")

#     print C
#     print D
#     print E