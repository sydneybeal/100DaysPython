"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day15_dictionaries.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

conversion = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(conversion)
print(conversion["a"])

menu = {"item1": ["egg", "spam", "bacon"],
        "item2": ["egg", "sausage", "spam"],
        "item3": ["egg", "spam"],
        "item4": ["egg", "bacon", "spam"],
        "item5": ["egg", "bacon", "sausage", "spam"],
        "item6": ["spam", "bacon", "sausage", "spam"],
        "item7": ["spam", "egg", "spam", "spam", "bacon", "spam"],
        "item8": ["spam", "egg", "sausage", "spam"]}
print(menu["item1"])
print(type(menu["item7"]))

menu["item2"][2] = "spam"
print(menu["item2"])

# List Comparison
l_ministry1 = ["silly", "walks"]
l_ministry2 = ["walks", "silly"]
print(l_ministry1 == l_ministry2)

# Dictionary Comparison
d_ministry1 = {"a": "silly", "b": "walks"}
d_ministry2 = {"b": "walks", "a": "silly"}
print(d_ministry1 == d_ministry2)


print(menu.keys())
print(menu.values())

ordered_keys = list(menu.keys())
print(ordered_keys)
ordered_keys.sort(reverse=True)
print(ordered_keys)

menu_tuple = tuple(menu.items())
print(menu_tuple)
print(type(menu_tuple))
print(menu_tuple[0])
print(type(menu_tuple[0]))

# Slicing the key/value tuple to obtain the key.
print(menu_tuple[0][0])
print(type(menu_tuple[0][0]))

# Slicing the key/value tuple to obtain the value.
print(menu_tuple[0][1])
print(type(menu_tuple[0][1]))

# Slicing the second item in the value list.
print(menu_tuple[0][1][1])
print(type(menu_tuple[0][1][1]))

print(menu["item1"][1])
print(menu_tuple[0][1][1] == menu["item1"][1])

order = "item9"
if menu.get(order, 0) == 0:
    print("{} is not a valid dish. Please try again.".format(order))
else:
    print("{} contains {}".format(order, menu.get(order)))

transportation = {"name": "coconut", "color": "brown"}
print(transportation.items())
transportation.setdefault("received_by", "swallow")
print(transportation.items())
transportation.setdefault("received_by", "found_on_ground")
print(transportation.items())