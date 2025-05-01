import pyfiglet
import time
from login import login
from boot import boot
from env import env
import sys  # Import sys for exit

# Use a different font if "doh" is not available
splash_scrn = pyfiglet.figlet_format("PseduOS", font="slant")  # Change font if needed
print(splash_scrn)
time.sleep(3)

print("Choose from the following:  ")
print("a. Boot PseduOS")
print("b. Exit")

u = input("Your choice: ")

# Corrected logical condition
if u.lower() == 'a':  # This will check for both 'a' and 'A'
    print("Welcome to PseduOS...")
    print(boot())
    time.sleep(2)

    print("Loading login Screen... ")
    time.sleep(1)
    print(login())
    print("Logging in... ")
    time.sleep(1)

    print("Loading Environment... ")
    time.sleep(2)
    print(env())
else:
    sys.exit()  # Use sys.exit() to exit the program

