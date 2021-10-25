class A:
    def add(self,a,b):
        return a+b
class B(A):    
   def add(self,a,b):
        return a*b
obj = B()
print(obj.add(5,5))