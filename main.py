########################
# --- THE YULE LOG --- #
########################

# Comfyton starting population. = 56
# names, ages, weights, and genders are all randomly generated.

# import random
import streamlit as st

import streamlit as st

pages = {
    "Menu": [
        st.Page("Landing.py", title ="Landing"),
        st.Page("Watchlist.py", title="Watchlist"),
        st.Page("test_page.py", title="Test")
    ],    
}

pg = st.navigation(pages, position="top")
pg.run()

# st.markdown("""
#     <style>
#     /* Apply font to all elements within the main content */
#     * {
#         font-family: 'Noto Serif', serif !important;
#     }

#     /* Set background color for the entire app */
#     .stApp {
#         background-color: #FFFCF5;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# class Individual:
#     def __init__(self, name, age, weight, gender, health=100):
#         self.name = name
#         self.age = age
#         self.weight = weight
#         self.gender = gender
#         self.health = health

#     def __repr__(self):
#         return f"Name: {self.name}, Age: {self.age}, Weight: {self.weight}, Gender: {self.gender}, Status: {self.health}"

# def generate_comfytown_population():
#     """
#     Reads names from a file and returns a dictionary of Individual objects
#     with random attributes.
#     """
#     population_dict = {}

#     with open("names.txt", "r") as file:
#         for line in file:
#             name = line.strip()

#             if not name:
#                 continue

#             age = random.randint(18, 80)
#             weight = random.randint(100, 230)
#             gender = random.choice(["Male", "Female"])
            
#             new_person = Individual(name, age, weight, gender)
            
#             population_dict[name] = new_person

#     return population_dict


# def game_timer():
#     """
#     Game starts on a random day in the year (for season variability)
#     Player can perform any actions to change status and conifgs. Everything sets once the day is over a and a log report is printed
#     """
#     pass
# # This ensures the script runs the menu when started
# if __name__ == "__main__":

#     population_dict = generate_comfytown_population()

#     aja_obj = population_dict["Aja"]
#     print(aja_obj)
#     print(aja_obj.weight)

#     for name in population_dict:
#         print(f"{population_dict[name]}\n")

#     putdlaq_ojb = population_dict["Putdlaq"]
#     print(putdlaq_ojb.health)

#     putdlaq_ojb.health -= 10

#     print(putdlaq_ojb.health)

#     st.title("The Yule Log")
#     st.write(f"{aja_obj}")
    