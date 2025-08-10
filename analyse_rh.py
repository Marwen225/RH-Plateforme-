import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import numpy as np

# Configuration pour l'affichage des graphiques
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

class AnalyseRH:
    """Classe pour l'analyse des données RH"""
    
    def __init__(self, filepath):
        """Initialise l'analyse avec le fichier CSV"""
        self.df = self.load_and_clean_data(filepath)
        self.prepare_additional_columns()
    
    def load_and_clean_data(self, filepath):
        """Charge et nettoie les données RH"""
        try:
            # Chargement du fichier CSV
            df = pd.read_csv(filepath, sep=';', encoding='latin-1')
            
            # Suppression des colonnes vides
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            df = df.dropna(how='all', axis=1)
            
            # Suppression des lignes vides
            df = df.dropna(how='all')
            
            # Nettoyage des noms de colonnes
            df.columns = df.columns.str.strip()
            
            # Conversion des dates
            if 'Date de naissance' in df.columns:
                df['Date de naissance'] = pd.to_datetime(df['Date de naissance'], format='%d/%m/%Y', errors='coerce')
            
            if 'DateEntree' in df.columns:
                df['DateEntree'] = pd.to_datetime(df['DateEntree'], format='%d/%m/%Y', errors='coerce')
            
            # Nettoyage des colonnes textuelles
            text_columns = ['Sexe', 'Situation Civile', 'Type de contrat', 'Direction', 'Déparetement']
            for col in text_columns:
                if col in df.columns:
                    df[col] = df[col].astype(str).str.strip()
            
            print(f"Données chargées avec succès: {len(df)} employés")
            return df
        
        except Exception as e:
            print(f"Erreur lors du chargement: {e}")
            return None
    
    def prepare_additional_columns(self):
        """Prépare des colonnes supplémentaires pour l'analyse"""
        if self.df is None:
            return
        
        # Calcul de l'âge actuel
        if 'Date de naissance' in self.df.columns:
            today = datetime.now()
            self.df['Age_calcule'] = ((today - self.df['Date de naissance']).dt.days / 365.25).round()
        
        # Calcul de l'ancienneté
        if 'DateEntree' in self.df.columns:
            self.df['Anciennete_calculee'] = ((datetime.now() - self.df['DateEntree']).dt.days / 365.25).round(1)
        
        # Tranches d'âge
        if 'Age_calcule' in self.df.columns:
            bins = [0, 25, 35, 45, 55, 100]
            labels = ['<25', '25-34', '35-44', '45-54', '55+']
            self.df['Tranche_age'] = pd.cut(self.df['Age_calcule'], bins=bins, labels=labels, right=False)
        
        # Standardisation du sexe
        if 'Sexe' in self.df.columns:
            self.df['Sexe'] = self.df['Sexe'].map({'M': 'Masculin', 'F': 'Féminin'}).fillna(self.df['Sexe'])
    
    def display_summary_stats(self):
        """Affiche les statistiques descriptives"""
        print("=== STATISTIQUES GÉNÉRALES ===")
        print(f"Nombre total d'employés: {len(self.df)}")
        
        if 'Age_calcule' in self.df.columns:
            print(f"Âge moyen: {self.df['Age_calcule'].mean():.1f} ans")
            print(f"Âge médian: {self.df['Age_calcule'].median():.1f} ans")
            print(f"Âge min/max: {self.df['Age_calcule'].min():.0f} - {self.df['Age_calcule'].max():.0f} ans")
        
        if 'Anciennete_calculee' in self.df.columns:
            print(f"Ancienneté moyenne: {self.df['Anciennete_calculee'].mean():.1f} ans")
        
        print("\n=== RÉPARTITIONS ===")
        
        # Répartition par sexe
        if 'Sexe' in self.df.columns:
            print("\nRépartition par sexe:")
            sexe_counts = self.df['Sexe'].value_counts()
            for sexe, count in sexe_counts.items():
                percentage = (count / len(self.df)) * 100
                print(f"  {sexe}: {count} ({percentage:.1f}%)")
        
        # Répartition par type de contrat
        if 'Type de contrat' in self.df.columns:
            print("\nRépartition par type de contrat:")
            contrat_counts = self.df['Type de contrat'].value_counts()
            for contrat, count in contrat_counts.items():
                percentage = (count / len(self.df)) * 100
                print(f"  {contrat}: {count} ({percentage:.1f}%)")
    
    def create_visualizations(self):
        """Crée les visualisations principales"""
        fig, axes = plt.subplots(2, 3, figsize=(18, 12))
        fig.suptitle('Tableau de Bord RH - Analyses Principales', fontsize=16, fontweight='bold')
        
        # 1. Répartition par sexe
        if 'Sexe' in self.df.columns:
            sexe_counts = self.df['Sexe'].value_counts()
            axes[0, 0].pie(sexe_counts.values, labels=sexe_counts.index, autopct='%1.1f%%')
            axes[0, 0].set_title('Répartition par sexe')
        
        # 2. Distribution des âges
        if 'Age_calcule' in self.df.columns:
            axes[0, 1].hist(self.df['Age_calcule'].dropna(), bins=15, alpha=0.7, color='skyblue', edgecolor='black')
            axes[0, 1].set_title('Distribution des âges')
            axes[0, 1].set_xlabel('Âge')
            axes[0, 1].set_ylabel('Nombre d\'employés')
        
        # 3. Employés par direction (top 10)
        if 'Direction' in self.df.columns:
            direction_counts = self.df['Direction'].value_counts().head(10)
            axes[0, 2].barh(range(len(direction_counts)), direction_counts.values)
            axes[0, 2].set_yticks(range(len(direction_counts)))
            axes[0, 2].set_yticklabels(direction_counts.index, fontsize=8)
            axes[0, 2].set_title('Top 10 Directions')
            axes[0, 2].set_xlabel('Nombre d\'employés')
        
        # 4. Types de contrat
        if 'Type de contrat' in self.df.columns:
            contrat_counts = self.df['Type de contrat'].value_counts()
            axes[1, 0].bar(range(len(contrat_counts)), contrat_counts.values, color='lightcoral')
            axes[1, 0].set_xticks(range(len(contrat_counts)))
            axes[1, 0].set_xticklabels(contrat_counts.index, rotation=45, ha='right')
            axes[1, 0].set_title('Types de contrat')
            axes[1, 0].set_ylabel('Nombre d\'employés')
        
        # 5. Tranches d'âge par sexe
        if 'Tranche_age' in self.df.columns and 'Sexe' in self.df.columns:
            tranche_sexe = pd.crosstab(self.df['Tranche_age'], self.df['Sexe'])
            tranche_sexe.plot(kind='bar', ax=axes[1, 1], stacked=True)
            axes[1, 1].set_title('Tranches d\'âge par sexe')
            axes[1, 1].set_xlabel('Tranche d\'âge')
            axes[1, 1].set_ylabel('Nombre d\'employés')
            axes[1, 1].legend(title='Sexe')
        
        # 6. Ancienneté
        if 'Anciennete_calculee' in self.df.columns:
            axes[1, 2].hist(self.df['Anciennete_calculee'].dropna(), bins=15, alpha=0.7, color='lightgreen', edgecolor='black')
            axes[1, 2].set_title('Distribution de l\'ancienneté')
            axes[1, 2].set_xlabel('Ancienneté (années)')
            axes[1, 2].set_ylabel('Nombre d\'employés')
        
        plt.tight_layout()
        plt.show()
    
    def analyze_departures(self):
        """Analyse les départs d'employés"""
        print("\n=== ANALYSE DES DÉPARTS ===")
        
        if 'Observation' not in self.df.columns:
            print("Aucune colonne 'Observation' trouvée.")
            return
        
        # Identifier les départs
        departs = self.df[self.df['Observation'].notna() & (self.df['Observation'] != '')]
        
        if len(departs) == 0:
            print("Aucun départ enregistré.")
            return
        
        print(f"Nombre de départs: {len(departs)}")
        print(f"Taux de rotation: {(len(departs) / len(self.df)) * 100:.1f}%")
        
        # Raisons de départ
        print("\nRaisons de départ:")
        raisons = departs['Observation'].value_counts()
        for raison, count in raisons.items():
            percentage = (count / len(departs)) * 100
            print(f"  {raison}: {count} ({percentage:.1f}%)")
        
        # Visualisation des départs
        if len(raisons) > 0:
            plt.figure(figsize=(12, 6))
            plt.subplot(1, 2, 1)
            raisons.plot(kind='bar', color='salmon')
            plt.title('Raisons de départ')
            plt.xlabel('Raison')
            plt.ylabel('Nombre de départs')
            plt.xticks(rotation=45, ha='right')
            
            # Analyse par âge des départs
            if 'Age_calcule' in departs.columns:
                plt.subplot(1, 2, 2)
                plt.hist(departs['Age_calcule'].dropna(), bins=10, alpha=0.7, color='salmon', edgecolor='black')
                plt.title('Âge des employés partants')
                plt.xlabel('Âge')
                plt.ylabel('Nombre de départs')
            
            plt.tight_layout()
            plt.show()
    
    def detailed_department_analysis(self):
        """Analyse détaillée par département"""
        print("\n=== ANALYSE PAR DÉPARTEMENT ===")
        
        if 'Déparetement' not in self.df.columns:
            print("Aucune colonne 'Département' trouvée.")
            return
        
        # Statistiques par département
        dept_stats = self.df.groupby('Déparetement').agg({
            'Matricule': 'count',
            'Age_calcule': 'mean' if 'Age_calcule' in self.df.columns else lambda x: 0,
            'Anciennete_calculee': 'mean' if 'Anciennete_calculee' in self.df.columns else lambda x: 0,
        }).round(1)
        
        dept_stats.columns = ['Effectif', 'Âge moyen', 'Ancienneté moyenne']
        dept_stats = dept_stats.sort_values('Effectif', ascending=False)
        
        print("\nTop 10 des départements par effectif:")
        print(dept_stats.head(10))
        
        # Visualisation
        fig, axes = plt.subplots(1, 2, figsize=(15, 6))
        
        # Effectifs par département (top 10)
        top_depts = dept_stats.head(10)
        axes[0].barh(range(len(top_depts)), top_depts['Effectif'])
        axes[0].set_yticks(range(len(top_depts)))
        axes[0].set_yticklabels(top_depts.index, fontsize=10)
        axes[0].set_title('Top 10 des départements par effectif')
        axes[0].set_xlabel('Nombre d\'employés')
        
        # Âge moyen par département
        if 'Âge moyen' in top_depts.columns:
            axes[1].barh(range(len(top_depts)), top_depts['Âge moyen'], color='lightcoral')
            axes[1].set_yticks(range(len(top_depts)))
            axes[1].set_yticklabels(top_depts.index, fontsize=10)
            axes[1].set_title('Âge moyen par département')
            axes[1].set_xlabel('Âge moyen (années)')
        
        plt.tight_layout()
        plt.show()
    
    def generate_report(self):
        """Génère un rapport complet"""
        print("=" * 60)
        print("RAPPORT D'ANALYSE RH COMPLET")
        print("=" * 60)
        
        self.display_summary_stats()
        self.create_visualizations()
        self.analyze_departures()
        self.detailed_department_analysis()
        
        print("\n" + "=" * 60)
        print("FIN DU RAPPORT")
        print("=" * 60)

# Fonction principale pour exécuter l'analyse
def main():
    """Fonction principale pour lancer l'analyse"""
    # Initialiser l'analyse
    analyste = AnalyseRH('Book1.csv')
    
    if analyste.df is not None:
        # Générer le rapport complet
        analyste.generate_report()
    else:
        print("Impossible de charger les données. Vérifiez le fichier CSV.")

if __name__ == "__main__":
    main()
