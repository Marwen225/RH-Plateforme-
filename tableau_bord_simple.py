import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import os

class TableauBordRHSimple:
    """Version simplifiée du tableau de bord RH avec matplotlib uniquement"""
    
    def __init__(self, filepath):
        """Initialise l'analyse avec le fichier CSV"""
        self.df = self.load_and_clean_data(filepath)
        if self.df is not None:
            self.prepare_additional_columns()
    
    def load_and_clean_data(self, filepath):
        """Charge et nettoie les données RH"""
        try:
            # Vérifier si le fichier existe
            if not os.path.exists(filepath):
                print(f"Erreur: Le fichier {filepath} n'existe pas.")
                return None
            
            # Chargement du fichier CSV
            df = pd.read_csv(filepath, sep=';', encoding='latin-1')
            print(f"Fichier chargé: {len(df)} lignes, {len(df.columns)} colonnes")
            
            # Afficher les premières colonnes pour déboguer
            print("Colonnes disponibles:", list(df.columns[:10]))
            
            # Suppression des colonnes complètement vides
            df = df.dropna(how='all', axis=1)
            
            # Suppression des lignes complètement vides
            df = df.dropna(how='all')
            
            # Nettoyage des noms de colonnes
            df.columns = df.columns.str.strip()
            
            # Conversion des dates
            if 'Date de naissance' in df.columns:
                df['Date de naissance'] = pd.to_datetime(df['Date de naissance'], format='%d/%m/%Y', errors='coerce')
            
            if 'DateEntree' in df.columns:
                df['DateEntree'] = pd.to_datetime(df['DateEntree'], format='%d/%m/%Y', errors='coerce')
            
            # Nettoyage des colonnes textuelles
            text_columns = ['Sexe', 'Situation Civile', 'Type de contrat', 'Direction']
            for col in text_columns:
                if col in df.columns:
                    df[col] = df[col].astype(str).str.strip()
            
            print(f"Données nettoyées: {len(df)} employés")
            return df
        
        except Exception as e:
            print(f"Erreur lors du chargement: {e}")
            return None
    
    def prepare_additional_columns(self):
        """Prépare des colonnes supplémentaires pour l'analyse"""
        # Calcul de l'âge actuel
        if 'Date de naissance' in self.df.columns:
            today = datetime.now()
            self.df['Age_calcule'] = ((today - self.df['Date de naissance']).dt.days / 365.25).round()
        
        # Calcul de l'ancienneté
        if 'DateEntree' in self.df.columns:
            self.df['Anciennete_calculee'] = ((datetime.now() - self.df['DateEntree']).dt.days / 365.25).round(1)
        
        # Standardisation du sexe
        if 'Sexe' in self.df.columns:
            self.df['Sexe'] = self.df['Sexe'].map({'M': 'Masculin', 'F': 'Féminin'}).fillna(self.df['Sexe'])
    
    def afficher_statistiques_generales(self):
        """Affiche les statistiques générales"""
        print("\n" + "="*60)
        print("📊 TABLEAU DE BORD RH - STATISTIQUES GÉNÉRALES")
        print("="*60)
        
        print(f"👥 Nombre total d'employés: {len(self.df)}")
        
        if 'Age_calcule' in self.df.columns:
            age_stats = self.df['Age_calcule'].describe()
            print(f"📈 Âge moyen: {age_stats['mean']:.1f} ans")
            print(f"📊 Âge médian: {age_stats['50%']:.1f} ans")
            print(f"📉 Âge min/max: {age_stats['min']:.0f} - {age_stats['max']:.0f} ans")
        
        if 'Anciennete_calculee' in self.df.columns:
            anc_moyenne = self.df['Anciennete_calculee'].mean()
            print(f"⏱️ Ancienneté moyenne: {anc_moyenne:.1f} ans")
        
        # Répartition par sexe
        if 'Sexe' in self.df.columns:
            print(f"\n👥 RÉPARTITION PAR SEXE:")
            sexe_counts = self.df['Sexe'].value_counts()
            for sexe, count in sexe_counts.items():
                percentage = (count / len(self.df)) * 100
                print(f"   {sexe}: {count} employés ({percentage:.1f}%)")
        
        # Répartition par type de contrat
        if 'Type de contrat' in self.df.columns:
            print(f"\n📋 TYPES DE CONTRAT:")
            contrat_counts = self.df['Type de contrat'].value_counts()
            for contrat, count in contrat_counts.items():
                percentage = (count / len(self.df)) * 100
                print(f"   {contrat}: {count} employés ({percentage:.1f}%)")
        
        # Top 5 des directions
        if 'Direction' in self.df.columns:
            print(f"\n🏢 TOP 5 DES DIRECTIONS:")
            direction_counts = self.df['Direction'].value_counts().head(5)
            for direction, count in direction_counts.items():
                percentage = (count / len(self.df)) * 100
                print(f"   {direction}: {count} employés ({percentage:.1f}%)")
    
    def creer_graphiques_essentiels(self):
        """Crée les graphiques essentiels"""
        plt.style.use('default')
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle('📊 Tableau de Bord RH - Analyses Principales', fontsize=16, fontweight='bold')
        
        # 1. Répartition par sexe
        if 'Sexe' in self.df.columns:
            sexe_counts = self.df['Sexe'].value_counts()
            colors = ['lightblue', 'pink']
            axes[0, 0].pie(sexe_counts.values, labels=sexe_counts.index, autopct='%1.1f%%', colors=colors)
            axes[0, 0].set_title('👥 Répartition par sexe')
        
        # 2. Distribution des âges
        if 'Age_calcule' in self.df.columns:
            ages = self.df['Age_calcule'].dropna()
            axes[0, 1].hist(ages, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
            axes[0, 1].set_title('📊 Distribution des âges')
            axes[0, 1].set_xlabel('Âge (années)')
            axes[0, 1].set_ylabel('Nombre d\'employés')
            axes[0, 1].grid(True, alpha=0.3)
        
        # 3. Top 10 des directions
        if 'Direction' in self.df.columns:
            direction_counts = self.df['Direction'].value_counts().head(10)
            y_pos = range(len(direction_counts))
            axes[1, 0].barh(y_pos, direction_counts.values, color='lightcoral')
            axes[1, 0].set_yticks(y_pos)
            axes[1, 0].set_yticklabels([d[:20] + '...' if len(d) > 20 else d for d in direction_counts.index], fontsize=8)
            axes[1, 0].set_title('🏢 Top 10 des directions')
            axes[1, 0].set_xlabel('Nombre d\'employés')
            axes[1, 0].grid(True, alpha=0.3)
        
        # 4. Types de contrat
        if 'Type de contrat' in self.df.columns:
            contrat_counts = self.df['Type de contrat'].value_counts()
            axes[1, 1].bar(range(len(contrat_counts)), contrat_counts.values, color='lightgreen')
            axes[1, 1].set_xticks(range(len(contrat_counts)))
            axes[1, 1].set_xticklabels(contrat_counts.index, rotation=45, ha='right')
            axes[1, 1].set_title('📋 Types de contrat')
            axes[1, 1].set_ylabel('Nombre d\'employés')
            axes[1, 1].grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
    
    def analyser_departs(self):
        """Analyse les départs d'employés"""
        print(f"\n🚪 ANALYSE DES DÉPARTS")
        print("="*40)
        
        if 'Observation' not in self.df.columns:
            print("❌ Aucune colonne 'Observation' trouvée.")
            return
        
        # Identifier les départs
        departs = self.df[self.df['Observation'].notna() & (self.df['Observation'] != '')]
        
        if len(departs) == 0:
            print("✅ Aucun départ enregistré dans les données.")
            return
        
        print(f"📊 Nombre de départs: {len(departs)}")
        print(f"📈 Taux de rotation: {(len(departs) / len(self.df)) * 100:.1f}%")
        
        # Raisons de départ
        print(f"\n📋 RAISONS DE DÉPART:")
        raisons = departs['Observation'].value_counts()
        for raison, count in raisons.items():
            percentage = (count / len(departs)) * 100
            print(f"   {raison}: {count} ({percentage:.1f}%)")
        
        # Graphique des départs
        if len(raisons) > 0:
            plt.figure(figsize=(12, 5))
            
            plt.subplot(1, 2, 1)
            raisons.plot(kind='bar', color='salmon', alpha=0.7)
            plt.title('🚪 Raisons de départ')
            plt.xlabel('Raison')
            plt.ylabel('Nombre de départs')
            plt.xticks(rotation=45, ha='right')
            plt.grid(True, alpha=0.3)
            
            # Âge des partants
            if 'Age_calcule' in departs.columns:
                plt.subplot(1, 2, 2)
                ages_departs = departs['Age_calcule'].dropna()
                plt.hist(ages_departs, bins=10, alpha=0.7, color='salmon', edgecolor='black')
                plt.title('📊 Âge des employés partants')
                plt.xlabel('Âge (années)')
                plt.ylabel('Nombre de départs')
                plt.grid(True, alpha=0.3)
            
            plt.tight_layout()
            plt.show()
    
    def generer_rapport_complet(self):
        """Génère un rapport complet"""
        if self.df is None:
            print("❌ Impossible de générer le rapport: données non chargées.")
            return
        
        print("\n🚀 GÉNÉRATION DU RAPPORT RH EN COURS...")
        
        # Statistiques générales
        self.afficher_statistiques_generales()
        
        # Graphiques principaux
        print(f"\n📊 Génération des graphiques...")
        self.creer_graphiques_essentiels()
        
        # Analyse des départs
        self.analyser_departs()
        
        print(f"\n✅ RAPPORT TERMINÉ!")
        print("="*60)

def main():
    """Fonction principale"""
    print("🚀 LANCEMENT DU TABLEAU DE BORD RH SIMPLIFIÉ")
    print("="*50)
    
    # Vérifier si le fichier CSV existe
    csv_file = 'Book1.csv'
    if not os.path.exists(csv_file):
        print(f"❌ Erreur: Le fichier {csv_file} n'existe pas dans le répertoire courant.")
        print(f"📁 Répertoire courant: {os.getcwd()}")
        print(f"📋 Fichiers disponibles: {os.listdir('.')}")
        return
    
    # Créer et lancer l'analyse
    tableau_bord = TableauBordRHSimple(csv_file)
    
    if tableau_bord.df is not None:
        tableau_bord.generer_rapport_complet()
    else:
        print("❌ Impossible de charger les données. Vérifiez le fichier CSV.")

if __name__ == "__main__":
    main()
