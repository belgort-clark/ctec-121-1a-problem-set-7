# Module 8
# YOUR NAME MUST BE HERE
# Problem Set No. 7
# Problem 1

import string
from random import *


def generatePassword(passwordLength):
    # string contained all of the possible characters
    possiblePasswordChars = string.ascii_letters + string.digits + "!$%^*/?-&"

    password = ""
    for i in range(passwordLength):
        randomNumber = randrange(0, len(possiblePasswordChars) - 1)
        # YOUR CODE GOES BELOW THIS COMMENT: get a single character from the string using the randomNumber generated

        # YOUR CODE GOES BELOW THIS COMMENT: use accumulator pattern to create new password

    # send the password back to the caller using return
    return password


def main():

    # open the file to store passwords in for append
    passwordFile =  # Your code goes here
    # how many password to generate
    numPasswords =  # Your code goes here
    # desired length of password
    pwLength = int(input("Desired password length: "))

    # Ensure pwLength is between 8 and 42 inclusively
    # if password is between 8 and 42 then call the generatePassword() function
    if pwLength >= 8 and pwLength <= 42:
        for i in range(numPasswords):
            generatedPassword = generatePassword(pwLength)

            # YOUR CODE GOES BELOW THIS COMMENT: write password to a file with a line feed

        # YOUR CODE GOES BELOW THIS COMMENT: close the file


main()
