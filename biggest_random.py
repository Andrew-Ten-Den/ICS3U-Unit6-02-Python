#!/usr/bin/env python3

# Created by: Andrew-Ten-Den
# Created on: June 2022
# This program finds the largest of 10 random numbers

import random


def main():

    random_numbers = []

    loop_counter = 0
    biggest = 0
    # input
    print("Here are the 10 numbers:")

    while loop_counter < 10:
        random_variable = random.randint(0, 100)
        random_numbers.append(random_variable)
        if random_variable > biggest:
            biggest = random_variable

        loop_counter = loop_counter + 1
    print("")
    print(random_numbers)
    print("The biggest of these 10 numbers is {}".format(biggest))

    print("\n\nDone.")


if __name__ == "__main__":
    main()
