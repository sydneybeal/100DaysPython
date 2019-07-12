"""
    Author:         <REPLACE>
    Project:        100DaysPython
    File:           module2_day28_challenge.py
    Creation Date:  <REPLACE>
    Description:    Create a program to encrypt and decrypt messages using a substitution cipher. The user provides a
                    word that does not have any duplicate letters and no numbers or special characters. The user then
                    provides the instruction to either encrypt or decrypt the message. Finally, the user then provides
                    the message to be encrypted or decrypted. Create a function to check if the transposition word is
                    valid, another function to encrypt the message, and a third function to decrypt the message. When
                    encrypting the message, only letters should be provided; do not return any spaces, numbers, or
                    special character. Additionally, the program should not be case sensitive and all output should be
                    in lowercase. Finally, add robust logging to collect insights about the effectiveness of the
                    application.

                    A substitution cipher is created by shifting the letters of the alphabet based on a keyword. For
                    instance, if the word provided is "zebra", the cipher would be:
                    {"a": "z",
                     "b": "e",
                     "c": "b",
                     "d": "r",
                     "e": "a",
                     "f": "c",
                     "g": "d",
                     etc.}
"""

import logging

log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename="module2_day28_challenge.log",
                    level=logging.INFO,
                    format=log_formatter,
                    filemode="w")
logger = logging.getLogger()
logger.setLevel("INFO")


def check_codeword(s):
    logger.info(f"Code word entered: {s}")
    if s == "x":
        logger.info(f"User entered x")
        print("Goodbye.")
        exit(0)
    letters = []
    for i in s:
        if i.lower() in "abcdefghijklmnopqrstuvwxyz":
            if i not in letters:
                letters.append(i)
            else:
                print("Code word contains duplicate letters.")
                logger.info(f"Code word contains duplicate letters.")
                return 0
        else:
            print("Code word contains special characters.")
            logger.info(f"Code word contains special characters.")
            return 0
    logger.info(f"Code word entry successful: {s}")
    return 1


def get_method(s):
    logger.info(f"Method entered: {s}")
    if s[0] == "e":
        logger.info(f"Starts with e --> encrypt")
        r = "encrypt"
    elif s[0] == "d":
        logger.info(f"Starts with d --> decrypt")
        r = "decrypt"
    else:
        logger.info(f"Entry does not start with \'e\' or \'d\'")
        print("Incorrect entry, goodbye.")
        exit(1)
    return r


def get_conversion(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    spill_alphabet = list("abcdefghijklmnopqrstuvwxyz")
    conversion = {}
    for i in range(0, 26):
        if i < len(s):
            conversion[alphabet[i].lower()] = s[i].lower()
            spill_alphabet.remove(s[i])
        elif i == len(s):
            last_index = len(s)
            conversion[alphabet[i].lower()] = spill_alphabet[0].lower()
            spill_alphabet.remove(spill_alphabet[0])
        elif i > len(s):
            for j in spill_alphabet:
                if j not in conversion.values():
                    conversion[alphabet[i].lower()] = j.lower()
                    spill_alphabet.remove(j)
                    break
    print(conversion)
    logger.info(f"Crypto-conversion successful: {conversion}")
    return conversion


def encrypt(s, m):
    conversion = get_conversion(s)
    logger.info(f"Got crypto-conversion")
    ret = ""
    for letter in m:
        if letter.lower() in "abcdefghijklmnopqrstuvwxyz":
            ret += conversion.get(letter.lower())
            logger.info(f"Letter entered: {letter.lower()}\nConversion: {conversion.get(letter.lower())}\nWord now: {ret}")
    return ret


def decrypt(s, m):
    conversion = get_conversion(s)
    logger.info(f"Got crypto-conversion")
    ret = ""
    for letter in m:
        if letter.lower() in "abcdefghijklmnopqrstuvwxyz":
            for key, value in conversion.items():
                if value == letter.lower():
                    ret += key
                    logger.info(
                        f"Letter entered: {letter.lower()}\nConversion: {key}\nWord now: {ret}")
    return ret


status = 0

while status == 0:
    got_word = 0
    while got_word == 0:
        codeword = input("Enter a word with no duplicate letters or special characters (\"x\" to end):\n")
        # codeword = "dogs"
        print(codeword)
        got_word = check_codeword(codeword)
    choice = input("Would you like to encrypt (e) or decrypt (d) the message?\n")
    # choice = "e"
    method = get_method(choice)
    print(method)
    message = input("Enter message to {0}:\n".format(method))
    # message = "Hy my name is Sydney"
    if method == "encrypt":
        converted_msg = encrypt(codeword, message)
        print("Message encrypted: {0}".format(converted_msg))
        logger.info(f"Message successfully encrypted\nCodeword: {codeword}\nMessage: {message}\n"
                    f"Converted message: {converted_msg}")
    elif method == "decrypt":
        converted_msg = decrypt(codeword, message)
        print("Message decrypted: {0}".format(converted_msg))
        logger.info(f"Message successfully decrypted\nCodeword: {codeword}\nMessage: {message}\n"
                    f"Converted message: {converted_msg}")
    else:
        logger.info(f"User error in choosing encrypt or decrypt")
        print("Goodbye.")
