import csv


input_f = "Corp_Summary.csv"
output_f = "depart.csv"


# функция которая читает файл 
def read_file(file_name):
    employees = []

#  контекстный менеджер
    with open(file_name, encoding="utf-8-sig") as file:
        reader = csv.DictReader(file, delimiter=";")

        for r in reader:
            employees.append(r)

    return employees



def hierarchy(employees):
    departments = {}

    for employee in employees:
        department = employee["Департамент"]
        team = employee["Отдел"]

        if department not in departments:
            departments[department] = set()

        departments[department].add(team)

    for department, teams in departments.items():
        print(department)

        for team in teams:
            print(" -", team)


#  статистикa по департаментам
def depart(employees):
    departments = {}

    for employee in employees:
        department = employee["Департамент"]
        salary = int(employee["Оклад"])

        if department not in departments:
            departments[department] = []

        departments[department].append(salary)

    result = []

    for department, salaries in departments.items():
        result.append({
            "department": department,
            "count": len(salaries),
            "min_salary": min(salaries),
            "max_salary": max(salaries),
            "avg_salary": round(sum(salaries) / len(salaries), 2)
        })

    return result


# 2. Вывод статистики на экран
def print_summary(employees):
    summary = depart(employees)

    for row in summary:
        print(
            row["department"],
            "количество:", row["count"],
            "минимальная зарплата:", row["min_salary"],
            "максимальная зарплата:", row["max_salary"],
            "средняя зарплата:", row["avg_salary"]
        )


# записываем в цсв
def save_summary(employees, filename):
    summ = depart(employees)

    with open(filename, "w", encoding="utf-8-sig", newline="") as file:
        fieldnames = [
            "department",
            "count",
            "min_salary",
            "max_salary",
            "avg_salary"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames,
            delimiter=";"
        )

        writer.writeheader()
        writer.writerows(summ)



def make_rep(rep_nm):
    employees = read_file(input_f)

    if rep_nm == 1:
        hierarchy(employees)

    elif rep_nm == 2:
        print_summary(employees)

    elif rep_nm == 3:
        save_summary(employees, output_f)
        print("записали отчет в", output_f)

    else:
        print("Такого варианта отчёта нет")


make_rep(3)