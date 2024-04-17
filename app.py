import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load data
data = pd.read_csv('food.csv')
recipe_list = pickle.load(open('recipes_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))
recipes_titles = recipe_list['title'].values  # Assuming 'title' is the column name in your DataFrame

st.header("Recipe Recommendation System")
selected_recipe = st.selectbox("Select a recipe:", recipes_titles)

def recommend(recipe_title):
    index = recipe_list[recipe_list['title'] == recipe_title].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_recipes = []
    for i in distance[1:6]:  # Get top 5 recommendations
        recommended_recipes.append(recipe_list.iloc[i[0]])
    return recommended_recipes

if st.button('Get Recommendations'):
    recommendations = recommend(selected_recipe)
    st.write('**Recommended Recipes:**')
    for rec in recommendations:
        st.write(f"**Recipe Name:** {rec['title']}")
        st.write(f"**Required Time:** {rec.get('RequiredTime', 'N/A')} minutes")  # Using .get() to avoid KeyError
        st.write(f"**Ingredients:** {rec.get('Ingredients', 'N/A')}")
        st.write(f"**Description:** {rec.get('Description', 'N/A')}")
        st.write('---')
