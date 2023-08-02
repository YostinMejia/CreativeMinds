def asignar_estudiantes(estudiantes, tamano_grupo):
    grupos = []  # Lista de grupos vacía #O(1)

    while estudiantes: # O(n)
        nuevo_grupo = []  # Crear un nuevo grupo vacío # O(n)
        grupos.append(nuevo_grupo) #O(n)

        for estudiante in estudiantes[:]:  # Utilizamos una copia para evitar problemas de eliminación en el bucle #O(n**2)
            if len(nuevo_grupo) < tamano_grupo: #O(n**2)
                nuevo_grupo.append(estudiante) #O(n**2)
                estudiantes.remove(estudiante) #O(n**2)

    return grupos #O(1)
 
 #Complejidad de la función
 #  2 O(1) + 3 O(n) + 4 O(n**2)

# Ejemplo de uso:
lista_estudiantes = ["Estudiante1", "Estudiante2", "Estudiante3", "Estudiante4", "Estudiante5", "Estudiante6"] #O(1)
tamano_max_grupo = 3 #O(1)
grupos_asignados = asignar_estudiantes(lista_estudiantes, tamano_max_grupo) #O(n**2)

print(grupos_asignados) #O(1)

#Complejidad del algoritmo
#  3 O(1) + O(n**2)

