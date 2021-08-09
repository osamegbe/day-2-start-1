#Data Types
#Int, flotats, strings and boolians

#string = string of characters strong together . needs double quotes

#subscript - pulling out a particular element from a string. programming starts counting from zero 
# use square brackets to pull out individuals characters
print("Hello"[4])
# if a number is in double quotes then its treated like regular text because of the double quotes 
print("123")

#Integer - for whole number. numbers without decimal places. just write the number without anything else
# _ underscore are seens as comas inprogramming
print (123 + 345)

#float 0 for number that have decimal place

print (3.123)

#boolean - this has two possible values. either True of False - no quotation marks around them
num_char =len(input("What is your name ? "))

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

# for seeing the type check print(type(num_char))

a = float(123)
print (a)

print (type(a))