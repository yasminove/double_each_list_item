income = [20, 30, 40]

def double_income(dollars):
    return dollars * 2


new_income = list(map(double_income, income))

print(new_income)