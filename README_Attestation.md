# Dashboard RH Executive - Générateur d'Attestation de Travail

## 🆕 Nouvelle Fonctionnalité

Votre dashboard RH dispose maintenant d'un **générateur automatique d'attestations de travail** !

## 📋 Fonctionnalités

- **Sélection intuitive** : Liste déroulante avec recherche des employés
- **Génération automatique** : Attestation personnalisée au format Word (.docx)
- **Template personnalisable** : Basé sur "attestation de travail.docx"
- **Téléchargement direct** : Fichier prêt à imprimer et signer

## 🔧 Installation

### Option 1 : Installation automatique (Windows)
```bash
# Double-cliquez sur le fichier :
install_attestation.bat
```

### Option 2 : Installation automatique (Linux/Mac)
```bash
# Dans le terminal :
chmod +x install_attestation.sh
./install_attestation.sh
```

### Option 3 : Installation manuelle
```bash
pip install python-docx
python create_template.py
```

## 📄 Template d'Attestation

Le générateur utilise un template Word avec les placeholders suivants :

- `[NOM_COMPLET]` - Nom et prénom de l'employé
- `[DATE_NAISSANCE]` - Date de naissance (format JJ/MM/AAAA)
- `[LIEU_NAISSANCE]` - Lieu de naissance
- `[POSTE]` - Poste occupé
- `[DATE_ENTREE]` - Date d'entrée dans l'entreprise
- `[DATE_GENERATION]` - Date de génération de l'attestation
- `[NOM_ENTREPRISE]` - Nom de votre entreprise
- `[DIRECTEUR_RH]` - Nom du directeur RH
- `[VILLE]` - Ville de l'entreprise

## 🎯 Utilisation

1. **Démarrez le dashboard** : `streamlit run dashboard_rh.py`
2. **Scrollez vers le bas** jusqu'à la section "GÉNÉRATEUR D'ATTESTATION DE TRAVAIL"
3. **Sélectionnez un employé** dans la liste déroulante
4. **Cliquez sur "Générer l'Attestation"**
5. **Téléchargez le fichier** généré

## 🔄 Personnalisation du Template

Pour personnaliser votre attestation :

1. Ouvrez le fichier `attestation de travail.docx`
2. Modifiez le contenu selon vos besoins
3. Gardez les placeholders `[...]` pour l'injection automatique des données
4. Sauvegardez le fichier

## 📊 Données Requises

Pour générer une attestation complète, les colonnes suivantes sont recommandées dans votre CSV :

- `Nom` (requis)
- `Prenoms` (requis)
- `Date de naissance`
- `Lieu de naissance`
- `Poste`
- `DateEntree`

## ⚠️ Dépannage

### Erreur "python-docx n'est pas installé"
```bash
pip install python-docx
```

### Template non trouvé
Le système créera automatiquement un template par défaut si `attestation de travail.docx` n'existe pas.

### Données manquantes
Les champs manquants afficheront "Non renseigné" dans l'attestation.

## 🎨 Aperçu de l'Interface

La nouvelle section comprend :
- 🔍 **Sélecteur d'employé** avec recherche
- 📊 **Affichage des informations** de l'employé sélectionné
- 📄 **Bouton de génération** de l'attestation
- 💾 **Téléchargement direct** du document
- ℹ️ **Informations** sur le template et les placeholders
- 📈 **Statistiques** des données disponibles

## 🚀 Avantages

- **Gain de temps** : Plus besoin de créer manuellement chaque attestation
- **Consistance** : Format uniforme pour toutes les attestations
- **Traçabilité** : Horodatage automatique
- **Professionnalisme** : Documents standardisés et bien formatés

Profitez de cette nouvelle fonctionnalité pour optimiser votre gestion RH ! 🎉
