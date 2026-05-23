ename = str(input ("Enter employee name: "));
basic_salary = float(input("Enter basic salary: "));
bonus_amount=float(input("Enter bonus amount: "));
tax_Percentage=float(input("enter tax percentage :"))


gross_salary= basic_salary + bonus_amount;
tax_amount = (gross_salary*tax_Percentage)/100;
net_salary = gross_salary - tax_amount


print("_____________________")
print("Salary Slip ");

print("Employee name is  :",ename);
print("employee basic salary is  :",basic_salary);
print("employee bonus amount is  :",bonus_amount);
print("employee tax percentage is  :",tax_Percentage);

print("Gross salary is :",gross_salary);
print("Tax amount is :",tax_amount);
print("Net salary is :",net_salary);
