# print("Calorie content for")

print ("Today's Date?")
Date = input()
print ("Breakfast Calories?")
Breakfast_Calories = int(input())
print ("Lunch Calories?")
Lunch_Calories = int(input())
print ("Dinner Calories?")
Dinner_Calories = int(input())
print ("Snack Calories?")
Snack_Calories = int(input())
sum =  Breakfast_Calories + Lunch_Calories + Dinner_Calories + Snack_Calories
# print(sum)

print ("Calorie content for " + Date + ":") + print("Calorie Content for " + Date + ":"+ str(sum))