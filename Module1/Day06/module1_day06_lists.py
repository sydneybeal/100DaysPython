"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day06_lists.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

list_1 = []
list_2 = list()

print("List 1 Type: {}\nList 2 Type: {}".format(type(list_1), type(list_2)))

text = "Luggage Combination"
print(list(text))

luggage = [1, 3, 5, 2, 4]
luggage.sort()
print(luggage)

numbers = [1, 2, 3, 4, 5]
numbers_sorted = numbers
numbers_sorted.sort(reverse=True)
print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))

numbers = [1, 2, 3, 4, 5]
numbers_sorted = list(numbers)
numbers_sorted.sort(reverse=True)
print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))

odd = [1, 3, 5]
even = [2, 4]
luggage = odd + even
print(luggage)

luggage = [1, 3, 5]
even = [2, 4]
luggage.extend(even)
print(luggage)

odd = [1, 3, 5]
even = [2, 4]
luggage = odd + even
print("Unsorted list: {}".format(luggage))
print("Using the sorted() function: {}".format(sorted(luggage)))
luggage.sort()
print("Using the .sort() method: {}".format(luggage))

lines = []
lines.append("They told me to comb the desert, so I'm combing the desert")
lines.append("YOGURT! I hate Yogurt! Even with strawberries!")
lines.append("We'll meet again in Spaceballs 2: The Quest for More Money.")
print(lines)

luggage = [1, 2, 3, 4, 5]
print(luggage.index(2))

quote = list("YOGURT! I hate Yogurt! Even with strawberries!")
print(quote)
print(quote.count("r"))

luggage = [1, 2, 4, 5]
luggage.insert(2, 3)
print(luggage)

luggage = [1, 2, 3, 3, 4, 5, 6]
print(luggage.pop())
print(luggage)
print(luggage.pop(2))
print(luggage)

countdown = [5, 4, 3, 2, 1]
countdown.reverse()
countdown

sample = list(range(1,13))
times_12 = [i * 12 for i in sample]
print(times_12)

luggage.clear()
print(luggage)

luggage = [2, 2, 3, 4, 5]
luggage[0] = 1
print(luggage)