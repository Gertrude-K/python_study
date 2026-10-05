import math

# (upper limit of gross salary, NHIF amount)
NHIF_BANDS = [
    (6000, 150), (8000, 300), (12000, 400), (15000, 500),
    (20000, 600), (25000, 750), (30000, 850), (35000, 900),
    (40000, 950), (45000, 1000), (50000, 1100), (60000, 1200),
    (70000, 1300), (80000, 1400), (90000, 1500), (100000, 1600),
]

# (size of band, rate); anything above these bands is taxed at 35%
PAYE_BANDS = [(24000, 0.10), (8333, 0.25), (467667, 0.30), (300000, 0.325)]
TOP_PAYE_RATE = 0.35
PERSONAL_RELIEF = 2400


def get_amount(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("invalid character entered")
            continue
        if not math.isfinite(value) or value < 0:
            print("enter a positive number")
            continue
        return value


def get_nhif(gross_salary):
    for upper_limit, contribution in NHIF_BANDS:
        if gross_salary < upper_limit:
            return contribution
    return 1700


def get_nssf(gross_salary):
    return min(gross_salary, 18000) * 0.06


def get_nhdf(gross_salary):
    return gross_salary * 0.015


def get_paye(taxable_income):
    if taxable_income <= 0:
        return 0
    tax = 0
    remaining = taxable_income
    for band_size, rate in PAYE_BANDS:
        amount = min(remaining, band_size)
        tax += amount * rate
        remaining -= amount
        if remaining <= 0:
            break
    if remaining > 0:
        tax += remaining * TOP_PAYE_RATE
    return max(tax - PERSONAL_RELIEF, 0)


def main():
    basic_salary = get_amount("Enter basic salary: ")
    benefits = get_amount("Enter benefits: ")

    gross_salary = basic_salary + benefits
    nhif = get_nhif(gross_salary)
    nssf = get_nssf(gross_salary)
    nhdf = get_nhdf(gross_salary)
    taxable_income = gross_salary - (nssf + nhdf + nhif)
    paye = get_paye(taxable_income)
    net_salary = gross_salary - (nhif + nhdf + nssf + paye)

    print(f"Gross salary:   {gross_salary:,.2f}")
    print(f"NHIF:           {nhif:,.2f}")
    print(f"NSSF:           {nssf:,.2f}")
    print(f"NHDF:           {nhdf:,.2f}")
    print(f"Taxable income: {taxable_income:,.2f}")
    print(f"PAYE:           {paye:,.2f}")
    print(f"Net salary:     {net_salary:,.2f}")


main()
