# TODO: Try making the income calc loop until a correct input was given
# think about different inputs like 1 obviously isnt going to do anything
# also try doing this without assigning values to the budget dictionary
# also also make a function that validates the income input instead of a long if statement
# also also also see if you can make a function to get the values for EACH bills property ;)

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
    if type(income_data) == int and > 0:
        calc_income = income_data / 12
        # Set monthly income in budget to calculated income
        budget["monthly_income"] = calc_income
        return calc_income
    else:
        print("Please input a valid number")


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
    return (bill_data / income_data) * 100


def main():
    # print all the things together
    print(f"""
    Your monthly income is:
    {income_calculator(int(input("What is your yearly income, before tax?")))}

    Total Amount after bills: 
    {bill_total(budget["bills"], budget["monthly_income"])}

    Debt Checker: 
    {debt_checker(bill_total(budget["bills"], budget["monthly_income"]))}

    Total percentage of income payed to bills:
    {expense_percentage(budget["monthly_expense"], budget["monthly_income"])}
    """)


if __name__ == "__main__":
    main()

# Notes
