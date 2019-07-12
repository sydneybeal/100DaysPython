"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module3_day31_csv.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

import csv

actor = ["Alan Alda", "Loretta Swit", "Jaime Farr", "William Christopher", "Larry Linville", "Mike Farrell",
         "Gary Burghoff"]
character = ["Captain Benjamin Franklin 'Hawkeye' Pierce", "Major Margaret 'Hot Lips' Houlihan",
             "Corporal Maxwell Q Klinger", "Father Francis Mulcahy", "Major Frank Burns", "Captain B.J. Hunnicutt",
             "Corporal Walter 'Radar' O'Reilly"]
episodes = [251, 251, 216, 213, 121, 179, 177]

mash = open("mash_pipe.csv", "wt")
try:
    writer = csv.writer(mash, delimiter="|", lineterminator="\n")
    writer.writerow(("actor", "character", "episodes"))
    for i in range(len(actor)):
        writer.writerow((actor[i], character[i], episodes[i]))
    writer.writerow(("This includes a, comma", "How will that affect, it?", "This normally contains integers"))
finally:
    mash.close()

mash = open("mash.tsv", "wt")
try:
    writer = csv.writer(mash, delimiter="\t", lineterminator="\n")
    writer.writerow(("actor", "character", "episodes"))
    for i in range(len(actor)):
        writer.writerow((actor[i], character[i], episodes[i]))
    writer.writerow(("This includes a, comma", "How will that affect, it?", "This normally contains integers"))
finally:
    mash.close()

csv.register_dialect("pipe-delim", delimiter="|", lineterminator="\n")

with open("mash_pipe.csv", "rt") as mash_in, open("mash.csv", "wt") as mash_out:
    writer = csv.writer(mash_out, lineterminator="\n")
    for row in csv.reader(mash_in, dialect="pipe-delim"):
        if row[0] == "This includes a, comma":
            continue
        else:
            writer.writerow(row)