import streamlit as st
import pandas as pd
import numpy as np
import pickle 



recipe_list1 = pickle.load(open('recipes_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
recipes_list2 = recipe_list1['recipes'].values
#st.image('food.jpg', use_column_width=True)

st.header("Recipe Recommandation System")

#dropDown
selecte_recipes = st.selectbox("Select a recipe: ",recipes_list2)

import streamlit.components.v1 as components

def recommend(recipe):
    index = recipe_list1[recipe_list1['recipes'] == recipe].index[0]
    distance = sorted(list(enumerate(similarity[index])) , reverse = True , key = lambda vector:vector[1])
    recommend_recipe = []
    for i in distance[1:6]:
        #recipe_id = recipes.iloc[i[0]].id
        recommend_recipe.append(recipe_list1.iloc[i[0]].recipe)
    return recommend_recipe

if st.button("Show Recommandation"):
    recipe_name   = recommend(selecte_recipes)
    col1 , col2 , col3 , col4 , col5 = st.columns(5)
    with col1:
        st.text(recipe_name[0])
    with col2:
        st.text(recipe_name[1])
    with col3:
        st.text(recipe_name[2])
    with col4:
        st.text(recipe_name[3])
    with col5:
        st.text(recipe_name[4])

