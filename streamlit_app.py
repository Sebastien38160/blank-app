import streamlit as st
import pandas as pd 
from PIL import Image
import numpy as np 

st.title("🎈 My new streamlit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

import streamlit as st
from PIL import Image
import pandas as pd

# --- Barre latérale de navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Choisissez une page :", ["Accueil", "Exploration de données", "Visualisation", "À propos de"])

# --- Page Accueil ---
if page == "Accueil":
    st.title("🎮 Bienvenue sur l'Accueil !")
    st.write("Choisissez une option dans la barre latérale pour commencer.")

# --- Page Exploration de données ---
elif page == "Exploration de données":
    st.title("📊 Exploration de données")
    
# Téléchargement d'un fichier CSV
uploaded_file = st.file_uploader("Téléchargez un fichier CSV", type=["csv"])
    
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Aperçu des données :")
    st.dataframe(df)

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("📷 Lire et afficher des images")
    
# Téléchargement et affichage d'images
uploaded_image = st.file_uploader("Téléchargez une image", type=["png", "jpg", "jpeg"])
    
if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="Image chargée", use_container_width=True)

# --- Page À propos de ---
elif page == "À propos de":
    st.title("ℹ️ À propos de cette application")
    st.write("Cette application a été créée avec Streamlit pour afficher des données et des images.")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.title("📊 Exploration de données")

# 1️⃣ Chargement du fichier CSV
uploaded_file = st.file_uploader("vgsales_cleaning.csv", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

# Créer des onglets pour séparer exploration et visualisation
    tab_exploration, tab_visualisation = st.tabs(["Exploration des données", "Visualisation"])
    
    # 2️⃣ Exploration des données (dans l'onglet exploration)
    with tab_exploration:
        st.subheader("Aperçu des données")
        st.dataframe(df.head())  
    
    # 2️⃣ Aperçu des données
    st.subheader("Aperçu des données")
    st.dataframe(df.head())  # Affiche les 5 premières lignes du DataFrame

    # 3️⃣ Informations générales
    st.subheader("Informations générales")
    st.write(df.info())

    # 4️⃣ Valeurs manquantes
    st.subheader("Valeurs manquantes")
    st.write(df.isnull().sum())

    # 5️⃣ Statistiques descriptives
    st.subheader("Statistiques générales")
    st.write(df.describe())
else:
    st.write("Veuillez télécharger un fichier CSV pour commencer l'analyse.")



    
 












