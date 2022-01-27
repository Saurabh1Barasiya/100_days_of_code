import math as m
n = int(input(""))
val = n/4
if type(val) == float:
    print("Participants of group A",m.floor(val))
    print("Participants of group B",m.ceil(val))
    print("Participants of group C",m.ceil(val))
    print("Participants of group D",m.ceil(val)+3)
else:
    print("sdfsfsdsds")
    print("Participants of group A",val)
    print("Participants of group B",val)
    print("Participants of group C",val)
    print("Participants of group D",val)