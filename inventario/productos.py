import json
import csv
import os

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')

def guardar_txt(datos):
    with open(os.path.join(DATA_DIR, 'datos.txt'), 'a') as f:
        f.write(f"{datos['id']},{datos['nombre']},{datos['precio']},{datos['cantidad']}\n")

def leer_txt():
    try:
        with open(os.path.join(DATA_DIR, 'datos.txt'), 'r') as f:
            return f.read()
    except FileNotFoundError:
        return ""

def guardar_json(datos):
    try:
        with open(os.path.join(DATA_DIR, 'datos.json'), 'r') as f:
            lista = json.load(f)
    except FileNotFoundError:
        lista = []
    lista.append(datos)
    with open(os.path.join(DATA_DIR, 'datos.json'), 'w') as f:
        json.dump(lista, f, indent=4)

def leer_json():
    try:
        with open(os.path.join(DATA_DIR, 'datos.json'), 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def guardar_csv(datos):
    with open(os.path.join(DATA_DIR, 'datos.csv'), 'a', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['id', 'nombre', 'precio', 'cantidad'])
        writer.writerow(datos)

def leer_csv():
    productos = []
    try:
        with open(os.path.join(DATA_DIR, 'datos.csv'), 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                productos.append(row)
    except FileNotFoundError:
        pass
    return productos