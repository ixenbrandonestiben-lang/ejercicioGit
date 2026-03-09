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
  
