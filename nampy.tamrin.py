import numpy as np

num=int(input("enter number of years:"))
r=float(input("enter discoutn rate:")) #Enter discount rate (e.g., 0.1 for 10%)

pattern=[("income","i4"),("cost","i4")]

cashflow=np.zeros((num,1),dtype=pattern)
for i in range(num):
    a=input(f"input(income,cost) for year{i+1}:") 
    income, cost = map(int, a.split(","))
    cashflow[i,0]=(income,cost)
print(cashflow)
total_income = cashflow["income"].sum()
total_cost= cashflow["cost"].sum()
net_profit= total_income - total_cost
print("Total income:", total_income)
print("Total cost:", total_cost)
print("Net profit:", net_profit)

npv_income = 0.0
for i in range(num):
    npv_income += cashflow["income"][i, 0] / ((1 + r) ** (i + 1))  # npv of incomes
print("npv-income:",npv_income)
     
npv_cost = 0.0
for i in range(num):
    npv_cost += cashflow["cost"][i, 0] / ((1 + r) ** (i + 1))  # npv of costs
print("npv-cost:",npv_cost)
print("total NPV:",npv_income- npv_cost)
     
