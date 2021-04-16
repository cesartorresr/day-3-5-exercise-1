# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name1_lowercase = name1.lower()
name2_lowercase = name2.lower()


#count the words TRUE and LOVE in the name1 and name 2
true1 = name1_lowercase.count("T".lower()) + name1_lowercase.count("R".lower()) + name1_lowercase.count("U".lower()) + name1_lowercase.count("E".lower()) + name2_lowercase.count("T".lower()) + name2_lowercase.count("R".lower()) + name2_lowercase.count("U".lower()) + name2_lowercase.count("E".lower())

love1 = name1_lowercase.count("L".lower()) + name1_lowercase.count("O".lower()) + name1_lowercase.count("V".lower()) + name1_lowercase.count("E".lower()) + name2_lowercase.count("L".lower()) + name2_lowercase.count("O".lower()) + name2_lowercase.count("V".lower()) + name2_lowercase.count("E".lower())

convert_result_string = str(true1) + str(love1)
convert_again_int = int(convert_result_string)
total = convert_again_int

if total < 10 or total > 90:
  print(f"Your score is {total}, you go together like coke and mentos.")
elif total >= 40 and total <= 50:
  print(f"Your score is {total}, you are alright together.")
else:
  print(f"Your score is {total}")
