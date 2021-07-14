class binstr:

    def __init__(self, bs):

        self.bs = bs

    def __or__(self, scnd):

        return int(self.bs, 2)|int(scnd.bs, 2)

    def __and__(self, scnd):

        return int(self.bs, 2)&int(scnd.bs, 2)

    def __add__(self, scnd): 

        return int(self.bs, 2)+int(scnd.bs, 2)
 
    def __sub__(self, ot):

        return int(self.bs, 2)-int(scnd.bs, 2)

    def __mul__(self, scnd):

        return int(self.bs, 2)*int(scnd.bs, 2)

    def __lshift__(self, scnd):

        return int(self.bs, 2)<<int(scnd.bs, 2)

    def __rshift__(self, scnd):

        return int(self.bs, 2)>>int(scnd.bs, 2)