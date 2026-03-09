def munu():
    try:
        print("   calculadora    ")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
    except ValueError:
<<<<<<< HEAD
        print("Error: Ingrese un número válido.")     
=======
        print("Error: Ingrese un número válido.") 

<<<<<<< HEAD
def calcular_suma(a,b):
    num1=float(input("ingrese el primer numero"))
    num2= float(input("ingrese el segundo numero"))
    suma = num1 + num2
    print(suma)

def  calcular_division(num1,num2):
    num1=float(input("ingrese el primer numero"))
    num2= float(input("ingrese el segundo numero"))
    producto=num1 * num2
    print(producto)
while True:
    munu()
    opcion= opcion()

    if opcion==1:
        calcular_suma(num1,num2)
    elif opcion==2:
        resta()
    elif opcion==3:
        multiplicacion()
    elif opcion==4:
        division()
    elif opcion==4:
        print("saliendo del programa")
        break
  
>>>>>>> remotes/origin/feature/Ciclo
=======
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
        
>>>>>>> remotes/origin/feature/multiplicacion
