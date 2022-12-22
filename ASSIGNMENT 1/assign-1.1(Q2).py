a= int(input("your gross income"))

b= int(input("number of dependents"))

standard_deduction= 10000

additional_deduction= b * 3000


taxable_income= a- standard_deduction - int(additional_deduction)
print("taxable income" + str(taxable_income))

tax_rate= 0.20

tax= taxable_income + tax_rate
print("tax"+ str(tax))