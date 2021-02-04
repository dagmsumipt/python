from sys import argv
script_name, salary_per_h, h, prem = argv
salary = float(salary_per_h)*float(h) + float(prem)
print(salary)
