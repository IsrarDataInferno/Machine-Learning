print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")













# age = input("What is your current age?\n")
# # 🚨 Don't change the code above 👆

# #Write your code below this line 👇

# #day 2 video 9
# #int(age)
# print(f"You have {int(age)*365} days, {int(age)*52} weeks, and {int(age)*12} months left.")