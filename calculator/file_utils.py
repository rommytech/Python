import csv
from datetime import datetime

def guardar_en_csv(valor, nombre_archivo='datos.csv'):
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(nombre_archivo, mode='a', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow([fecha, valor])
