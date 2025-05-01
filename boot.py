import os 
import time 

def boot():
    print("Booting PseduOS...")
    time.sleep(3)
    print("Booted into PseudoOS")
    time.sleep(3)
    return '-------------------------------------------'

# Directly print the welcome message
print("Welcome to PseduOS")

# Call the boot function without any arguments
boot()

