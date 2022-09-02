import time
import random
from pynput.keyboard import Controller
keyboard = Controller()
def type_string_with_delay(string):
    for character in string:
        keyboard.type(character)
        delay = random.uniform(0, 0.4)
        time.sleep(delay)
txt1 = input("Enter file name: ")
file = open(txt1, 'r')
print("5 second delay....")
time.sleep(5)
type_string_with_delay(file.read())
print("Done!")
