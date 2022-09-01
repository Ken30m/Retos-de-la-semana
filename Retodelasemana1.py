print("Calculadora de años")
entrada1=input("Introduce el año actual: ")
if entrada1.isnumeric():
    año1=int(entrada1)
else:
    print("\t\tEROR \n Por favor introduce el año en digitos")
    exit()
if año1<1000 or año1>10000:
    print("\t\tERRORE \n Por favor introduce un año de cuatro digitos")
    exit()
else:
    pass
entrada2=input("Introduce un segundo año: ")
if entrada2.isnumeric():
    año2=int(entrada2)
else:
    print("\t\tEROR \n Por favor introduce el año en digitos")
    exit()
if año2<1000 or año2>10000:
    print("\t\tERRORE \n Por favor introduce un año de cuatro digitos")
    exit()
else:
    pass
if año1==año2:
    print("Ingresaste el mismo año dos, veces vuelte a intentarlo")
elif año2==año1+1:
    print(f"Ya solo fata 1 año para llegar al año {año2}")
elif año2==año1-1:
    print(f"Ha pasado solo 1 año desde el {año2}")
elif año1>año2:
    print(f"Han pasado {año1-año2} años desde el año {año2}")
elif año1<año2:
    print(f"Faltan {año2-año1} para llegar al {año2}")
