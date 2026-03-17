position = int(input("Please enter a number between 1-20: "))
for i in range(1, 21):

    if i == position:
        print("X", end="")
    else:
        print("-", end="")

position = int(input("Please enter a number between 1-20: "))

if position < 1 or position > 20:
    print("sorry, the number needs to be between 1 and 20")
else:
    for i in range(1, 21):
        if i == position:
            print("X", end="")
        else:
            print("-", end="")