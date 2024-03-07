import subprocess

# Lista de comandos a ejecutar
comandos = [
    "jupyter nbconvert --to script --output-dir='../' 0_main.ipynb",
    "jupyter nbconvert --to script --output-dir='../' 1_DataCollection.ipynb",
    "jupyter nbconvert --to script --output-dir='../' 3_sqlite3.ipynb"
]

# Ejecutar cada comando en la lista
for comando in comandos:
    subprocess.run(comando, shell=True)
