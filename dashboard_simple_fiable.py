import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Configuration de la page Streamlit
st.set_page_config(
    page_title="🏢 Dashboard RH | Données Réelles",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .main > div {
        padding-top: 2rem;
    }
    .metric-container {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 10px;
        color: white;
        margin: 10px 0;
    }
    h1 {
        color: #2c3e50;
        font-family: 'Arial', sans-serif;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
    }
    .info-box {
        background-color: #d1ecf1;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #17a2b8;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 5px solid #28a745;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Fonction pour charger les données
@st.cache_data
def load_data():
    """Charge les données RH du fichier CSV"""
    try:
        df = pd.read_csv('Book1.csv', sep=';', encoding='latin-1')
        
        # Nettoyage de base
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df = df.dropna(how='all', axis=1)
        empty_cols = [col for col in df.columns if df[col].isna().all() or (df[col] == '').all()]
        df = df.drop(columns=empty_cols)
        df = df.dropna(how='all')
        df.columns = df.columns.str.strip()
        
        # Nettoyage des espaces
        text_columns = ['Sexe', 'Situation Civile', 'Type de contrat', 'Direction', 'Déparetement', 'CSP', 'Poste', 'Unité']
        for col in text_columns:
            if col in df.columns:
                df[col] = df[col].astype(str).str.strip()
        
        # Conversion des dates
        if 'Date de naissance' in df.columns:
            df['Date de naissance'] = pd.to_datetime(df['Date de naissance'], format='%d/%m/%Y', errors='coerce')
        
        if 'DateEntree' in df.columns:
            df['DateEntree'] = pd.to_datetime(df['DateEntree'], format='%d/%m/%Y', errors='coerce')
        
        # Calculs d'âge et ancienneté
        if 'Date de naissance' in df.columns:
            today = datetime.now()
            df['Age_calcule'] = ((today - df['Date de naissance']).dt.days / 365.25).round().astype('Int64')
        
        if 'DateEntree' in df.columns:
            df['Anciennete_calculee'] = ((datetime.now() - df['DateEntree']).dt.days / 365.25).round(1)
        
        return df
    
    except Exception as e:
        st.error(f"Erreur lors du chargement des données: {e}")
        return None

def main():
    # Header
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1 style='color: #2c3e50; font-size: 2.5em; margin-bottom: 10px;'>
            🏢 DASHBOARD RH FIABLE
        </h1>
        <p style='color: #7f8c8d; font-size: 1.2em; font-style: italic;'>
            Analyses basées uniquement sur vos données réelles
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Chargement des données
    with st.spinner('🔄 Chargement des données...'):
        df = load_data()
    
    if df is None:
        st.error("❌ Impossible de charger les données.")
        st.stop()
    
    st.markdown(f"""
    <div class="success-box">
        <h4>✅ Données chargées avec succès</h4>
        <p><strong>Total:</strong> {len(df)} employés | <strong>Mise à jour:</strong> {datetime.now().strftime('%d/%m/%Y à %H:%M')}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Filtres
    st.sidebar.header("🔍 Filtres")
    
    # Filtre par direction
    if 'Direction' in df.columns:
        directions = ['Toutes'] + df['Direction'].dropna().unique().tolist()
        selected_direction = st.sidebar.selectbox("Direction", directions)
    
    # Filtre par sexe
    if 'Sexe' in df.columns:
        sexes = ['Tous'] + df['Sexe'].dropna().unique().tolist()
        selected_sexe = st.sidebar.selectbox("Sexe", sexes)
    
    # Application des filtres
    filtered_df = df.copy()
    
    if 'Direction' in df.columns and selected_direction != 'Toutes':
        filtered_df = filtered_df[filtered_df['Direction'] == selected_direction]
    
    if 'Sexe' in df.columns and selected_sexe != 'Tous':
        filtered_df = filtered_df[filtered_df['Sexe'] == selected_sexe]
    
    # Métriques principales
    st.header("📊 MÉTRIQUES PRINCIPALES")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-container">
            <h3 style="margin: 0; color: white;">👥</h3>
            <h2 style="margin: 5px 0; color: white;">{len(filtered_df)}</h2>
            <p style="margin: 0; color: #f8f9fa;">Employés Total</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        if 'Age_calcule' in filtered_df.columns:
            avg_age = filtered_df['Age_calcule'].mean()
            st.markdown(f"""
            <div class="metric-container">
                <h3 style="margin: 0; color: white;">📅</h3>
                <h2 style="margin: 5px 0; color: white;">{avg_age:.1f} ans</h2>
                <p style="margin: 0; color: #f8f9fa;">Âge Moyen</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col3:
        if 'Anciennete_calculee' in filtered_df.columns:
            avg_tenure = filtered_df['Anciennete_calculee'].mean()
            st.markdown(f"""
            <div class="metric-container">
                <h3 style="margin: 0; color: white;">⏱️</h3>
                <h2 style="margin: 5px 0; color: white;">{avg_tenure:.1f} ans</h2>
                <p style="margin: 0; color: #f8f9fa;">Ancienneté Moy.</p>
            </div>
            """, unsafe_allow_html=True)
    
    with col4:
        if 'Observation' in filtered_df.columns:
            departs = filtered_df[filtered_df['Observation'].notna() & (filtered_df['Observation'] != '')]
            nb_departs = len(departs)
            st.markdown(f"""
            <div class="metric-container">
                <h3 style="margin: 0; color: white;">🚪</h3>
                <h2 style="margin: 5px 0; color: white;">{nb_departs}</h2>
                <p style="margin: 0; color: #f8f9fa;">Départs</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Analyses visuelles
    st.header("📈 ANALYSES BASÉES SUR VOS DONNÉES")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Répartition par sexe
        if 'Sexe' in filtered_df.columns:
            sexe_counts = filtered_df['Sexe'].value_counts()
            fig_sexe = px.pie(
                values=sexe_counts.values,
                names=sexe_counts.index,
                title="👥 Répartition par Sexe"
            )
            st.plotly_chart(fig_sexe, use_container_width=True)
    
    with col2:
        # Répartition par département
        if 'Déparetement' in filtered_df.columns:
            dept_counts = filtered_df['Déparetement'].value_counts().head(8)
            fig_dept = px.bar(
                y=dept_counts.index,
                x=dept_counts.values,
                orientation='h',
                title="🏢 Répartition par Département"
            )
            st.plotly_chart(fig_dept, use_container_width=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Répartition par direction
        if 'Direction' in filtered_df.columns:
            direction_counts = filtered_df['Direction'].value_counts()
            fig_direction = px.bar(
                x=direction_counts.index,
                y=direction_counts.values,
                title="🎯 Répartition par Direction"
            )
            fig_direction.update_xaxes(tickangle=45)
            st.plotly_chart(fig_direction, use_container_width=True)
    
    with col2:
        # Types de contrat
        if 'Type de contrat' in filtered_df.columns:
            contrat_counts = filtered_df['Type de contrat'].value_counts()
            fig_contrat = px.pie(
                values=contrat_counts.values,
                names=contrat_counts.index,
                title="📋 Types de Contrat"
            )
            st.plotly_chart(fig_contrat, use_container_width=True)
    
    # Distribution des âges
    if 'Age_calcule' in filtered_df.columns:
        st.subheader("📊 Distribution des Âges")
        fig_age = px.histogram(
            filtered_df,
            x='Age_calcule',
            nbins=20,
            title="Distribution des Âges"
        )
        st.plotly_chart(fig_age, use_container_width=True)
        
        # Statistiques d'âge
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("👶 Plus jeune", f"{filtered_df['Age_calcule'].min()} ans")
        with col2:
            st.metric("📊 Médiane", f"{filtered_df['Age_calcule'].median():.0f} ans")
        with col3:
            st.metric("👴 Plus âgé", f"{filtered_df['Age_calcule'].max()} ans")
    
    # Analyse des départs
    if 'Observation' in filtered_df.columns:
        departs = filtered_df[filtered_df['Observation'].notna() & (filtered_df['Observation'] != '')]
        if len(departs) > 0:
            st.subheader("🚪 Analyse des Départs")
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Raisons de départ
                raisons = departs['Observation'].value_counts()
                fig_raisons = px.pie(
                    values=raisons.values,
                    names=raisons.index,
                    title="Raisons de Départ"
                )
                st.plotly_chart(fig_raisons, use_container_width=True)
            
            with col2:
                # Âge des partants
                if 'Age_calcule' in departs.columns:
                    fig_age_departs = px.histogram(
                        departs,
                        x='Age_calcule',
                        title="Âge des Partants",
                        nbins=10
                    )
                    st.plotly_chart(fig_age_departs, use_container_width=True)
    
    # Tableaux de données
    st.header("📋 DONNÉES DÉTAILLÉES")
    
    tab1, tab2 = st.tabs(["👥 Liste des Employés", "📊 Statistiques"])
    
    with tab1:
        st.subheader("Liste des Employés Filtrés")
        
        # Colonnes à afficher
        cols_to_show = ['Matricule', 'Nom', 'Prenoms', 'Sexe', 'Poste', 'Direction', 'Déparetement']
        available_cols = [col for col in cols_to_show if col in filtered_df.columns]
        
        if 'Age_calcule' in filtered_df.columns:
            available_cols.append('Age_calcule')
        if 'Anciennete_calculee' in filtered_df.columns:
            available_cols.append('Anciennete_calculee')
        
        st.dataframe(filtered_df[available_cols], use_container_width=True)
        
        # Export
        if st.button("📥 Exporter en CSV"):
            csv = filtered_df.to_csv(index=False)
            st.download_button(
                label="⬇️ Télécharger",
                data=csv,
                file_name=f"export_rh_{datetime.now().strftime('%Y%m%d_%H%M')}.csv",
                mime="text/csv"
            )
    
    with tab2:
        st.subheader("Statistiques par Colonne")
        
        # Sélection de colonne
        numeric_cols = filtered_df.select_dtypes(include=[np.number]).columns.tolist()
        if numeric_cols:
            selected_col = st.selectbox("Choisir une colonne numérique", numeric_cols)
            
            if selected_col:
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.metric("Moyenne", f"{filtered_df[selected_col].mean():.2f}")
                with col2:
                    st.metric("Médiane", f"{filtered_df[selected_col].median():.2f}")
                with col3:
                    st.metric("Min", f"{filtered_df[selected_col].min():.2f}")
                with col4:
                    st.metric("Max", f"{filtered_df[selected_col].max():.2f}")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px;'>
        <p style='color: #6c757d; margin: 0;'>
            🏢 <strong>Dashboard RH Fiable</strong> | 
            📊 <em>100% basé sur vos données réelles</em> | 
            📅 <em>Mise à jour: {}</em>
        </p>
    </div>
    """.format(datetime.now().strftime('%d/%m/%Y à %H:%M')), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
