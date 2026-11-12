import csv

amount_arr = []
category_totals = {}

with open('expenses.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        amount_arr.append(row['amount'])

        category = row["category"]
        amount = float(row["amount"])

        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount

print(category_totals)

def get_total_expenses(arr_expenses):
    total_expenses = 0

    for amount in arr_expenses:
        total_expenses += float(amount)

    return total_expenses

print(f"Your total spending are: ${get_total_expenses(amount_arr)}")


def get_categories_by_highest_to_lowest(all_categories):
    category_list = all_categories
    sorted_expenses = dict(sorted(category_list.items(), key=lambda item: item[1], reverse=True))
    return sorted_expenses


print(get_categories_by_highest_to_lowest(category_totals))