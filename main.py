
# TODO remove magic Number
monthly_income = 100

budget = {
    "monthly_income": 100, 
    "bills":{
        "water":1, 
        "electric":24,
        "rent":2,
        "cellphone":600, 
        "internet":9
    }
}

def bill_total(bill_data, income_data):
    total = 0
    if len(bill_data) == 0 and income_data <= 0: return
    for amount in bill_data.values():
        total += amount
        
    return income_data - total

def debt_checker(total_after_bills):
    if total_after_bills < 0:
        return "You broke man, get to work!"
    if total_after_bills > 0:
        return "Keep it up!"
    if total_after_bills == 0:
        return "Comparison is the thief of Joy"


# Introduced a name main thingy, probably good practice
if __name__ == "__main__":
    print(
        "Total Amount after bills\n", 
        bill_total(budget["bills"], budget["monthly_income"])
        )
    
    print(
        "Debt Checker\n",
        debt_checker(bill_total(budget["bills"], budget["monthly_income"]))
        )  

# Notes
# I thought we would have to rewrite the whole thing but actually
# its only the way we refference the list that needed to change
# I added a name+main thing to encourage good habits even though it might not be necessary now
# Also, some light formatting in the CLI output to contextualize the values returned
