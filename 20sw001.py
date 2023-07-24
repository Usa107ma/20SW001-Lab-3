 
**Task 1**
"""

points = 134

result = ""

if points >= 1 and points <= 50:
    result = "wooden rabbit"
elif points > 50 and points <= 150:
    result = "no prize"
elif points > 150 and points <= 180:
    result = "water-thin mint"
elif points > 180 and points <= 200:
    result = "penguin"
else:
    result = "error"

print(result)

"""**Task 2**"""

answer = 52
guess = int(input("Enter your guess: "))
if guess < answer:
    result = "Oops! Your guess was too low."
elif guess > answer:
    result = "Oops! Your guess was too high."
else:
    result = "Nice! Your guess matched the answer!"

print(result)

"""**Task 3**"""

tax_rates = {
    "CA": 0.075,  # 7.5%
    "MN": 0.095,  # 9.5%
    "NY": 0.089,  # 8.9%
}

amount_of_purchase = float(input("Enter the amount of the purchase: "))
state = input("Enter the state (CA, MN, or NY): ")

if state in tax_rates:
    tax_rate = tax_rates[state]
    tax_amount = amount_of_purchase * tax_rate
    total_amount = amount_of_purchase + tax_amount

    print(f"Tax amount: ${tax_amount:.2f}")
    print(f"Total amount including tax: ${total_amount:.2f}")
else:
    print("Invalid state. Please enter CA, MN, or NY.")

"""**Task 4**"""

sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
for word in sentence:
  print(word)

"""**Task 5**"""

for i in range (1, 30):
  if i%5==0 :
    print(i)

"""**Task 6**"""

names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
first_names = names[0]

print(first_names)

"""**Task 7**"""

multiples_3 = [i * 3 for i in range(1, 20)]

# Print the list
print(multiples_3)

"""**Task 8**"""

scores = {
    "Rick Sanchez": 70,
    "Morty Smith": 35,
    "Summer Smith": 82,
    "Jerry Smith": 23,
    "Beth Smith": 98
}

passed = [name for name, score in scores.items() if score >= 65]

print(passed)

"""**Task 9**"""

cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
cast_heights = [72, 68, 72, 66, 76]

# Using zip to combine the lists and then converting to a dictionary
cast = dict(zip(cast_names, cast_heights))

print(cast)

"""**Task 10**"""

cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
heights = [72, 68, 72, 66, 76]

# Using enumerate to modify each element in the cast list
for index, name in enumerate(cast):
    height = heights[index]
    cast[index] = f"{name} {height}"

print(cast)