#!/bin/bash
jupyter nbconvert --to script main.ipynb
jupyter nbconvert --to script 1_DataCollection.ipynb
jupyter nbconvert --to script 2_DataProcess.ipynb
jupyter nbconvert --to script 3_DataAnalysis.ipynb
read -p "Presiona Enter para salir..."