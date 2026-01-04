# Your original welcome message, cleaned up a bit
print("---------------------------------")
print("   Welcome to Calorie Tracker")
print("---------------------------------\n\n")
print("This program helps you track your daily calorie consumption.\n")

meal_names = []
calories = []

num_meals_input = input("How many meals do you want to log? \n")
num_meals = int(num_meals_input)

for i in range(num_meals):
    print(f"\n--- Entering Meal #{i + 1} ---")
    
    m_name = input("Enter meal name (e.g., Breakfast, Lunch): ")
    
   
    c_amount_input = input(f"Enter calories for {m_name} (whole number): ")
    c_amount = int(c_amount_input)

    meal_names.append(m_name)
    calories.append(c_amount)

print("\nAll meals entered. Calculating summary...")


total_calories = 0
average_calories = 0


if len(calories) > 0:
    total_calories = sum(calories)
    average_calories = float(total_calories) / float(len(calories))

daily_limit_input = input("\nWhat is your daily calorie limit (whole number)? ")
daily_limit = int(daily_limit_input)




print("\n--- Your Daily Calorie Report ---")
print("Meal Name\t\tCalories")
print("---------------------------------")

for i in range(len(meal_names)):
    print(f"{meal_names[i]}\t\t\t{calories[i]}")

print("---------------------------------")
print(f"Total:\t\t\t{total_calories}")
print(f"Average:\t\t{average_calories}")
print("---------------------------------")


if total_calories > daily_limit:
    print(f"!!! WARNING: You are {total_calories - daily_limit} calories OVER your limit of {daily_limit}.")
else:
    print(f"Success! You are {daily_limit - total_calories} calories UNDER your limit of {daily_limit}.")
print("---------------------------------")



print("\nThank you for using Calorie Tracker. Goodbye!")