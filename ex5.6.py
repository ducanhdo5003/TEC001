def remove_odds(numbers):
    return [num for num in numbers if num % 2 == 0]

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 20]
even_list = remove_odds(original_list)

print(f"Original list: {original_list}")
print(f"Cut-down list: {even_list}")