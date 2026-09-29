# import timeit
# import time
# import random

# # exec_time = timeit.timeit("print('Hello World!')", number=5)
# # print(exec_time, "secs")

# if __name__ == "__main__":    
#     print("ready to press Enter!")
#     time.sleep(random.randint(2,10))
#     start = time.process_time()
#     user_input = input("press the button now!")
#     if user_input == "":
#         print(time.process_time() - start)
#     else:
#         print("bro slow")

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
        elif reaction_time <= 1 and reaction_time > 0.5:
            print("Meh okay. not the best")
        elif reaction_time <= 2 and reaction_time > 1:
            print("Go to sleep old man")
        else:
            print("damn go play roblox or something")
    else:
        print("bro slow 💀")