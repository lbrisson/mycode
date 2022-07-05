

import threading
import os

# what happens when the timer is up!
def consequence():
    print("You took too long! The zombie ate your brains!")
    
    # closes multiple-thread programs
    os._exit(os.EX_OK)

S = threading.Timer(3.0, consequence)
        # sec

# second thread
S.start()
# as of this line, the timer is running!


print("You're trapped in arom wiht zombie")


while True: 
    choice= input("What do you do? \n")

    if(choice.lower() == "run":
            print("you've escaped!")
            S.cancel()
            break


print("You win! You should only see this if you escape the zombie")
