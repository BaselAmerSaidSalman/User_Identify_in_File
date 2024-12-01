import time
import string

# User_Name
name = input("Please enter your name: ")
while name[0] in string.digits:  
  print("Please enter the right input")
  name = input("Please enter your name: ")

# User_Age
while True:
  try:
    age = int(input("Please enter your age: "))
    while age <= 0:
      print("Age cannot be 0 or less")
      age = int(input("Please enter your age: "))
    break
  except ValueError:
    print("Please enter the right input")

# User_Gender
nationality = input("Please enter your nationality: ")
while nationality[0] in string.digits:  
  print("Please enter the right input")
  nationality = input("Please enter your nationality: ")


# User_Identify_File_Code
f = open("User Identify. txt" , "w")
f.write(f"My name is {name}\nI'm {age} years old\nI'm {nationality}")

f = open("User Identify. txt" , "r")
print(f"\n{f.read()}")
f.close()
time.sleep(2)

