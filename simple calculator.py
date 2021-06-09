from operator import add,sub,mul,floordiv

class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        print('Add -',add(self.x,self.y))
    def sub(self):
        print('Sub -',sub(self.x,self.y))
    def mul(self):
        print('Mul -',mul(self.x,self.y))
    def div(self):
        print('Div -',floordiv(self.x,self.y))

calc=calculator(10,5)
calc.add()
calc.sub()
calc.mul()
calc.div()