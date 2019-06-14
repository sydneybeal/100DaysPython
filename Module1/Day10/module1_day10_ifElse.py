"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day10_ifElse.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

lost = True
if lost:
   print("We're going to need a montage.")


lost = False
if lost:
   print("We're going to need a montage.")
else:
   print("Celebrate by giving Adrian a kiss.")

prompt = input("What do you want to know? Type: 'steps' for number of steps at the Art Museum, 'bouts' for the major fights, or 'job' for Rocky's original job.")
if prompt.lower() == "steps":
   print("You need to run up 72 steps to take a picture with Rocky at the Art Museum in Philadelphia.")
elif prompt.lower() == "bouts":
   print("Rocky (1976): Apollo Creed\nRocky II (1979): Apollo Creed\nRocky III (1982): James 'Clubber' Lang\nRocky IV (1985): Ivan Drago\nRocky V (1990): Tommy Gunn\nRocky Balboa (2006): Mason Dixon")
elif prompt.lower() == "job":
   print("Before becoming a professional boxer, Rocky was nothing but a 'bum' that collected payments for a loan shark.")
else:
   print("{} is not an acceptable entry.".format(prompt))


num = int(input("Select a positive number between 1 and 10: "))
if num > 10:
   print("How can you expect to be the champ if you can't follow directions?")
elif num < 1:
   print("How can you expect to be the champ if you can't follow directions?")
elif num < 3:
   print("Only {} sides of beef? You need to punch more if you plan to be the champ.".format(num))
elif num < 6:
   print("{} sides of beef? That's a good number to punch if you want to be the champ.".format(num))
elif num < 10:
   print("{} sides of beef? Punching that many is a waste. Even if you become the champ, you shouldn't be wasteful.".format(num))
else:
   print("Well, that shouldn't have happened. {} caused an error.".format(num))


awards = input("Which would you like to see, awards won or nominated?")
if awards.lower() == 'won':
   print("Rocky won Oscars for Best Picture, Best Director, and Best Film Editing")
elif awards.lower() == 'nominated':
   movie = input("Which movie do you want to hear about, Rocky or Rocky III?")
   if movie.lower() == 'rocky':
      print("Rocky received Oscar nominations for Best Actor, Best Actress, two Best Supporting Actor, Best Original Screenplay, Best Original Song, and Best Sound.")
   elif movie.lower() == 'rocky iii':
      print("Rocky received Oscar an nomination for Best Original Song.")
   else:
      print("{} is not an acceptable entry.".format(awards))
else:
   print("{} is not an acceptable entry.".format(awards))


reviews = 60
rating = .93 if reviews > 50 else "Not enough reviews"
print("On Rotten Tomatoes, Rocky has a rating: {} with a number of reviews: {}.".format(rating * 100, reviews))