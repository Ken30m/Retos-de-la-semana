print("\t\tCrea una contraseña")
contador=0
while contador<=3:
    contraseña=input("Introduce una contraseña: ")
    if contraseña[0].isdigit():
        contraseña2=input("Introduce nuevamente la contraseña: ")
        if contraseña==contraseña2:
            print("Contraseña creada correctamente")
            break
        else:
            print("\tError \nLas contraseña no coinciden")
            contador+=1
            continue
    else:
        print("\tError \nLa contraseña debe iniciar con un número, intenta de nuevo")
        contador+=1
        continue