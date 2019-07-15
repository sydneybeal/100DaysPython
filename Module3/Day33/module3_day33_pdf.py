"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module3_day33_pdf.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

from tabula import read_pdf
import csv
import os

census = read_pdf("MontcoCensus.pdf")
census.to_csv("census_temp.csv", mode="w", sep="|", index=False)

csv.register_dialect("pipe-delim", delimiter="|", lineterminator="\n")

with open("census_temp.csv", "rt") as census_in, open("census_20100401.csv", "wt") as census_out:
    writer = csv.writer(census_out, delimiter="|", lineterminator="\n")
    writer.writerow(("age", "both_sexes", "male", "female"))
    for row in csv.reader(census_in, dialect="pipe-delim"):
        if row[0] == "Unnamed: 0" or row[0] == "":
            continue
        else:
            writer.writerow([row[0], row[2], row[3], row[4]])

os.remove("census_temp.csv")
