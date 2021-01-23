# Write your code here
import random

options = ["rock", "paper", "scissors"]
user_points = {}


def read_file():
    file = open("rating.txt", "r")
    for line in file:
        components = line.split(" ")
        user_points[components[0]] = int(components[1])


def has_win(choice, opponent_choice):
    assert choice in options
    assert opponent_choice in opponent_choice

    position = options.index(choice)
    other_options = options[position + 1:] + options[:position]

    opponent_position = other_options.index(opponent_choice)
    if opponent_position < len(other_options) / 2:
        return False
    else:
        return True


if __name__ == '__main__':

    read_file()

    name = input("Enter your name: ")

    print(f"Hello, {name}")

    rating = 0
    if name in user_points.keys():
        rating = user_points[name]

    options_input = input()
    if len(options_input.strip()) > 0:
        options = options_input.split(",")
    print("Okay, let's start")

    while True:
        user_input = input()
        computer_choice = random.choice(options)

        if user_input == "!exit":
            print("Bye!")
            break
        elif user_input == "!rating":
            print(f"Your rating: {rating}")
        elif user_input not in options:
            print("Invalid input")
        elif user_input == computer_choice:
            rating += 50
            print(f"There is a draw ({computer_choice})")
        elif has_win(user_input, computer_choice):
            rating += 100
            print(f"Well done. The computer chose {computer_choice} and failed")
        else:
            print(f"Sorry, but the computer chose {computer_choice}")
