 Financial-analysis

A fast and simple Python tool to calculate key financial indicators (NPV, IRR, Payback, Discounted Payback) directly from Excel input.

 Financial Analysis Tool:

This is a lightweight Python project for quickly calculating key financial indicators from an Excel file.  
The tool helps evaluate investment projects based on cash flow data.

 Features:

- Net Present Value (NPV)
- Internal Rate of Return (IRR)
- Payback Period
- Discounted Payback Period

 Input Format:

Your Excel file must contain a column named exactly: cash_flows

Each row under this column should represent the cash flow of a specific period (e.g., Year 1, Year 2, etc.).

 Example: `cash_flows.xlsx`

| cash_flows |
|------------|
| 100        |
| 150        |
| 200        |

 How to Run:

1. Install required packages:

```bash
pip install pandas numpy-financial openpyxl

2. Place your Excel file (e.g., cash_flows.xlsx) in the same directory as the script.

3. Run the Python script:

4. When prompted:

Enter the initial investment amount (e.g., 500)

Enter the discount rate (e.g., 0.1 for 10%)

The script will calculate and print:

NPV (Net Present Value)

IRR (Internal Rate of Return)

Payback Period (in years)

Discounted Payback Period (in year





