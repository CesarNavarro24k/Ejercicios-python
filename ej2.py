"""
Hacer un programa que solite por teclado dos numeros y realice las siquientes operaciones:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Potencia
6. Salir
"""
while True:
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Salir")
    opc = int(input("Opcion: "))
    if opc == 6:
        break
    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    if opc == 1:
        print("La suma es:",num1+num2)
    elif opc == 2:
        print("La resta es:",num1-num2)
    elif opc == 3:
        print("La multiplicacion es:",num1*num2)
    elif opc == 4:
        if num2 == 0:
            print("No se puede dividir por cero")
        else:
            print("La division es:",num1/num2)
    
    elif opc == 5:
        print("La potencia es:",num1**num2)
    else:
        print("Opción no válida")
    print()