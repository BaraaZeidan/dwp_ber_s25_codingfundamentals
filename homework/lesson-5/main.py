#By using Google, find a function that gives you current date and time and print the current date and time
from datetime import datetime
current_date_and_time = datetime.now()
print ("current date and time is:" + str (current_date_and_time) )
       
# Write a function that counts number of letters in a string you input.
def count_letters (string):
 count = 0
 for x in string:
     count += 1
 print("Number of the letters is:", count)

count_letters("banana")

#return function 

def count_letters (string):
 count = 0
 for x in string:
     count += 1
 return count

print("Number of the letters is:", count_letters ("banana"))


# Create a simple function with two parameters that returns their sum.
def add_two_numbers (number1, number2):
   return number1 + number2
sum_of_the_number = add_two_numbers (3,5)

#Create another function with one parameter that decides if the parameter can be divided by 3 and prints appropriate messages
#Call the second function and use the variable that you created in the b) part as argument.
 
def devide_by_3 (number):
   if number % 3 == 0:
      print (int (number) % 3)
   else:
      print (number,"is not divisible by 3")

devide_by_3 (3)
devide_by_3 (int (sum_of_the_number))