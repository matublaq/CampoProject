#!/bin/bash
jupyter nbconvert --to script --output-dir="../" 0_main.ipynb
jupyter nbconvert --to script --output-dir="../" 1_DataCollection.ipynb
jupyter nbconvert --to script --output-dir="../" 2_DataProcess.ipynb
jupyter nbconvert --to script --output-dir="../" 3_sqlite3.ipynb
read -p "Presiona Enter para salir..."