# Нужно найти:

# - среднюю оценку каждого товара
# - худший товар по средней оценке среди тех, у кого хотя бы два отзыва
# - сколько отзывов на 1 или 2 звезды
# - какую долю всех отзывов они составляют

reviews = [
    {"id": 1, "product": "Чехол", "stars": 5},
    {"id": 1, "product": "Чехол", "stars": 3},
    {"id": 1, "product": "Чехол", "stars": 4},
    {"id": 2, "product": "Наушники", "stars": 2},
    {"id": 2, "product": "наушники", "stars": 2},
    {"id": 2, "product": "НАУШНИКИ", "stars": 5},
    {"id": 3, "product": "Планшет", "stars": 5},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 4, "product": "Колонка", "stars": 4},
    {"id": 5, "product": "Кабель", "stars": 1},
]


for i in reviews:
    i['product'] = i['product'].lower()

stars_sum = {}
cnt = {}
for i in reviews: 
    product = i['product']

    if product not in stars_sum: 
        stars_sum[product] = 0
        cnt[product] = 0

    stars_sum[product] += i['stars']
    cnt[product] += 1

average_stars = {}
for product in stars_sum:
    average_stars[product] = stars_sum[product] / cnt[product]

print("1. cредняя оценка каждого товара:")
for product, average in average_stars.items():
    print(f"{product} - {average}")

products_two_reviews = {}
for product, average in average_stars.items():
    if cnt[product] >= 2:
        products_two_reviews[product] = average

worst_product = min(products_two_reviews, key=products_two_reviews.get)
print()
print(f"2. худший товар по средней оценке среди тех, у кого хотя бы два отзыва: {worst_product}")
print()
bad_reviews_count = 0
for review in reviews:
    if review["stars"] == 1 or review["stars"] == 2:
        bad_reviews_count += 1

print(f"3. сколько отзывов на 1 или 2 звезды: {bad_reviews_count}")
print()
print(f"4. какую долю всех отзывов они составляют: {bad_reviews_count / len(reviews)}") 

