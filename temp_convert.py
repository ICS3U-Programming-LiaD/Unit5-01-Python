#!/usr/bin/env python3
# Created by: Lia Duggan
# Created on: Nov.22nd, 2022
# This program coverts celsius to fahrenheit


def fahrenheit():
    try:
        # Gets the temperature in celsius from the user
        user_celsius = float(input("Enter the temperature in celsius: "))
    # Converts celsius to fahrenheit
    except ValueError:
        print("Please enter a number")
    else:
        fahrenheit = (9 / 5) * user_celsius + 32
        # Displays the user input and the converted temperature
        print("{}℃ is equal to {}℉".format(user_celsius, fahrenheit))


def main():

    fahrenheit()

if __name__ == "__main__":
    main()