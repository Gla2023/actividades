print("Vamos a calcular el área de un rectángulo")

def calcular_area(base, altura):
    area = base * altura
    return area

base = float(input("Escribe el valor de la base:"))
altura = float(input("Escribe el valor de la altura:"))

resultado_area = calcular_area(base, altura)
print("El área de ese rectángulo es:", resultado_area)
