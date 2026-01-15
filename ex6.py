talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

num1 = (talents * 20 * 32 * 13.3) + (pounds * 32 * 13.3) + (lots * 13.3)

num2 = int(num1 // 1000)
num3 = num1 % 1000

print("The weight:" ,num2 , "kilograms and" , num3, "grams")