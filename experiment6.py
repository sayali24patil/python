#TUPPLE

c1=(6,18,10,16,21,3,23,5,17,12,9)
print(type(c1))

c3=(47,49,51,52,64,59,65)
print(type(c3))

#Concatination operation
c=c1+c3
print(c)

#Calculating the lenth of tupple
print(len(c))
print(len(c1))
print(len(c3))

#Membership operation /boolean operation
print(49 in (c3))

#Slicing Operation
print(c[0:10])
print(c1[:10])