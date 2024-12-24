import random
caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ""
while True:
    num = int(input("Cuántos caracteres quieres que tenga tu contraseña: "))
    for i in range( num):
        password += random.choice(caracteres)
    print("La contraseña generada es:",password)
    preg = input("Quieres generar otra contraseña? (si/no): ")
    if preg == "no":
        break
    else:
        password = ""