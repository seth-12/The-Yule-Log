

import streamlit as st
import pandas as pd
import random
from pathlib import Path
from config import render_markdown_with_static_images as render_images
from config import config as cfg


# cfg()

class Individual:
    def __init__(self, name, age, weight, gender, health=100):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender
        self.health = health

    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Status: {self.health}"

@st.cache_data
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


col1, col2, col3, col4, col5 = st.columns(5)

with col2:
    st.write("Name")
with col3:
    st.write("Age")
with col4:
    st.write("Gender")
with col5:
    st.write("Status")

st.divider()

col1, col2, col3, col4, col5 = st.columns(5)

count = 0   
for person in population_dict.values():
    count += 1 
    with col1:
        st.write(count)
    with col2:
        st.write(person.name)
    with col3:
        st.write(person.age)
    with col4:
        st.write(person.gender)
    with col5:
        st.write(person.health)


if st.button("test"):
    aja_obj = population_dict["Aja"]
    st.write(aja_obj)