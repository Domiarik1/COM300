# Capacity = 30
# num_students = 28
# room_booked = False
# computers_required = True
# num_computers = 25
#
# if room_booked:
#     print("Room is already booked")
# elif num_students > Capacity:
#     print("Not enough space in the room")
# elif computers_required and num_computers < num_students:
#     print("Not enough computers")
# else:
#     print("Room booking allowed.")
#
# while True:
#     hours = float(input("Enter hours parked (or -1 to quit: "))
#     if hours == -1:
#         print("Not enough hours")
#     if hours < 0:
#         print("Invalid input. Hours cannot be negative")
#         continue
#     if hours <= 2:
#         cost = hours * 2
#     else:
#         cost = (2 * 2) + ((hours - 2) * 1)
#         print(f"Total cost: £ {cost:.2f}")
#
# rounds = int(input("Enter number of rounds: "))
# score = 0
# for round_num in range(1, rounds + 1):
#     print(f"Round {round_num}:")
#     secret_number = random.randint(1, 10)
#     guessed_correctly = False
#     for attempt in range(1, 6):
#         guess = int(input(f"Attempt the number {attempt}/5 Guess the number (1-10): "))
#
#         if guess <= secret_number:
#             print("Too low")
#         elif guess > secret_number:
#             print("Too high")
#         else:
#             print("Correct!")
#             score += 1
#             guessed_correctly = True
#             break
#     if not guessed_correctly:
#         print(f"Out of attempts! The number was {secret_number}")
# print(f"\nGame over! You guessed correctly in {score} out of {rounds} rounds!")