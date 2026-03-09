def munu():
    try:
        print("   calculadora    ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
    except ValueError:
        print("Error: Ingrese un número válido.")     

def ocpcion():
    try:
        opcion = int(input("Seleccione una opción: "))
        return opcion
    except ValueError:
        print("Error: Ingrese un número válido.")
        return None
            
def resta():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    except ValueError:
        print("Error: Ingrese un número válido.")
        
def multiplicacion():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    except ValueError:
        print("Error: Ingrese un número válido.")
        
