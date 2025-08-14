import numpy as np
a=int(input("enter number of construction years:"))
b=int(input("enter number of operational years:"))
aa=np.arange(1,a+1,1)#ماتريس سال هاي ساخت
bb=np.arange(1,b+1,1)#ماتريس سال هاي بهره برداري
print(aa)
print(bb)
construction_costs = np.zeros(a, dtype=float)
for i in range (a):
 c=float(input(f"enter construction cost in year {i+1}:"))
 construction_costs[i]=c

print("Construction costs array:", construction_costs)
