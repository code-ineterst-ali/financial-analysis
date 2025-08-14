
import numpy as np
import numpy_financial as npf

class Financial:
    def __init__(self):
        # --- Inputs ---
        self.n = int(input("enter number of years: "))
        self.investment = float(input("enter initial investment (positive number): "))
        r_in = float(input("enter discount rate (e.g., 0.1 for 10% or 10 for 10%): "))
        # Normalize rate: if user enters 10 treat it as 0.10
        self.r = r_in / 100.0 if r_in > 1 else r_in

        # --- Structured array to store income and cost per year ---
        # Use float64 ('f8') for better numerical precision
        dtype_pattern = [("income", "f8"), ("cost", "f8")]
        flows = np.zeros(self.n, dtype=dtype_pattern)  # 1D is simpler than shape (n, 1)

        # Collect yearly income and cost
        for i in range(self.n):
            a = input(f"input(income,cost) for year {i+1}: ")
            income, cost = map(float, a.split(","))
            flows[i] = (income, cost)

        # Keep the full structured array for reporting,
        # and also store a 1D float array of net cash flows for calculations
        self.flows = flows
        self.income = flows["income"]
        self.cost = flows["cost"]
        self.cash_flows = (self.income - self.cost).astype(float)  # net cash flow per year

    def NPV(self):
        """Net Present Value: sum(CF_t / (1+r)^t) - initial investment."""
        discounts = (1 + self.r) ** np.arange(1, self.n + 1, dtype=float)
        pv = (self.cash_flows / discounts).sum()
        return pv - self.investment

    def IRR(self):
        """Internal Rate of Return using numpy_financial.irr."""
        # Build full cash-flow vector including the initial outflow
        cf = np.concatenate(([-self.investment], self.cash_flows))
        irr = npf.irr(cf)
        # numpy_financial.irr returns np.nan if it cannot find a solution
        if irr is None or np.isnan(irr):
            return "IRR could not be calculated"
        return irr * 100  # percentage

    def payback_period(self):
        """Years until cumulative undiscounted cash flows recover the initial investment."""
        cumulative = 0.0
        for year, cash in enumerate(self.cash_flows, start=1):
            cumulative += cash
            if cumulative >= self.investment:
                return year
        return "Initial investment was never fully recovered"

    def discounted_payback_period(self):
        """Years until cumulative discounted cash flows recover the initial investment."""
        cumulative_pv = 0.0
        for year, cash in enumerate(self.cash_flows, start=1):
            cumulative_pv += cash / (1 + self.r) ** year
            if cumulative_pv >= self.investment:
                return year
        return "Initial investment was not recovered within discounted cash flows"

    def print_table(self):
        """Pretty-print a table of income, cost, and net by year, plus totals."""
        header = f"{'Year':>4}  {'Income':>12}  {'Cost':>12}  {'Net':>12}"
        print("\n" + header)
        print("-" * len(header))
        for i in range(self.n):
            print(f"{i+1:>4}  {self.income[i]:>12.2f}  {self.cost[i]:>12.2f}  {self.cash_flows[i]:>12.2f}")
        print("-" * len(header))
        print(f"{'SUM':>4}  {self.income.sum():>12.2f}  {self.cost.sum():>12.2f}  {self.cash_flows.sum():>12.2f}")

# --- Run ---
f = Financial()
print("Net Present Value (NPV):", f.NPV())
print("Internal Rate of Return (IRR) %:", f.IRR())
print("Payback Period (years):", f.payback_period())
print("Discounted Payback Period (years):", f.discounted_payback_period())
f.print_table()
