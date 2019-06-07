"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module1_day08_tuples.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

theme = "East", "Bound", "Down"
print(type(theme))
print(theme)
good = ("Bandit", "Frog", "Snowman")
print(type(good))
print(good)

return_trip = "West", theme[1], theme[2]
print(return_trip)

movie = ("Smokey and the Bandit", 1977, "Hal Needham", ("Burt Reynolds", "Sally Field", "Jerry Reed"))
title, year, director, stars = movie
bandit, frog, snowman = stars
print("Title: {}\nYear: {}\nDirector: {}".format(title, year, director))
type(stars)
print("Stars: {}\nBandit: {}\nFrog: {}\nSnowman: {}".format(stars, bandit, frog, snowman))

movie_list = ("Smokey and the Bandit", 1977, "Hal Needham", ["Burt Reynolds", "Sally Field", "Jerry Reed"])
title, year, director, cast = movie_list
type(cast)
print(cast)
cast.append("Jackie Gleason")
print(cast)

del movie_list