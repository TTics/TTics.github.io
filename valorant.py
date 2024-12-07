import random
import time
from inputimeout import inputimeout, TimeoutOccurred
print("welcome to handmade version of valorant")
print("when encountering an enemy, type any key to shoot when 'shoot now' appeared")
input("are you ready?")

pro = [
    {"name": "tenz", "level": "high"},
    {"name": "fns", "level": "slightly low"},
    {"name": "chronicle", "level": "slightly high"},
    {"name": "uno", "level": "low"},
    {"name": "aspas", "level": "high"},
]
def encounter():
    luck = random.randint(0,4)
    enemy = pro[luck]
    return enemy

def fight(enemy):
    if enemy["level"] == "low":
        print("You have 1 seconds to kill " + enemy["name"])
        j = random.randint(1,5)
        time.sleep(j)
        try:
            gay = inputimeout("Shoot now! ", 1)
            print("you killed " + enemy["name"])
        except TimeoutOccurred:
            print(enemy["name"] + " " + "killed you")
            print("game over")
    if enemy["level"] == "slightly low":
        print("You have 0.7 seconds to kill " + enemy["name"])
        j = random.randint(1,5)
        time.sleep(j)
        try:
            gay = inputimeout("Shoot now! ", 0.7)
            print("you killed " + enemy["name"])
        except TimeoutOccurred:
            print(enemy["name"] + " " + "killed you")
            print("game over")
    if enemy["level"] == "medium":
        print("You have 0.5 seconds to kill " + enemy["name"])
        j = random.randint(1,5)
        time.sleep(j)
        try:
            gay = inputimeout("Shoot now! ", 0.5)
            print("you killed " + enemy["name"])
        except TimeoutOccurred:
            print(enemy["name"] + " " + "killed you")
            print("game over")

    if enemy["level"] == "slightly high":
        print("You have 0.35 seconds to kill " + enemy["name"])
        j = random.randint(1,5)
        time.sleep(j)
        try:
            gay = inputimeout("Shoot now! ", 0.35)
            print("you killed " + enemy["name"])
        except TimeoutOccurred:
            print(enemy["name"] + " " + "killed you")
            print("game over")

    if enemy["level"] == "high":
        print("You have 0.2 seconds to kill " + enemy["name"])
        j = random.randint(1,5)
        time.sleep(j)
        try:
            gay = inputimeout("Shoot now! ", 0.2)
            print("you killed " + enemy["name"])
        except TimeoutOccurred:
            print(enemy["name"] + " " + "killed you")
            print("game over")

            
enemy = encounter()
fight(enemy)