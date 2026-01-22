import math
def calculate_unit_price(diameter_cm, price_usd):
    radius_cm = diameter_cm / 2
    radius_m = radius_cm / 100
    area_m2 = math.pi * (radius_m ** 2)
    unit_price = price_usd / area_m2
    return unit_price

def main():
    d1 = float(input("Enter the diameter of Pizza 1: "))
    p1 = float(input("Enter the price of Pizza 1: "))
    d2 = float(input("Enter the diameter of Pizza 2: "))
    p2 = float(input("Enter the price of Pizza 2: "))
    a = calculate_unit_price(d1, p1)
    b = calculate_unit_price(d2, p2)
    print("Pizza 1 costs $", a, "per square meter.")
    print("Pizza 2 costs $", b, "per square meter.")
    if a < b:
        print("Result: Pizza 1 provides better value for money!")
    elif b < a:
        print("Result: Pizza 2 provides better value for money!")
    else:
        print("Result: Both pizzas have the same value.")
main()