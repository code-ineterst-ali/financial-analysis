
📂 Model 1 – Excel Input
📊 Financial Analysis Tool from Excel (Python)
This script is a financial evaluation utility that reads cash flow data from an Excel file and calculates key investment metrics such as Net Present Value (NPV), Internal Rate of Return (IRR), Payback Period, and Discounted Payback Period.
✨ Features
•	Reads cash flow data directly from an Excel file (.xlsx)
•	Calculates Net Present Value (NPV)
•	Calculates Internal Rate of Return (IRR)
•	Calculates Payback Period (undiscounted)
•	Calculates Discounted Payback Period
📦 Requirements
You need Python 3 and the following packages:
📂 Input File Format
The Excel file (e.g., cash_flows.xlsx) must have a column named: "cash_flows"
Each row in this column represents the net cash flow for a given year (positive or negative). Example:
cash_flows
20000
30000
40000
🚀 How to Run
Run the script:
The script will prompt you for:
1.	Capital expenditure (initial investment, positive number)
2.	Discount rate (as decimal, e.g., 0.1 for 10%)
📋 Example Input/Output
Input:
Enter the capital expenditure: 50000
Enter discount rate (e.g., 0.1 for 10%): 0.1
Example Excel file content (cash_flows.xlsx):
cash_flows
20000
30000
40000
Output:
Net Present Value (NPV): 22562.81
Internal Rate of Return (IRR) %: 24.89
Payback Period (years): 3
Discounted Payback Period (years): 3
📚 Main Functions
•	NPV() → Calculates Net Present Value
•	IRR() → Calculates Internal Rate of Return using numpy_financial.irr()
•	payback_period() → Determines the number of years to recover the investment (no discounting)
•	discounted_payback_period() → Determines the number of years to recover the investment considering the discount rate

📂 Model 2 – Interactive Entry
📊 Financial Analysis Tool (Python)
This script is a simple financial analysis utility that takes investment details, yearly income, and yearly cost, then calculates key financial metrics such as NPV, IRR, Payback Period, and Discounted Payback Period.
✨ Features
•	Net Present Value (NPV) calculation
•	Internal Rate of Return (IRR) calculation
•	Payback Period (undiscounted)
•	Discounted Payback Period
•	Neatly formatted yearly table showing income, cost, and net cash flow
📦 Requirements
You need Python 3 and the following packages:
🚀 How to Run
Run the script 
The script will prompt for:
1.	Number of years
2.	Initial investment (positive number)
3.	Discount rate (as a decimal or percentage, e.g., 0.1 or 10)
4.	Income and cost for each year in the format income,cost (e.g., 50000,20000)
📋 Example Input/Output
Input:
enter number of years: 3
enter initial investment (positive number): 100000
enter discount rate (e.g., 0.1 for 10% or 10 for 10%): 10
input(income,cost) for year 1: 50000,20000
input(income,cost) for year 2: 60000,25000
input(income,cost) for year 3: 70000,30000
Output:
Net Present Value (NPV): 24132.21
Internal Rate of Return (IRR) %: 18.45
Payback Period (years): 3
Discounted Payback Period (years): 3

Year       Income         Cost          Net
--------------------------------------------
   1     50000.00     20000.00     30000.00
   2     60000.00     25000.00     35000.00
   3     70000.00     30000.00     40000.00
--------------------------------------------
 SUM    180000.00     75000.00    105000.00
📚 Main Functions
•	NPV() → Calculates Net Present Value
•	IRR() → Calculates Internal Rate of Return
•	payback_period() → Calculates the time needed to recover the initial investment (no discounting)
•	discounted_payback_period() → Calculates the time needed to recover the initial investment with discounting
•	print_table() → Displays a formatted table of yearly income, cost, and net cash flow





