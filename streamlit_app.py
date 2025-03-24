
import streamlit as st

st.markdown(
    """
    <style>
    /* Cibler les titres principaux */
    h1 {
        color: #007bff !important; /* Bleu */
    }

    /* Cibler les sous-titres */
    h2, h3 {
        color: #28a745 !important; /* Vert */
    }

    /* Cibler les paragraphes qui servent de sous-titres */
    /* Remplacez .votre-classe-de-sous-titre par la classe réelle */
    .st-emotion-cache-r421ms p {
        color: #6c757d !important; /* Gris */
    }

    /* Ajoutez d'autres sélecteurs et styles ici */
    </style>
    """,
    unsafe_allow_html=True,
)
import streamlit as st



# Couleurs personnalisées
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f8ff; /* Couleur de fond */
    }
    .stButton>button {
        background-color: #4CAF50; /* Couleur des boutons */
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Espacement
st.markdown("<br>", unsafe_allow_html=True)  # Ajoute une ligne vide


import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
    <script>
    const mainBlock = document.querySelector('.stMainBlockContainer.block-container.st-emotion-cache-mtjnbi.eht7o1d4');
    if (mainBlock) {
        mainBlock.addEventListener('click', () => {
            if (mainBlock.style.backgroundColor === 'lightblue') {
                mainBlock.style.backgroundColor = '#f0f8ff'; // Couleur d'origine
            } else {
                mainBlock.style.backgroundColor = 'lightblue';
            }
        });

        mainBlock.addEventListener('mouseover', () => {
            mainBlock.style.transform = 'scale(1.05)'; // Agrandir légèrement au survol
            mainBlock.style.transition = 'transform 0.3s ease';
        });

        mainBlock.addEventListener('mouseout', () => {
            mainBlock.style.transform = 'scale(1)'; // Rétablir la taille d'origine
        });
    }
    </script>
    """,
    height=0,  # Important: définit la hauteur de l'iframe à 0 pour qu'il ne soit pas visible
)
import streamlit as st
import pandas as pd 
from PIL import Image
import numpy as np 

st.title("🎈 Ma nouvelle application streamlit")
st.write(
    "Commençons à construire ! Pour trouver de l'aide et de l'inspiration, rendez-vous sur [docs.streamlit.io](https://docs.streamlit.io/)."
)

import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Vérifier l'intégrité de la base de données
cursor.execute("PRAGMA integrity_check;")
print(cursor.fetchone())

conn.close()

# ajout dans la barre de navigation "gestion des utilisateur"
import streamlit as st
from db import init_db, add_user, get_users

# Initialiser la base de données (crée la table si elle n'existe pas)
init_db()

# --- Barre de navigation latérale ---
with st.sidebar:
    st.title("Gestion des utilisateurs")

    # Formulaire pour ajouter un utilisateur
    st.subheader("Ajouter un nouvel utilisateur")
    new_user = st.text_input("Nom d'utilisateur", key="new_user")
    new_password = st.text_input("Mot de passe", type="password", key="new_password")

    if st.button("Ajouter l'utilisateur"):
        if new_user and new_password:  # Vérifier que les champs ne sont pas vides
            success = add_user(new_user, new_password)
            if success:
                st.success(f"L'utilisateur {new_user} a été ajouté avec succès !")
            else:
                st.error("Ce nom d'utilisateur existe déjà. Veuillez en choisir un autre.")
        else:
            st.warning("Veuillez remplir tous les champs.")

    # Afficher la liste des utilisateurs
    st.subheader("Liste des utilisateurs enregistrés")
    users = get_users()
    st.dataframe(users)  # Affichage sous forme de tableau

# --- Contenu principal de l'application ---
st.title("Contenu principal de l'application")
st.write("Le contenu principal de votre application s'affiche ici.")


# ajouter dans la barre de navigation "connexion et inscription"
import sqlite3
import streamlit as st
import hashlib

# Connexion à la base SQLite
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Création de la table users
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)''')
conn.commit()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hash_password(password)))
    conn.commit()

def authenticate_user(username, password):
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hash_password(password)))
    return cursor.fetchone() is not None

# --- Barre de navigation latérale ---
with st.sidebar:
    st.title("Authentification")

    menu = st.selectbox("Menu", ["Connexion", "Inscription"])

    if menu == "Inscription":
        new_user = st.text_input("Nom d'utilisateur", key="inscription_nom_utilisateur")
        new_pass = st.text_input("Mot de passe", type="password", key="inscription_mot_passe")
        if st.button("S'inscrire"):
            register_user(new_user, new_pass)
            st.success("Inscription réussie")

    if menu == "Connexion":
        user = st.text_input("Nom d'utilisateur", key="connexion_nom_utilisateur")
        password = st.text_input("Mot de passe", type="password", key="connexion_mot_passe")
        if st.button("Se connecter"):
            if authenticate_user(user, password):
                st.success("Connexion réussie")
            else:
                st.error("Identifiants incorrects")






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
    

    # 3️⃣ Informations générales
    st.subheader("Informations générales")
    st.write("""
Ce jeu de données présente les ventes de jeux vidéo à travers le monde, classées par popularité. 
Les colonnes principales incluent le nom du jeu, la plateforme, l'année de sortie, le genre et l'éditeur. 
Les ventes sont exprimées en millions d'unités vendues. 
Cette analyse vise à identifier les jeux les plus populaires et les tendances du marché.
""")

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
    st.write("Choisissez l'onglet Visualisation pour voir les graphiques.")

# --- Page Visualisation ---
if page == "Visualisation":
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



## Ajout d'un graphique en barre
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

## Ajout d'un graphique en aires
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


 ## Ajout d'un graphique en camembert 
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


## Ajout d'un graphique linéaire
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


## Ajout d'un graphique en violon
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
    
## Ajout d'un graphique de dispersion
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


## Ajout d'un graphique en barres groupées
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


# --- Page Accueil ---
if page == "Accueil":
    pass  # Ne rien afficher dans l'onglet Accueil

# --- Page Exploration de données ---
elif page == "Exploration de données":
    st.title("Exploration de données")

    # Filtres interactifs
    genre_options = ['Tous'] + list(df['Genre'].unique())
    selected_genre = st.selectbox("Filtrer par genre", genre_options)

    platform_options = ['Toutes'] + list(df['Plateforme'].unique())
    selected_platform = st.multiselect("Filtrer par plateforme", platform_options)

    year_options = ['Toutes'] + list(df['Année'].dropna().unique().astype(int))
    selected_year = st.selectbox("Filtrer par année", year_options)

    # Filtrage des données
    filtered_df = df.copy()
    if selected_genre != 'Tous':
        filtered_df = filtered_df[filtered_df['Genre'] == selected_genre]

    if 'Toutes' not in selected_platform:
        filtered_df = filtered_df[filtered_df['Plateforme'].isin(selected_platform)]

    if selected_year != 'Toutes':
        filtered_df = filtered_df[filtered_df['Année'] == selected_year]

    # Affichage des données filtrées
    st.write(f"Nombre de jeux affichés: {filtered_df.shape[0]}")
    st.dataframe(filtered_df)

# --- Page Visualisation ---
elif page == "Visualisation":
    # ... (votre code de visualisation) ...
    pass

# --- Page Accueil ---
if page == "Accueil":
    pass  # Ne rien afficher dans l'onglet Accueil

# --- Page Exploration de données ---
elif page == "Exploration de données":
    st.title("Exploration de données")

    # Filtre avec st.slider
    min_sales, max_sales = st.slider("Filtrer par ventes globales (millions)", 0.0, float(df['Ventes_Globales'].max()), (0.0, float(df['Ventes_Globales'].max())))

    # Filtrage des données
    filtered_df = df[(df['Ventes_Globales'] >= min_sales) & (df['Ventes_Globales'] <= max_sales)]

    # Affichage des données filtrées
    st.write(f"Nombre de jeux affichés: {filtered_df.shape[0]}")
    st.dataframe(filtered_df)

# --- Page Visualisation ---
elif page == "Visualisation":
    # ... (votre code de visualisation) ...
    pass


## Ajout des logos des différentes plateforme de jeux vidéos
from PIL import Image
import os

# Dictionnaire de correspondance des logos
logos = {
    'PS4': 'logos/images(6).png',
    'XOne': 'logos/images(4).png',
    'WiiU': 'logos/images(12).png',
    'Wii': 'logos/images(11).png',
    'NES': 'logos/images(13).jpeg',
    'GB': 'logos/images (2).jpeg',
    'GC': 'logo/images(7).jpeg',
    'X360': 'logos/images (1).jpeg',
    'XB': 'logos/images(3).jpeg',
    'PS3': 'logos/images(5).jpeg',
    'PS2': 'logos/images(8).png',
    'DS': 'logos/images(9).png',
    'SNES': 'logos/images(15).png',
    'PSP': 'logos/images(10).png', 
    'PS': 'logos/images(14).jpeg',
    'GBA': 'logos/images(16).jpeg',
    '3DS': 'logos/images(17).jpeg',
    '2600': 'logos/images(18).png'

    
}
 
# --- Barre latérale de navigation ---
st.sidebar.title("Navigation")
pages = ["Accueil", "Logos des plateformes"]
page = st.sidebar.selectbox("Choisissez une page :", pages)

# --- Page Accueil ---
if page == "Accueil":
    pass  # Ne rien afficher dans l'onglet Accueil

# --- Page Logos des plateformes ---
elif page == "Logos des plateformes": # et ici
    st.title("Logos des plateformes de jeux vidéo")

    # Sélection de la plateforme
    platform_options = ['Toutes'] + list(df['Plateforme'].unique())
    selected_platform = st.selectbox("Sélectionner une plateforme", platform_options)

    # Afficher le logo si une plateforme est sélectionnée
    if selected_platform != 'Toutes':
        if selected_platform in logos:
            logo_path = logos[selected_platform]
            if os.path.exists(logo_path):
                try:
                    image = Image.open(logo_path)
                    st.image(image, caption=selected_platform, width=200)  # Agrandir le logo
                except Exception as e:
                    st.error(f"Erreur lors du chargement du logo pour {selected_platform}: {e}")
            else:
                st.warning(f"Logo non trouvé pour {selected_platform} à l'emplacement: {logo_path}")
        else:
            st.info(f"Logo non disponible pour la plateforme : {selected_platform}")


import streamlit as st

st.markdown(
    """
    <style>
    body {
        background-color: #e8f5e9; 
    }
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

import streamlit as st

st.markdown(
    """
    <style>
    .stVerticalBlock.st-emotion-cache-64tehz.eu6p4el3 {
        background-color: #f0f8ff;
        border: 1px solid #ccc;
        padding: 20px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
    <script>
    const verticalBlock = document.querySelector('.stVerticalBlock.st-emotion-cache-64tehz.eu6p4el3');
    if (verticalBlock) {
        verticalBlock.addEventListener('click', () => {
            verticalBlock.style.backgroundColor = 'lightblue';
        });

        verticalBlock.addEventListener('mouseover', () => {
            verticalBlock.style.transform = 'scale(1.05)';
            verticalBlock.style.transition = 'transform 0.3s ease';
        });

        verticalBlock.addEventListener('mouseout', () => {
            verticalBlock.style.transform = 'scale(1)';
        });
    }
    </script>
    """,
    height=0,
)

import streamlit as st

st.markdown(
    """
    <style>
    .stMainBlockContainer.block-container.st-emotion-cache-mtjnbi.eht7o1d4 {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }

    .stMainBlockContainer.block-container.st-emotion-cache-mtjnbi.eht7o1d4:hover {
        transform: scale(1.02);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ajouter image fond ecran à l'application
import base64

def image_to_base64(image_path):
    """Convertit une image en chaîne base64."""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

image_path = "image fond ecran streamlit.jpeg"  # Remplacez par le chemin de votre image
base64_image = image_to_base64(image_path)

import streamlit as st
import base64

def image_to_base64(image_path):
    """Convertit une image en chaîne base64."""
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

image_path = "image fond ecran streamlit.jpeg"  # Remplacez par le chemin de votre image
base64_image = image_to_base64(image_path)

st.markdown(
    f"""
    <style>
    body {{
        background-image: url("data:image/jpeg;base64,{base64_image}");
        background-size: cover;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

## Ajout de "paramétres" dans navigation
import streamlit as st

# --- Barre latérale de navigation ---
st.sidebar.title("Navigation")
pages = ["Accueil","Paramètres"]  # Ajoutez "Paramètres"
page = st.sidebar.selectbox("Choisissez une page :", pages)

# --- Page Exploration de données ---
if page == "Exploration de données":
    st.title("Exploration de données")
    # ... votre code pour l'exploration de données ...

# --- Page Visualisation ---
elif page == "Visualisation":
    st.title("Visualisation")
    # ... votre code pour la visualisation ...

# --- Page Paramètres ---
elif page == "Paramètres":
    st.title("Paramètres et Ressources")

    st.header("À propos de Streamlit")
    st.write(
        """
        Streamlit est un framework Python open-source qui permet de créer facilement des applications web interactives pour la science des données et le machine learning.
        """
    )
    st.markdown("[Documentation Streamlit](https://docs.streamlit.io/)")

    st.header("Charte graphique")
    st.write(
        """
        Voici la charte graphique utilisée pour cette application :
        """
    )
    st.write("- Couleur principale : #007bff (bleu)")
    st.write("- Couleur secondaire : #28a745 (vert)")
    st.write("- Couleur de fond : #f0f8ff")

    st.header("Ressources utiles")
    st.markdown("- [Charte graphique 1](https://docs.streamlit.io/library/get-started/main-concepts)")
    st.markdown("- [Charte graphique 2](https://docs.streamlit.io/library/advanced-features/configuration)")



## Ajout collecte de données
import streamlit as st
import sqlite3

def collect_user_data():
    """Collecte les données personnelles de l'utilisateur."""
    nom_utilisateur = st.text_input("Nom d'utilisateur")
    email = st.text_input("Adresse e-mail")
    # Ajoutez d'autres champs nécessaires
    return {"nom_utilisateur": nom_utilisateur, "email": email}

def store_user_data(data):
    """Stocke les données personnelles dans la base de données."""
    conn = sqlite3.connect("utilisateurs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS utilisateurs (
            nom_utilisateur TEXT,
            email TEXT
        )
    """)
    cursor.execute("INSERT INTO utilisateurs VALUES (?, ?)", (data["nom_utilisateur"], data["email"]))
    conn.commit()
    conn.close()

# Exemple d'utilisation
user_data = collect_user_data()
if st.button("Enregistrer"):
    store_user_data(user_data)
    st.success("Données enregistrées !")


## Ajout du consentement de l'utilisateur
import streamlit as st

def get_user_consent():
    """Obtient le consentement de l'utilisateur."""
    consent = st.checkbox("J'accepte que mes données soient utilisées conformément à la politique de confidentialité.")
    return consent

# Exemple d'utilisation
consent = get_user_consent()
if consent:
    st.write("Consentement accordé !")
else:
    st.write("Veuillez accepter la politique de confidentialité.")


## Ajout des droits des utlisateurs
import streamlit as st
import sqlite3

def get_user_data(nom_utilisateur):
    """Récupère les données personnelles de l'utilisateur."""
    conn = sqlite3.connect("utilisateurs.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM utilisateurs WHERE nom_utilisateur = ?", (nom_utilisateur,))
    data = cursor.fetchone()
    conn.close()
    return data

def delete_user_data(nom_utilisateur):
    """Supprime les données personnelles de l'utilisateur."""
    conn = sqlite3.connect("utilisateurs.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM utilisateurs WHERE nom_utilisateur = ?", (nom_utilisateur,))
    conn.commit()
    conn.close()

# Exemple d'utilisation
nom_utilisateur = st.text_input("Nom d'utilisateur", key="nom_utilisateur_input")  # Ajout de key
if st.button("Afficher mes données", key="afficher_donnees"):  # Ajout de key
    data = get_user_data(nom_utilisateur)
    if data:
        st.write(data)
    else:
        st.write("Utilisateur non trouvé.")
if st.button("Supprimer mes données", key="supprimer_donnees"):  # Ajout de key
    delete_user_data(nom_utilisateur)
    st.success("Données supprimées !")
