
# Instructions:
# 1) The program should start by asking the user to enter his/her name.
user_name = input("Enter your name: ")

# 2) Next, the program should ask the user to enter the amount of his/her salary. Consider that this amount can be a decimal number.
user_salary = float(input("Enter your salary: "))

# 3) Next, the program should ask for the percentage of the bonus received by the user, which can also be a decimal number.
bonus_multiplier = float(input("Enter your bonus multiplier: "))

# 4) The calculation of the 2024 bonus KPI is 1000 + salary * bonus
bonus_constant = 1000

kpi = bonus_constant + (user_salary * bonus_multiplier)

# 5) Finally, the program should print a message in the following format: "Hello [name], your bonus amount was 5000".
print(f"Heelo {user_name}, your bonus amount was {kpi}")



