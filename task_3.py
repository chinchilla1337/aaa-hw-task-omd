# Нужно найти:

# - на какую сумму оформили возвраты
# - кто хотя бы раз вернул заказ
# - сколько заказов доставлено покупателю
# - средний чек доставленных заказов

orders = [
    {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
    {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
    {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
    {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
    {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
    {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
]

returned_amt = 0
buyers_w_return = set()
delivered_cnt = 0
delivered_amt = 0

for o in orders:
    if o["status"] == "returned":
        returned_amt += o["amount"]
        buyers_w_return.add(o["buyer"])

    if o["status"] == "delivered":
        delivered_cnt += 1
        delivered_amt += o["amount"]

avg_ch = delivered_amt / delivered_cnt

print(f"1. сумма возвратов: {returned_amt}")
print(f"2. кто хотя бы раз вернул заказ: {buyers_w_return}")
print(f"3. количество доставленных заказов: {delivered_cnt}")
print(f"4. средний чек доставленных заказов: {avg_ch}")