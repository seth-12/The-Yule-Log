

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

            age = random.randint(16, 95)
            weight = random.randint(100, 230)
            gender = random.choice(["Male", "Female"])
            
            new_person = Individual(name, age, weight, gender)
            
            population_dict[name] = new_person

    return population_dict


if "population" not in st.session_state:
    st.session_state.population = generate_comfytown_population()
population_dict = st.session_state.population



###########
# Page UI #
###########

col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14 = st.columns(14)

with col2:
    st.write("Name")
with col3:
    st.write("Age")
with col4:
    st.write("Gender")
with col5:
    st.write("Status")

st.divider()


col1, col2, col3, col4, col5, col6, col7, col8, col9, col10, col11, col12, col13, col14 = st.columns(14)

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
    random_obj = random.choice(list(population_dict.values()))
    st.write(random_obj)
    random_obj.health -= 10
    st.write("After damage:")
    st.write(random_obj)


if st.button("Reload"):
    st.rerun()