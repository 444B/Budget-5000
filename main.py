# YEARLY_SALARY = input("What is your yearly Income before Tax")
# feature for future COUNTRY_CODE = 

monthly_income = 100

bills = {
    "water":1, 
    "electric":24,
    "rent":2,
    "cellphone":6, 
    "internet":9
}

def bill_total(bill_data, income_data):
    total = 0
    if len(bill_data) == 0 and income_data <= 0: return
    for amount in bill_data.values():
        total += amount
        
    return income_data - total
    
print(bill_total(bills, monthly_income))

def debt_checker(total_after_bills):
    if total_after_bills < 0:
        return "You broke man, get to work!"
    if total_after_bills > 0:
        return "Keep it up!"
    if total_after_bills == 0:
        return "Comparison is the thief of Joy"

print(debt_checker(bill_total(bills, monthly_income)))  
