from collections import Counter

queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]

counter = Counter(queries)

print(f"1. поисковых запросов в ленте: {len(queries)}")

print("2. сколько раз ввели каждый запрос?")
for a, b in counter.items():
    print(f"{a} - {b}")

max_query = max(counter, key=counter.get)

print(f"3. запрос который вводили чаще всего: {max_query}")

dolya = counter[max_query] / len(queries)
print(f"4. доля самого частого запроса среди всех: {dolya}")

print("5. запросы, которые встретились один раз:")
for a, b in counter.items():
    if b == 1:
        print(a)


queries = [
    "чехол",
    "iphone",
    "чехол",
    "наушники",
    "iphone",
    "iphone",
    "кабель",
    "чехол",
    "iphone",
]
from collections import Counter
print(f"1. Количество поисковых запросов в ленте: {len(queries)}")
counter = Counter(queries)
print("2. Сколько раз ввели каждый запрос?")
for key, item in counter.items(): 
    print(f"{key} - {item}")
print(f"3. Запрос с наибольшим количеством вводов: {max(counter, key = counter.get)}")
print(f"4. Доля, которую занимает запрос с наибольшим количеством вводов среди всех поисков: {(max(counter.values())) / len(queries)}")
lst = [] 
for key, item in counter.items(): 
    if item == 1:
        lst.append(key)
print(f"Запросы, которые встретились один раз: {lst}")