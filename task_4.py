# Нужно найти:

# - выручку за всю неделю
# - день с самой большой выручкой
# - среднюю выручку на один заказ в каждый день
# - дни, где возвратов больше 20% заказов

days = [
    {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
    {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
    {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
    {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
    {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
]


week_rev = 0
max_rev = max(days, key=lambda day: day["revenue"])
for day in days:
    week_rev += day["revenue"]

print(f"1. выручка за всю неделю: {week_rev}")
print()
print(f"2. день с самой большой выручкой: {max_rev['day']}")
print()
print("3. средняя выручка на один заказ каждый день:")
for i in days:
    print(f"{i['day']} - {i['revenue'] / i['orders']}")

dayss = []
for i in days:
    if i["returns"] / i["orders"] > 0.2:
        dayss.append(i["day"])
print()
print(f"4. дни, где возвратов больше 20% заказов: {dayss}")
