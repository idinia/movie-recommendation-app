total_rating = 0

for i in range(1, 6):
    rating = float(input(f"Please enter rating {i} (0 - 5): "))
    total_rating += rating

average_rating = total_rating / 5
print(f"Average rating: {average_rating}")