import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
import pandas as pd

# Funciones de ordenamiento
def MergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        MergeSort(left_half)
        MergeSort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def QuickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return QuickSort(left) + middle + QuickSort(right)


def Bucket(lista):
    # Convertimos la lista de cadenas a una lista de enteros
    lista = [int(x) for x in lista]

    max_lista = max(lista)
    min_lista = min(lista)

    bucket_rango = (max_lista - min_lista) / (len(lista)-1)

    buckets = [[] for _ in range(len(lista))]

    for i in lista:
        index = int((i - min_lista) / bucket_rango)
        if index == len(lista):
            index -= 1
        buckets[index].append(i)

    resultado = []
    for bucket in buckets:
        if bucket:  # Verifica si el balde no está vacío
            bucket = QuickSort(bucket)
            resultado.extend(bucket)

    return resultado
#Radix sort
def countingRadix(conjunto, exponente, dato):
    contadores =[0 for i in range (10) ]
    ordenada =[0 for i in range (len(conjunto))]

    for diccionario in conjunto: #suma los indices
        indice = (int(diccionario[dato])//exponente)# Se eliminan los digitos ya seleccionados
        indice = indice %10 #Se toma el ultimo dígito
        contadores[indice] += 1
    for i in range (len(contadores)-1): #Suma los indices del contador
        contadores [i+1] += contadores[i]
    #Ordena los valores
    i = len(conjunto)-1
    while i>=0:
        indice = (int(conjunto[i][dato]) //exponente)%10
        ordenada[contadores[indice]-1] = conjunto[i]
        contadores[indice] -=1
        i-=1
    for j in range (len(conjunto)):
        conjunto[j] = ordenada[j]

def radix(conjunto, dato):

    mayor = 0 #Número con más dígitos
    for diccionario in conjunto:
        if int(diccionario[dato])>mayor:
            mayor=int(diccionario[dato])
    exp = 1
    while mayor /exp >=1: #Hasta que se llegue al primer dígito
        countingRadix(conjunto, exp, dato)
        exp *=10 #Se avanza un dígito

#Heap Sort
def heapify(conjunto, N, i, objetivo):
    largest = i  # Initialize largest as root
    l = 2 * i + 1     
    r = 2 * i + 2     

    # See if left child of root exists and is
    # greater than root
    if l < N and int(conjunto[largest][objetivo]) < int(conjunto[l][objetivo]):
        largest = l

    # See if right child of root exists and is
    # greater than root
    if r < N and int(conjunto[largest][objetivo]) < int(conjunto[r][objetivo]):
        largest = r

    # Change root, if needed
    if largest != i:
        conjunto[i], conjunto[largest] = conjunto[largest], conjunto[i]  # swap

        # Heapify the root.
        heapify(conjunto, N, largest, objetivo)

# The main function to sort an conjuntoay of given size
def heapSort(conjunto, objetivo):
    N = len(conjunto)

    # Build a maxheap.
    for i in range(N//2 - 1, -1, -1):
        heapify(conjunto, N, i, objetivo)

    # One by one extract elements
    for i in range(N-1, 0, -1):
        conjunto[i], conjunto[0] = conjunto[0], conjunto[i]  # swap
        heapify(conjunto, i, 0, objetivo)


    return resultado

#Counting
def counting(conjunto, dato):
  
    mayor = 0 
    for diccionario in conjunto:
        if int(diccionario[dato])>mayor:
            mayor=int(diccionario[dato])

    contadores =[0 for i in range (mayor+1)]
    ordenada =[0 for i in range (mayor)]

    for diccionario in conjunto:
        contadores[int(diccionario[dato])] +=1
    for i in range (len(contadores)-1):
        contadores [i+1] += contadores[i]
    for diccionario in conjunto:
        ordenada[contadores[int(diccionario[dato])]-1] = diccionario
        contadores[int(diccionario[dato])]-=1
        
    for i in range(len(conjunto)):
        conjunto[i] = ordenada[i]
    return conjunto


# Función para obtener datos de la API
def obtener_datos_desde_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        messagebox.showerror("Error", "Error al obtener datos de la API")
    return data

def ordenar():
    url = "https://www.datos.gov.co/resource/s9jz-svhi.json"
    metodo = metodo_ordenamiento.get()
    variable = variable_ordenamiento.get()

    conjunto = obtener_datos_desde_api(url)
    data = pd.DataFrame(conjunto)
    if data is not None:
        if variable == "telefono":
            # Si es la columna de teléfono, la convertimos a tipo str para evitar notación científica
            data[variable] = data[variable].astype(str)
        elif variable == "matricula":
            data[variable] = data[variable].astype(float)  # Asegúrate de que sea float

        if metodo == "MergeSort":
            columna = data[variable].tolist()
            MergeSort(columna)
            data[variable] = columna
        elif metodo=="Counting":
            counting(conjunto,variable)
            data = pd.DataFrame(conjunto)
        elif metodo == "Heap":
            heapSort(conjunto,variable)
            data = pd.DataFrame(conjunto)
        elif metodo == "Radix":
            radix(conjunto,variable)
            data = pd.DataFrame(conjunto)
        elif metodo == "QuickSort":
            columna = data[variable].tolist()
            columna = QuickSort(columna)
            data[variable] = columna
        elif metodo == "Bucket":
            columna = data[variable].tolist()
            columna = Bucket(columna)
            data[variable] = columna
        print(data)


        resultado.delete(1.0, tk.END)
        resultado.insert(tk.END, data)

# Configuración de la interfaz gráfica
ventana = tk.Tk()
ventana.title("Taller de Ordenamiento")

# Combobox para seleccionar el método de ordenamiento
metodo_label = ttk.Label(ventana, text="Método de Ordenamiento:")
metodo_label.pack()
metodo_ordenamiento = ttk.Combobox(ventana, values=["Radix","MergeSort", "Heap","QuickSort", "Bucket","Counting"])
metodo_ordenamiento.set("Radix")
metodo_ordenamiento.pack()

# Combobox para seleccionar la variable de ordenamiento
variable_label = ttk.Label(ventana, text="Variable de Ordenamiento:")
variable_label.pack()
variable_ordenamiento = ttk.Combobox(ventana, values=["matricula", "telefono"])
variable_ordenamiento.set("matricula")  # Elige la variable por defecto
variable_ordenamiento.pack()

# Botón para ordenar los datos
boton_ordenar = tk.Button(ventana, text="Ordenar", command=ordenar)
boton_ordenar.pack()

# Resultado
resultado = tk.Text(ventana, height=40, width=150)
resultado.pack()

ventana.mainloop()
