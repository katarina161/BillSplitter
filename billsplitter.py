import random

# write your code here
num_of_people = int(input("Enter the number of friends joining (including you):\n"))
if num_of_people <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    dinner = {}
    for _ in range(num_of_people):
        dinner[input()] = 0
    # print(dinner)
    total_bill = float(input("Enter the total bill value:\n"))
    each_bill = round(total_bill / num_of_people, 2)
    dinner = {key: each_bill for key in dinner}
    # print(dinner)
    use_lucky_feature = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if use_lucky_feature == "Yes":
        lucky_one = random.choice(list(dinner.keys()))
        print(f"{lucky_one} is the lucky one!")
        each_bill = round(total_bill / (num_of_people - 1), 2)
        dinner = {key: (each_bill if key != lucky_one else 0) for key in dinner.keys()}
    else:
        print("No one is going to be lucky")

    print(dinner)
