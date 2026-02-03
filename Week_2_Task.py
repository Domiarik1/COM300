# age = int(input("How old are you? "))
# if age <= 0:
#   print("You are old enough to travel.")
#     my_age = 20
# if age == my_age:
#   print("You are old enough to travel.")
# day = int(input(" Enter the day: "))
# month = int(input(" Enter the month: "))
# if day == 1 and month == 4:
#   print("it is April fools day")
# if age >= 18:
#   print("You are old enough to travel.")
# else:
#   print("You are old enough to travel.")

def calculate_discounted_price(price, discount_percent):
    discounted_price = price * (1 - discount_percent / 100)
    return discounted_price

def grade_converter(percentage):
    if percentage >= 70:
      return "First"
    elif percentage >= 60:
      return "Upper-second (2:1)"
    elif percentage >= 50:
      return "Lower-second (2:2)"
    elif percentage >= 40:
      return "Third"
    else:
      return "Refer"