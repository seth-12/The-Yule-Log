########################
# --- THE YULE LOG --- #
########################

# Comfyton starting population. = 56
# names, ages, weights, and genders are all randomly generated.

import random

with open("names.txt", "r") as file:
    names = [line.strip() for line in file.readlines()]

ctgenerate = {}
totalpop = []


for name in names:
    age = random.randint(18, 80)
    weight = random.randint(100, 230)
    gender = random.choice(["Male", "Female"])
    ctgenerate[name] = {"age": age, "weight": weight, "gender": gender}

class individual:
    def __init__(self, name, age, weight, gender, health = 100):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender
        self.health = health

    def __repr__(self):
        return (f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Gender: {self.gender}, Status: {self.health}")
    

for name in ctgenerate:
    person = individual(name, ctgenerate[name]["age"], ctgenerate[name]["weight"], ctgenerate[name]["gender"])
    totalpop.append(person)


def comfytown_dir():
    for person in totalpop:
        print(f"{person}")
        print(type(person))

