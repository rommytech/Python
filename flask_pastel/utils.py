import csv
import os

def guardar_pedidos_csv(nom, prod, fecha, desc):
    existe = os.path.exists("pedidos.csv")
    
    # Abre el archivo pedidos.csv en modo 'a' (añadir)
    with open('pedidos.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)  # Crea el escritor de CSV
        
        # Si el archivo no existe, escribe el encabezado
        if not existe:
            writer.writerow(["Nombres", "Producto", "Fecha", "Desc."])
        
        # Escribe una nueva fila con los datos proporcionados
        writer.writerow([nom, prod, fecha, desc])

def contar_pedidos_csv():
    # Abre el archivo CSV donde se guardan los pedidos
    try:
        with open('pedidos.csv', mode='r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            pedidos = list(reader)
            
            # Si el archivo tiene encabezados, resta 1 al total
            if len(pedidos) > 0 and pedidos[0][0].lower() == 'nombres':
                return len(pedidos) - 1
            else:
                return len(pedidos)
    except FileNotFoundError:
        # Si el archivo no existe, no hay pedidos
        return 0
