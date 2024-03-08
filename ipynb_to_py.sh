#!/bin/bash
jupyter nbconvert --to script 0_main.ipynb
jupyter nbconvert --to script 1_DataCollection.ipynb
jupyter nbconvert --to script 2_DataProcess.ipynb
jupyter nbconvert --to script 3_sqlite3.ipynb
read -p "Presiona Enter para salir..."