#!/bin/bash
jupyter nbconvert --to script main.ipynb
jupyter nbconvert --to script DataCollection.ipynb
jupyter nbconvert --to script DataProcess.ipynb
jupyter nbconvert --to script DataAnalysis.ipynb
read -p "Presiona Enter para salir..."