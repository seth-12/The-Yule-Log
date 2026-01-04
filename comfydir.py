import streamlit as st
import random
from pathlib import Path
from config import render_markdown_with_static_images as render_images
from config import config as cfg
import json

# cfg()

class Individual:
    def __init__(self, name, age, weight, gender, age_class, health = 100):
        self.name = name
        self.age = age
        self.weight = weight
        self.gender = gender
        self.health = health
        self.age_class = age_class

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
            #age logic 
            if age <= 18:
                age_class = "young"
            elif 18 < age <= 36:
                age_class = "adult"
            elif 36 < age <= 55:
                age_class = "middle age"
            elif 55 < age <= 74:
                age_class = "old"
            elif 74 < age <= 100:
                age_class = "elderly"
            
            weight = random.randint(100, 230)
            gender = random.choice(["Male", "Female"])
            
            new_person = Individual(name, age, weight, gender, age_class)
            
            population_dict[name] = new_person

    return population_dict


if "population" not in st.session_state:
    st.session_state.population = generate_comfytown_population()
population_dict = st.session_state.population


###########
# Page UI #
###########

st.title("Comfyton Directory")

st.divider()

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
    random_obj = random.choice(list(population_dict.values()))
    st.write(random_obj)
    random_obj.health -= 10
    st.write("After damage:")
    st.write(random_obj)


if st.button("Reload"):
    st.rerun()




aja_obj = population_dict["Aja"]
print(aja_obj)
print(aja_obj.age_class)


# 1. Convert session state to a standard dictionary
# We use a dict comprehension to ensure we're working with a serializable copy
state_dict = {key: value for key, value in st.session_state.items()}

# 2. Save to a JSON file
if st.button("Save Session State"):
    try:
        with open("session_state.json", "w") as f:
            json.dump(state_dict, f, indent=4)
        st.success("State saved successfully!")
    except TypeError as e:
        st.error(f"Failed to save: Some objects are not JSON serializable. Error: {e}")