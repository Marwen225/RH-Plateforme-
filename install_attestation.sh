#!/bin/bash
echo "Installation des dépendances pour le générateur d'attestation..."
echo

echo "Installation de python-docx..."
pip install python-docx

echo
echo "Création du template d'attestation..."
python create_template.py

echo
echo "Installation terminée!"
