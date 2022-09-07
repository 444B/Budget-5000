

budget = {
    "monthly_income": 0,
    "monthly_expense": 0,
    "bills": {
        "water": 1,
        "electric": 24,
        "rent": 2,
        "cellphone": 600,
        "internet": 9
    }
}


def income_calculator(income_data):
    # check if argument is an int
    if type(income_data) == int:
        calc_income = income_data / 12
        # Set monthly income in budget to calculated income
        budget["monthly_income"] = calc_income
        return calc_income
    else:
        print("Please input a number")


def bill_total(bill_data, income_data):
    total = 0
    if len(bill_data) == 0 and income_data <= 0:
        return
    for amount in bill_data.values():
        total += amount
    budget["monthly_expense"] = total
    return income_data - total


def debt_checker(total_after_bills):
    if total_after_bills < 0:
        return "You broke man, get to work!"
    if total_after_bills > 0:
        return "Keep it up!"
    if total_after_bills == 0:
        return "Comparison is the thief of Joy"


# new function to calculate the percentage of income used to cover expenses
def expense_percentage(bill_data, income_data):
    yearly_percentage = (bill_data / income_data) * 100
    return yearly_percentage


def main():
    # Collect income
    print(f"""
    Your monthly income is:
    {income_calculator(int(input("What is your yearly income, before tax?")))}
    """)

    # Show Total Amount after bills
    print(f"""
    Total Amount after bills: 
    {bill_total(budget["bills"], budget["monthly_income"])}
    """)

    # Show if in debt
    print(f"""
    Debt Checker: 
    {debt_checker(bill_total(budget["bills"], budget["monthly_income"]))}
    """)

    # Show percentage of income that is used on yearly expenses
    print(f"""
    Total percentage of income payed to bills:
    {expense_percentage(budget["monthly_expense"], budget["monthly_income"])}
    """)
    print(budget["monthly_expense"])
    print(budget["monthly_income"])


if __name__ == "__main__":
    main()

# Notes
# I thought we would have to rewrite the whole thing but actually
# its only the way we refference the list that needed to change
# I added a name+main thing to encourage good habits even though it might not be necessary now
# Also, some light formatting in the CLI output to contextualize the values returned

# You can use f-strings and """ """ to make multi line print statements

#
