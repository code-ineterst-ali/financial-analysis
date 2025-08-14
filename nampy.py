import numpy as np

# creating random values:

x=np.arange(1,21,1) #or x=np.arange(20)
x.shape=(4,5)

r=np.linspace(1,20,5)
y=np.ones((2,3))
z=np.zeros((1,2))
w=np.random.random((2,4,2))
v=np.random.randint(1,10,(2,3,4))
vv=np.random.randint(1,10,(20))

print(x)
print(x[1,2])
print(r)
print(y)
print(z)
print(w)
print(v)
print("vv:",vv)
print(v[1,1,2])

# arrays attributes:
print("shape:",x.shape)
print("ndim:",x.ndim)
print("size:",x.size)

#masking array
a=np.arange(20)
b=a>10
print(b) # True-Falise display  =print(a>10)
print(a[b]) # value display
c= a%2==0
print(np.logical_and(b,c))
print(np.logical_or(b,c))

d=np.random.randint(1,5,50)
print(d)
print(np.unique(d))



