personal_allowance = 12_500
personal_allowance_limit = 100_000

basic_band = 37_500
highter_band = 150_000

basic_rate = 0.2
highter_rate = 0.4
additional_rate = 0.45

print(" - Income Tax Calculator - ")

salary = float(input("Enter annual salary: "))

if salary > personal_allowance_limit:
    personal_allowance -= (salary - personal_allowance_limit) / 2
    if personal_allowance < 0:
        personal_allowance = 0

taxable_income = salary - personal_allowance

if taxable_income <= 0:
    tax = 0
elif taxable_income > 0 and taxable_income <= basic_band:
    tax = taxable_income * basic_rate
elif taxable_income > basic_band and taxable_income <= highter_band:
    tax = (basic_band * basic_rate) + ((taxable_income - basic_band) * highter_rate)
else:
    tax = (basic_band * basic_rate) + ((highter_band - basic_band) * highter_rate) + ((taxable_income - highter_band) * additional_rate)

year_tax = round(tax, 2)
monthly_tax = round(tax/12, 2)

print(f"Your income tax yearly is ${year_tax} and monthly is ${monthly_tax}.")