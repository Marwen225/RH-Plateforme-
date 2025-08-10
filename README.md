# 📊 Tableau de Bord RH Analytique

## Description
Ce projet propose un tableau de bord interactif pour l'analyse des données RH, développé avec Python et Streamlit. Il permet d'analyser les effectifs, la démographie, les départs et autres KPIs essentiels pour le service RH.

## 🚀 Installation et Lancement

### Prérequis
- Python 3.8 ou plus récent
- Le fichier `Book1.csv` dans le même répertoire

### Installation des dépendances
```bash
pip install -r requirements.txt
```

### Lancement du tableau de bord
```bash
streamlit run dashboard_rh.py
```

### Analyse exploratoire (optionnel)
```bash
python analyse_rh.py
```

## 📈 Fonctionnalités Principales

### KPIs Affichés
- **Nombre total d'employés** : Effectif total filtré
- **Âge moyen** : Calculé à partir des dates de naissance
- **Ancienneté moyenne** : Calculée à partir des dates d'entrée
- **Taux de masculinité** : Pourcentage d'hommes dans l'effectif

### Visualisations Disponibles

#### 1. 👥 Répartition par sexe
- Graphique en secteurs (pie chart)
- Pourcentages automatiques

#### 2. 📋 Types de contrat
- Graphique en barres horizontales
- CDI, CDD, autres types

#### 3. 📊 Distribution des âges
- Histogramme des âges
- 20 tranches automatiques

#### 4. 🏢 Employés par direction
- Top 10 des directions
- Barres horizontales

#### 5. 🔺 Pyramide des âges
- Visualisation par sexe et tranche d'âge
- Hommes à gauche, femmes à droite

#### 6. 👔 Catégories socio-professionnelles (CSP)
- Répartition Cadre/Maîtrise/Exécution
- Graphique en secteurs

#### 7. 💼 Situation civile
- Marié/Célibataire/Autres
- Graphique en barres

#### 8. 🚪 Analyse des départs
- Raisons de départ (retraite, démission, etc.)
- Graphiques et tableau détaillé

## 🔍 Filtres Interactifs

### Sidebar de filtrage
- **Direction** : Filtrer par direction (tous ou spécifique)
- **Sexe** : Filtrer par sexe (tous, masculin, féminin)
- **Type de contrat** : Filtrer par type de contrat

### Application des filtres
Tous les graphiques et KPIs se mettent à jour automatiquement selon les filtres sélectionnés.

## 📋 Structure des Données

### Colonnes utilisées
- `Matricule` : Identifiant unique
- `Nom`, `Prenoms` : Identité
- `Date de naissance` : Pour calcul de l'âge
- `DateEntree` : Pour calcul de l'ancienneté
- `Age` : Âge fourni (backup)
- `Sexe` : M/F → Masculin/Féminin
- `Situation Civile` : État civil
- `Poste` : Fonction occupée
- `Département` : Service d'affectation
- `Direction` : Direction de rattachement
- `Type de contrat` : CDI/CDD/etc.
- `CSP` : Catégorie socio-professionnelle
- `Observation` : Raisons de départ

### Nettoyage automatique
- Suppression des colonnes vides
- Conversion des dates (format DD/MM/YYYY)
- Standardisation des valeurs textuelles
- Calculs automatiques d'âge et d'ancienneté

## 📊 Sections du Tableau de Bord

### 1. Indicateurs Clés
Métriques principales en haut de page

### 2. Graphiques Principaux
Visualisations essentielles en 2x2

### 3. Pyramide des Âges
Visualisation démographique détaillée

### 4. Analyses Complémentaires
CSP et situation civile

### 5. Analyse des Départs
Section dédiée aux mouvements de personnel

### 6. Données Détaillées
- Tableau filtrable des employés
- Statistiques par département

## 🛠️ Personnalisation

### Modification des tranches d'âge
Dans la fonction `create_age_pyramid()`, modifier :
```python
bins = range(20, 70, 5)  # Tranches de 5 ans de 20 à 70 ans
```

### Ajout de nouveaux KPIs
Dans la section métriques :
```python
with col5:
    nouveau_kpi = calcul_personalise(filtered_df)
    st.metric("Nouveau KPI", nouveau_kpi)
```

### Nouveaux filtres
Dans la sidebar :
```python
nouveau_filtre = st.sidebar.selectbox("Nouveau Filtre", options)
```

## 📱 Interface Responsive

Le tableau de bord s'adapte automatiquement :
- **Desktop** : Affichage en colonnes multiples
- **Tablet** : Colonnes réduites
- **Mobile** : Affichage vertical

## 🔄 Mise à Jour des Données

### Automatique
Les calculs se mettent à jour automatiquement lors du changement de filtres

### Manuel
Pour de nouvelles données :
1. Remplacer le fichier `Book1.csv`
2. Rafraîchir la page (F5)

## 📊 Analyses Disponibles

### Démographiques
- Pyramide des âges
- Répartition hommes/femmes
- Distribution des âges

### Organisationnelles
- Effectifs par direction/département
- Types de contrats
- Catégories professionnelles

### Mouvements de Personnel
- Taux de rotation
- Raisons de départ
- Profils des partants

### Temporelles
- Ancienneté moyenne
- Évolution des effectifs
- Tendances par période

## 🎯 Utilisation Recommandée

### Pour le DRH
- Suivi des KPIs principaux
- Préparation des CODIR
- Analyse des équilibres

### Pour les Managers
- Effectifs de leur direction
- Profils de leurs équipes
- Besoins en recrutement

### Pour les Analystes RH
- Études démographiques
- Préparation de rapports
- Analyses prédictives

## 🔧 Dépannage

### Erreur de chargement CSV
- Vérifier l'encodage (latin-1 par défaut)
- Contrôler le séparateur (point-virgule)
- S'assurer que le fichier existe

### Graphiques vides
- Vérifier les noms de colonnes
- Contrôler les données nulles
- Adapter les filtres

### Performance lente
- Réduire la taille du dataset
- Optimiser les filtres
- Utiliser le cache Streamlit

## 📧 Support

Pour toute question ou amélioration :
- Consulter la documentation Streamlit
- Vérifier les logs d'erreur
- Adapter le code aux spécificités locales

---

*Tableau de bord développé pour optimiser l'analyse des données RH et faciliter la prise de décision*
