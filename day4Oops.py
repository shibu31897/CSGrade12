# defining class
b = 2000
class Ops:
   def __init__(self,a,b):
       print(f"Welcome from constructor the value provided is {a} and {b}")
       self.firstValue = a
       self.secondValue = b


   def sum(self):
       print( self.firstValue+self.secondValue)


op = Ops(5,6)
op.sum()


