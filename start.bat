@echo off
echo Lancement du Tableau de Bord RH...
echo.
echo Assurez-vous que les packages suivants sont installés :
echo - streamlit
echo - pandas  
echo - matplotlib
echo - seaborn
echo - plotly
echo - numpy
echo.
echo Pour installer les packages :
echo pip install streamlit pandas matplotlib seaborn plotly numpy
echo.
echo Commandes pour lancer l'application :
echo.
echo 1. Analyse exploratoire (graphiques matplotlib) :
echo    python analyse_rh.py
echo.
echo 2. Tableau de bord interactif (Streamlit) :
echo    streamlit run dashboard_rh.py
echo.
echo 3. Alternative si streamlit n'est pas dans le PATH :
echo    python -m streamlit run dashboard_rh.py
echo.
pause
