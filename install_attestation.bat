@echo off
echo Installation des dependances pour le generateur d'attestation...
echo.

echo Installation de python-docx...
pip install python-docx

echo.
echo Creation du template d'attestation...
python create_template.py

echo.
echo Installation terminee!
pause
