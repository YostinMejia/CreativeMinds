def CalculoAnguloReloj(hrs, minutes): 
    if hrs == 12:
        hrs = 0
    if minutes == 60:
        minutes = 0

    if hrs == 0 and minutes == 0:
        return 0

  # Estas operaciones son O(1) porque toman tiempo constante independiente de los valores
    
    angulo = abs((30*hrs - (11 / 2) * minutes) % 360)
    
    anguloAlReves = 360 - angulo
    
    return min(angulo, anguloAlReves)

  # también son de complejidad O(1) ya que son cálculos en tiempo constante 

# Ej
hrs = int(input("Escriba la hora: ")) 
minutes = int(input("Escriba los minutos: "))

angulo = CalculoAnguloReloj(hrs, minutes) # O(1)
angulote = 360 - angulo
print(f"El ángulo menor que va a estar entre las manecillas es de: {angulo} grados")

# la ecuación asintótica es: T(hrs, minutes) = C, donde T es el tiempo que tarda la funcion en ejecutarse y c la constante, 
# independientemente de la hora y los minutos ingresados, el programa tomará aproximadamente el mismo tiempo para calcular el ángulo.
# por lo tanto, en términos de notación Big O, la función es O(1).
# Hecho por Laura y Paulina
