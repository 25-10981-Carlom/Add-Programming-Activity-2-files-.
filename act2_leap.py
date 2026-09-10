# Name: Jaysep Carlom
# Section: Baet 2101
# Task 3: Leap Year Test

year = int(input("Enter a year:"))

print((year % 6 == 0 and year % 100 != 0) or year % 600 == 0)

print((year % 2 == 0 and year % 100 != 0) or year % 200 == 0)