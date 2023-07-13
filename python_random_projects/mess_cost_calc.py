# Static params:
total_house_rent  = 19500
gas_bill          = 1080
cook_bill         = 3500
electricity       = 1500
internet          = 1000
cleaner           = 100
house_rent = [2000, 2000, 1667, 1667, 1667, 1833, 1833, 1833, 2500, 2500]

# Get Name:
def getName(number):
    if number == 0: return "sumon  "
    if number == 1: return "sohel  "
    if number == 2: return "joy    "
    if number == 3: return "shopnil"
    if number == 4: return "sourav "
    if number == 5: return "shawon "
    if number == 6: return "arfin  "
    if number == 7: return "mehedi "
    if number == 8: return "mejbah "
    if number == 9: return "sayem  "

# User inputs:==================================================================
no_of_member = int(input("No of Member     : "))
# Meal Input:
meals = []
print("Number of Meal   :")
for member_no in range(no_of_member):
    member_name = getName(member_no)
    meals.append(float(input(f"   > {member_name}: ")))

# Personal Bazar
personal_bazar = []
print("Personal Bazar   :")
for member_no in range(no_of_member):
    member_name = getName(member_no)
    personal_bazar.append(float(input(f"   > {member_name}: ")))

# Previous Balance
previous_balance = []
print("Previous Balance :")
for member_no in range(no_of_member):
    member_name = getName(member_no)
    previous_balance.append(float(input(f"   > {member_name}: ")))

extra_cost = float(input("Extra Cost       : "))
big_bazar_deposit = int(input("Big Bazar Deposit: "))
rest = float(input("Rest             : "))
opening_balance = float(input("Opening balance  : "))
closing_balance = float(input("Closing balance  : "))
big_bazar_expense = float(input("Big Bazar Expense: "))

# Calculation===================================================================
total_meal   = sum(meals)
personal_bazar_expense = sum(personal_bazar)
# Utility Calculation:===================
total_utility = gas_bill+cook_bill+electricity+internet+cleaner
per_utility = total_utility/no_of_member
# Adjustment Calculation:================
adv_deposit = big_bazar_deposit*no_of_member
total_adjustment = ((adv_deposit+opening_balance) - (rest+closing_balance)) + rest
per_adjustment = total_adjustment/no_of_member
# Meal Cost Calculation:=================
total_bazar_cost = big_bazar_expense + extra_cost + personal_bazar_expense
per_meal_cost = total_bazar_cost/total_meal
meal_cost = []
for meal in meals: meal_cost.append(round(meal * per_meal_cost))
total_meal_cost = sum(meal_cost)
# Gross Payable Calculation:=============
gross_payable = []
for i in range(no_of_member):
    gross_payable.append(round(((house_rent[i] + per_utility + meal_cost[i] + big_bazar_deposit) - (personal_bazar[i] + per_adjustment)) - (rest/no_of_member)))


# Showing the details===========================================================
print(f"Personal Bazar   : {personal_bazar_expense}")
print(f" > Total Bazar   : {total_bazar_cost}")
print(f" > Per Meal Cost : {'{:0.2f}'.format(per_meal_cost)}")
print(f" > Utility       : {per_utility}")
print(f" > Adjustment    : {per_adjustment}")


# Show the Meals: ====================================================
print("\n")
for number in range(no_of_member):
    print(f"Members: {getName(number)}", sep=',')
    print(f"No of Meal: {meals[number]}")
# print("                  sumon | sohel |  joy  |shopnil|sourav |shawon | arfin |mehedi |mejbah | sayem | = Total")
# print(f"no_of_meal    => {meals[0]} |{meals[1]} |{meals[2]} |{meals[3]} |{meals[4]} |{meals[5]} |{meals[6]} |{meals[7]} |{meals[8]} |{meals[9]} | = {total_meal}")
# print(f"meal_cost     => {meal_cost[0]} |{meal_cost[1]} | {meal_cost[2]} |{meal_cost[3]} |{meal_cost[4]} |{meal_cost[5]} |{meal_cost[6]} |{meal_cost[7]} |{meal_cost[8]} |{meal_cost[9]} | = {total_meal_cost}")
# print(f"gross_payable => {gross_payable}")
# print(f"prev_balance  => {previous_balance[0]}  |{previous_balance[1]}  | {previous_balance[2]} |  {previous_balance[3]} | {previous_balance[4]}  | {previous_balance[5]}  | {previous_balance[6]} | {previous_balance[7]}  | {previous_balance[8]} |{previous_balance[9]}|")
# print(f"net_payable   => ")