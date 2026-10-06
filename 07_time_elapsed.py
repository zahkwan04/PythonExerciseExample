"""Reaction Time Tester - Measure user reaction time."""

import time
import random


if __name__ == "__main__":
    print("Get ready...")
    time.sleep(random.randint(2, 5))

    start = time.perf_counter()
    user_input = input("PRESS ENTER NOW! ")

    if user_input == "":
        reaction_time = time.perf_counter() - start
        print(f"Your reaction time: {reaction_time:.3f} seconds")
        if reaction_time <= 0.5:
            print("F1 DRIVER LEVEL!")
        elif reaction_time <= 1:
            print("Meh okay. not the best")
        elif reaction_time <= 2:
            print("Go to sleep old man")
        else:
            print("damn go play roblox or something")
    else:
        print("bro slow 💀")
