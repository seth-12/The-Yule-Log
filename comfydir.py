

import streamlit as st
import pandas as pd
import random
from pathlib import Path
from config import render_markdown_with_static_images as render_images
from config import config as cfg


cfg()

class Individual:
    def __init__(self, name, age, weight, gender, health=100):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender
        self.health = health

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Status: {self.health}"

def generate_comfytown_population():
    """
    Reads names from a file and returns a dictionary of Individual objects
    with random attributes.
    """
    population_dict = {}

    with open("names.txt", "r") as file:
        for line in file:
            name = line.strip()

            if not name:
                continue

            age = random.randint(18, 80)
            weight = random.randint(100, 230)
            gender = random.choice(["Male", "Female"])
            
            new_person = Individual(name, age, weight, gender)
            
            population_dict[name] = new_person

    return population_dict


population_dict = generate_comfytown_population()

df = pd.DataFrame(
    [
       {"Command": "st.data_editor", "Rating": 5, "Is Cool": True},
       {"Command": "st.dataframe", "Rating": 4, "Is Cool": True},
    ]
)

# 3. Use the edited data
st.write("Current data in the spreadsheet:")
st.dataframe(df)