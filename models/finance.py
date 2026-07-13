class Finance:

    def __init__(self):
        self.monthly_expenses = []
        self.monthly_income = []

    def add_expense(self):
        
        amount = float(input("Enter amount: "))
        expense_type = input("What was the expense for?: ")
        day = int(input("Enter todays date: "))

        expense = {
            "amount" : amount,
            "expense type" : expense_type,
            "date" : day
        }

        self.monthly_expenses.append(expense)
        print(self.monthly_expenses)


    def add_income(self):
        
        amount = float(input("Enter amount: "))
        income_type = input("Where did you get the money?: ")
        date = int(input("what date did your receive the money?: "))

        income = {
            "amount" : amount,
            "income type" : income_type,
            "date" : date
        }

        self.monthly_income.append(income)
        print(self.monthly_income)



