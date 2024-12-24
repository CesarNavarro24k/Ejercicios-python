"""
Crea un programa que pida dos número enteros al usuario y diga si alguno de ellos es 
múltiplo del otro. Crea una función EsMultiplo que reciba  
los dos números, y devuelve si el primero es múltiplo del segundo. 
"""
def EsMultiplo(num1,num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
if EsMultiplo(num1,num2):
    print("Uno de los numeros es multiplo del otro")
else:
    print("Ninguno de los numeros es multiplo del otro")
