def CalculoAnguloReloj(hrs, minutes):
    if hrs == 12:
        hrs = 0
    if minutes == 60:
        minutes = 0

    if hrs == 0 and minutes == 0:
        return 0
    
    angulo = abs((30*hrs - (11 / 2) * minutes) % 360)
    
    anguloAlReves = 360 - angulo
    
    return min(angulo, anguloAlReves)

# Ej
hrs = int(input("Escriba la hora: "))
minutes = int(input("Escriba los minutos: "))

angulo = CalculoAnguloReloj(hrs, minutes)
print(f"El ángulo menor que va a estar entre las manecillas es de: {angulo} grados")