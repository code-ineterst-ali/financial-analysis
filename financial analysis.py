import pandas as pd
import numpy_financial as npf

class Financial:
    def __init__(self, filename):
        df = pd.read_excel(filename)
        self.cash_flows = df['cash_flows'].dropna().tolist()
        self.n = len(self.cash_flows)

        self.investment = int(input("Enter the capital expenditure: "))

        self.r = float(input("Enter discount rate (e.g., 0.1 for 10%): "))

    def NPV(self):
        total = 0
        for i in range(1, self.n + 1):
            pv = self.cash_flows[i - 1] / (1 + self.r) ** i
            total += pv
        return total - self.investment

    def IRR(self):
        """Calculate IRR using numpy_financial"""
        cash_flows = [-self.investment] + self.cash_flows
        result = npf.irr(cash_flows)

        if result is None:
            return "IRR could not be calculated"
        else:
            return result * 100  # return as percentage

    def payback_period(self):
        cumulative_cash = 0
        for year, cash in enumerate(self.cash_flows, start=1):
            cumulative_cash += cash
            if cumulative_cash >= self.investment:
                return year
        return "Initial investment was never fully recovered"

    def discounted_payback_period(self):
        cumulative_pv = 0
        for year, cash in enumerate(self.cash_flows, start=1):
            discounted_cash = cash / (1 + self.r) ** year
            cumulative_pv += discounted_cash
            if cumulative_pv >= self.investment:
                return year
        return "Initial investment was not recovered within discounted cash flows"


# Run the program
f = Financial("cash_flows.xlsx")
print("Net Present Value (NPV):", f.NPV())
print("Internal Rate of Return (IRR) %:", f.IRR())
print("Payback Period (years):", f.payback_period())
print("Discounted Payback Period (years):", f.discounted_payback_period())
