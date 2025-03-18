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


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le fichier CSV (assurez-vous que le chemin est correct)
df = pd.read_csv("vgsales_cleaned.csv")
# --- Page Accueil ---
if page == "Accueil":
    st.title("Bienvenue !")
    st.write("Choisissez l'onglet Visualisation pour voir le graphique.")

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("Visualisation des ventes par genre et par année")

    # Préparation des données pour le graphique en aires
    genre_year_sales = df.groupby(['Année', 'Genre'])['Ventes_Globales'].sum().unstack().fillna(0)

    # Création du graphique en aires avec Matplotlib
    fig, ax = plt.subplots(figsize=(12, 6))
    genre_year_sales.plot(kind='area', stacked=True, ax=ax)

    # Personnalisation du graphique
    ax.set_title("Ventes par genre et par année", fontsize=16)
    ax.set_xlabel("Année", fontsize=14)
    ax.set_ylabel("Ventes globales (millions)", fontsize=14)
    ax.legend(title="Genre", fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')

    # Affichage du graphique dans Streamlit
    st.pyplot(fig)




# --- Page Accueil ---
if page == "Accueil":
    # Vous pouvez laisser cette page vide ou y mettre d'autres éléments
    pass

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("Ventes mondiales par genre de jeux")

    # Préparation des données pour le graphique en barres
    sales_by_genre = df.groupby('Genre')['Ventes_Globales'].sum().sort_values(ascending=False).reset_index()

    # Création du graphique en barres avec Seaborn
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.barplot(data=sales_by_genre, x='Genre', y='Ventes_Globales', ax=ax, palette='viridis')

    # Personnalisation du graphique
    ax.set_title("Ventes mondiales par genre de jeux", fontsize=16)
    ax.set_xlabel("Genre", fontsize=14)
    ax.set_ylabel("Ventes globales (millions)", fontsize=14)
    ax.tick_params(axis='x', rotation=45)

    # Affichage du graphique dans Streamlit
    st.pyplot(fig)


# --- Page Accueil ---
if page == "Accueil":
    pass  # Ne rien afficher dans l'onglet Accueil

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("Ventes mondiales par genre de jeux (Graphique en Aires)")

    # Préparation des données pour le graphique en aires
    sales_by_genre = df.groupby('Genre')['Ventes_Globales'].sum().sort_values(ascending=False)

    # Affichage du graphique en aires avec Streamlit
    st.area_chart(sales_by_genre)
  
import plotly.graph_objects as go
# --- Page Accueil ---
if page == "Accueil":
    pass  # Ne rien afficher dans l'onglet Accueil

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("Top 10 des plateformes les plus utilisées (Camembert)")

    # Préparation des données pour le graphique camembert
    platform_counts = df['Plateforme'].value_counts().nlargest(10)

    # Création du graphique camembert avec Plotly
    fig = go.Figure(data=[go.Pie(labels=platform_counts.index, values=platform_counts.values, hole=.3)])

    # Personnalisation du graphique
    fig.update_layout(title_text="Top 10 des plateformes les plus utilisées")

    # Affichage du graphique dans Streamlit
    st.plotly_chart(fig)


# --- Page Accueil ---
if page == "Accueil":
    pass  # Ne rien afficher dans l'onglet Accueil

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("Évolution des ventes mondiales de jeux vidéo par année")

    # Préparation des données pour le graphique linéaire
    sales_by_year = df.groupby('Année')['Ventes_Globales'].sum()

    # Création du graphique linéaire avec Plotly
    fig = go.Figure(data=go.Scatter(x=sales_by_year.index, y=sales_by_year.values, mode='lines+markers'))

    # Personnalisation du graphique
    fig.update_layout(
        title="Évolution des ventes mondiales de jeux vidéo par année",
        xaxis_title="Année",
        yaxis_title="Ventes globales (millions)"
    )

    # Affichage du graphique dans Streamlit
    st.plotly_chart(fig)


# --- Page Accueil ---
if page == "Accueil":
    pass  # Ne rien afficher dans l'onglet Accueil

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("Distribution des ventes mondiales par genre (Violon)")

    # Création du graphique en violon avec Plotly
    fig = go.Figure()
    for genre in df['Genre'].unique():
        fig.add_trace(go.Violin(y=df['Ventes_Globales'][df['Genre'] == genre],
                                name=genre,
                                box_visible=True,
                                meanline_visible=True))

    # Personnalisation du graphique
    fig.update_layout(
        title="Distribution des ventes mondiales par genre",
        yaxis_title="Ventes globales (millions)",
        xaxis_title="Genre"
    )

    # Affichage du graphique dans Streamlit
    st.plotly_chart(fig)

 # --- Page Accueil ---
if page == "Accueil":
    pass  # Ne rien afficher dans l'onglet Accueil

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("Ventes par région pour une année")

    # Sélecteur d'année
    years = sorted(df['Année'].dropna().unique().astype(int))
    selected_year = st.selectbox("Sélectionner une année", years)

    # Préparation des données pour le graphique
    regions = ['Ventes_Nord_Amerique', 'Ventes_Europe', 'Ventes_Japon', 'Autres_Ventes']
    year_df = df[df['Année'] == selected_year]
    if not year_df.empty:
        region_sales = year_df[regions].sum()

    # Création du graphique en barres avec Plotly
    fig = go.Figure(data=[go.Bar(x=region_sales.index, y=region_sales.values)])

    # Personnalisation du graphique
    fig.update_layout(
        title="Ventes globales par région",
        xaxis_title="Région",
        yaxis_title="Ventes globales (millions)"
    )

    # Affichage du graphique dans Streamlit
    st.plotly_chart(fig)   
    

# --- Page Accueil ---
if page == "Accueil":
    pass  # Ne rien afficher dans l'onglet Accueil

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("Ventes globales par plateforme (Graphique de dispersion)")

    # Préparation des données pour le graphique de dispersion
    platform_sales = df.groupby('Plateforme')['Ventes_Globales'].sum().reset_index()

    # Création du graphique de dispersion avec Plotly
    fig = go.Figure(data=go.Scatter(x=platform_sales['Plateforme'],
                                    y=platform_sales['Ventes_Globales'],
                                    mode='markers'))

    # Personnalisation du graphique
    fig.update_layout(
        title="Ventes globales par plateforme",
        xaxis_title="Plateforme",
        yaxis_title="Ventes globales (millions)"
    )

    # Affichage du graphique dans Streamlit
    st.plotly_chart(fig)

import plotly.graph_objects as go   
# --- Page Accueil ---
if page == "Accueil":
    pass  # Ne rien afficher dans l'onglet Accueil

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("Jeux les plus vendus par plateforme (Graphique en barres groupées)")

    # Préparation des données pour le graphique
    platform_game_sales = df.groupby(['Plateforme', 'Nom'])['Ventes_Globales'].sum().nlargest(20).reset_index()

    # Création du graphique en barres groupées avec Plotly
    fig = go.Figure()
    for platform in platform_game_sales['Plateforme'].unique():
        platform_data = platform_game_sales[platform_game_sales['Plateforme'] == platform]
        fig.add_trace(go.Bar(x=platform_data['Nom'],
                                 y=platform_data['Ventes_Globales'],
                                 name=platform))

    # Personnalisation du graphique
    fig.update_layout(
        title="Jeux les plus vendus par plateforme (Top 20)",
        xaxis_title="Nom du jeu",
        yaxis_title="Ventes globales (millions)",
        barmode='group' # pour un graph en barre groupé
    )

    # Affichage du graphique dans Streamlit
    st.plotly_chart(fig)
