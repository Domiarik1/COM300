order_value = 50
distance = 12
if distance <= 10:
    delivery_fee = 0
elif distance <= 20:
    delivery_fee = 10
elif distance <= 30:
    delivery_fee = 15
else:
    delivery_fee = 20

def calculate_delivery_fee(distance):
    if distance <= 10:
        return 0
    elif distance <= 20:
        return 10
    elif distance <= 30:
        return 15
    else:
        return 20
order_fee = float(input("Enter order value: (50) "))
distance = float(input("Enter delivery distance (: (12) "))

delivery_fee = calculate_delivery_fee(distance)
total_cost = (order_fee + delivery_fee)


print(f"The cost of delivery is {delivery_fee}")


def calculate_delivery_fee(order_value, distance):

    if order_value > 100 and distance <= 10:
        return 0
    if distance <= 10:
        return 5
    elif distance <= 20:
        return 10
    elif distance <= 30:
        return 15
    else:
        extra_miles = distance - 30
        return 15 + (extra_miles + 0.5)

order_value = float(input("Enter order value: (100) "))
distance = float(input("Enter delivery distance (: (30) "))

delivery_fee = calculate_delivery_fee(order_value, distance)
total_cost = order_value + delivery_fee

print(f"The cost of delivery is {delivery_fee}")