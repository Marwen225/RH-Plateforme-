# 🎯 GUIDE D'UTILISATION - TABLEAU DE BORD RH

## 📋 Résumé du Projet

Vous disposez maintenant d'un **système complet d'analyse RH** avec 3 niveaux d'utilisation :

### 🚀 Fichiers Créés

1. **`dashboard_rh.py`** - Tableau de bord interactif Streamlit (RECOMMANDÉ)
2. **`analyse_rh.py`** - Analyse exploratoire avec matplotlib/seaborn
3. **`tableau_bord_simple.py`** - Version simplifiée (pandas + matplotlib seulement)
4. **`requirements.txt`** - Liste des dépendances
5. **`start.bat`** - Script de démarrage Windows
6. **`README.md`** - Documentation complète

---

## 🔥 UTILISATION RAPIDE

### Option 1: Tableau de Bord Interactif (MEILLEUR)
```bash
# Installation des packages (une seule fois)
pip install streamlit pandas matplotlib seaborn plotly numpy

# Lancement du tableau de bord
streamlit run dashboard_rh.py
```
**→ Ouvre une interface web interactive avec filtres**

### Option 2: Analyse Complète
```bash
# Installation des packages (une seule fois)
pip install pandas matplotlib seaborn numpy

# Lancement de l'analyse
python analyse_rh.py
```
**→ Génère des graphiques et statistiques dans la console**

### Option 3: Version Simplifiée (si problème de packages)
```bash
# Nécessite seulement pandas et matplotlib
python tableau_bord_simple.py
```
**→ Version allégée avec graphiques de base**

---

## 📊 FONCTIONNALITÉS INCLUSES

### 📈 KPIs Automatiques
- ✅ Nombre total d'employés
- ✅ Âge moyen et médian
- ✅ Ancienneté moyenne
- ✅ Taux de masculinité/féminité
- ✅ Répartition par type de contrat

### 📊 Visualisations Créées
- ✅ **Répartition par sexe** (graphique en secteurs)
- ✅ **Distribution des âges** (histogramme)
- ✅ **Pyramide des âges** (par sexe et tranche d'âge)
- ✅ **Top directions** (barres horizontales)
- ✅ **Types de contrat** (graphique en barres)
- ✅ **Catégories professionnelles** (CSP)
- ✅ **Situation civile** (marié/célibataire)

### 🚪 Analyse des Départs
- ✅ **Taux de rotation**
- ✅ **Raisons de départ** (retraite, démission, etc.)
- ✅ **Profil des partants** (âge, département)
- ✅ **Graphiques des départs**

### 🔍 Filtres Interactifs (Streamlit)
- ✅ **Par Direction** (tous ou spécifique)
- ✅ **Par Sexe** (tous, masculin, féminin)
- ✅ **Par Type de Contrat** (CDI, CDD, etc.)

---

## 📁 STRUCTURE DES DONNÉES ANALYSÉES

### Colonnes Utilisées
- `Matricule` → Identifiant unique
- `Nom`, `Prenoms` → Identité
- `Date de naissance` → Calcul automatique de l'âge
- `DateEntree` → Calcul automatique de l'ancienneté
- `Sexe` → M/F → Masculin/Féminin
- `Situation Civile` → État civil
- `Poste` → Fonction
- `Département` → Service
- `Direction` → Direction de rattachement
- `Type de contrat` → CDI/CDD/etc.
- `CSP` → Catégorie socio-professionnelle
- `Observation` → Raisons de départ

### Calculs Automatiques
- ✅ **Âge actuel** calculé depuis la date de naissance
- ✅ **Ancienneté** calculée depuis la date d'entrée
- ✅ **Tranches d'âge** (<25, 25-34, 35-44, 45-54, 55+)
- ✅ **Pourcentages** pour toutes les répartitions

---

## 🎨 CAPTURES D'ÉCRAN DES RÉSULTATS

### Interface Streamlit
```
📊 Tableau de Bord RH Analytique
┌─────────────────────────────────────┐
│ 🔍 Filtres                          │
│ Direction: [Tous ▼]                 │
│ Sexe: [Tous ▼]                      │
│ Type de contrat: [Tous ▼]           │
└─────────────────────────────────────┘

📈 Indicateurs Clés
┌─────────┬─────────┬─────────┬─────────┐
│ 487     │ 45.2    │ 9.3     │ 81.5%   │
│employés │ans      │ans      │masculin │
└─────────┴─────────┴─────────┴─────────┘

[Graphiques interactifs en secteurs, barres, histogrammes...]
```

### Rapport Console
```
=== STATISTIQUES GÉNÉRALES ===
👥 Nombre total d'employés: 487
📈 Âge moyen: 45.2 ans
📊 Âge médian: 45.0 ans
📉 Âge min/max: 23 - 62 ans
⏱️ Ancienneté moyenne: 9.3 ans

👥 RÉPARTITION PAR SEXE:
   Masculin: 397 employés (81.5%)
   Féminin: 90 employés (18.5%)

📋 TYPES DE CONTRAT:
   CDI: 487 employés (100.0%)
```

---

## 🎯 UTILISATION RECOMMANDÉE

### Pour le DRH / Manager
1. **Lancez** `streamlit run dashboard_rh.py`
2. **Filtrez** par direction pour analyser votre équipe
3. **Consultez** les KPIs en temps réel
4. **Analysez** les départs et leur impact

### Pour l'Analyse Ponctuelle
1. **Exécutez** `python analyse_rh.py`
2. **Sauvegardez** les graphiques générés
3. **Copiez** les statistiques pour vos rapports

### Pour les Présentations
1. **Utilisez** la version Streamlit en plein écran
2. **Projetez** les graphiques en direct
3. **Filtrez** en temps réel selon les questions

---

## 🔧 PERSONNALISATION FACILE

### Modifier les Tranches d'Âge
```python
# Dans le code, ligne ~70
bins = [0, 30, 40, 50, 60, 100]  # Nouvelles tranches
labels = ['<30', '30-39', '40-49', '50-59', '60+']
```

### Ajouter de Nouveaux KPIs
```python
# Dans dashboard_rh.py, section métriques
with col5:
    nouveau_kpi = calcul_personalise(filtered_df)
    st.metric("Nouveau KPI", nouveau_kpi)
```

### Nouveaux Filtres
```python
# Dans la sidebar
nouveau_filtre = st.sidebar.selectbox("Nouveau Filtre", options)
```

---

## 🚨 DÉPANNAGE

### Erreur "Module not found"
```bash
pip install streamlit pandas matplotlib seaborn plotly numpy
```

### Erreur d'encodage CSV
→ Le script gère automatiquement l'encodage `latin-1`

### Graphiques ne s'affichent pas
→ Utilisez `tableau_bord_simple.py` en premier

### Performance lente
→ Réduisez la taille du dataset ou utilisez les filtres

---

## 📊 ANALYSES DISPONIBLES IMMÉDIATEMENT

✅ **Démographie** - Pyramide des âges, répartition H/F
✅ **Organisation** - Effectifs par direction/département  
✅ **Contractuel** - Types de contrats, CSP
✅ **Temporel** - Ancienneté, tendances
✅ **Rotation** - Départs, raisons, profils
✅ **Filtrage** - Par direction, sexe, contrat
✅ **Export** - Tableaux, graphiques, statistiques

---

## 🎉 RÉSULTAT FINAL

Vous avez maintenant un **SYSTÈME COMPLET** pour :
- ✅ Impressionner votre responsable RH
- ✅ Analyser les données en temps réel
- ✅ Générer des rapports professionnels
- ✅ Filtrer et explorer interactivement
- ✅ Identifier les tendances et problèmes

**→ Lancez `streamlit run dashboard_rh.py` et profitez ! 🚀**
