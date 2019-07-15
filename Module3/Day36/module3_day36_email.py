"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module3_day36_email.py
    Creation Date:  <REPLACE>
    Description:    <REPLACE>
"""

import smtplib
import os

credentials = dict()

with open("credentials.txt", "r") as cred:
    for line in cred:
        var, val = line.split(": ")
        credentials[var] = val.rstrip("\n")
        var = ""
        val = ""
        line = ""

smtpObj = smtplib.SMTP(f'smtp.{credentials["username"].split("@")[1]}', 587)
smtpObj.ehlo()

smtpObj.starttls()

smtpObj.login(credentials["username"], credentials["password"])

smtpObj.sendmail(credentials["username"], credentials["username"],
                 f"Subject: Automated Email Test\nDear {os.getlogin()},\nThis is a test of the automated email system.")

credentials.clear()

smtpObj.quit()