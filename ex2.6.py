seasons = ("Winter", "Spring", "Summer", "Autumn")

month = int(input("Enter the number of the month (1-12): "))

season_index = (month % 12) // 3
print(f"The season is {seasons[season_index]}.")