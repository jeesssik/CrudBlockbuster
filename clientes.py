

#faltaria una opcion para salir y volver al menú anterior

choice= input ("Desea: \n A - Dar de alta un cliente \n B - Modificar teléfono o dirección del cliente \n C - Eliminar cliente\n X - Volver al menú anterior\n Selección: ").upper()

#validacion de seleccion de menu cliente

while choice!="A" and choice!="B" and choice!="C" and choice!="X":
    print("\n\n------------------------\nPor favor, ingrese una de las opciones especificadas\n------------------------\n\n")
    choice= input ("Desea: \n A - Dar de alta un cliente \n B - Modificar teléfono o dirección del cliente \n C - Eliminar cliente\n X - Volver al menú anterior\n Selección: ").upper()


if choice=="A":
    #para dar de alta a un cliente tengo que validar que no exista en la db
    #ingresa DNI y lo busca, si está salta alerta, sino procede a la creación
    valido=True
    while valido:
        dni=input("Ingrese el DNI del nuevo cliente: ")
        try:
            entrada= int(dni)
            if entrada<=0:
                print("El numero no puede ser 0 ni negativo, volvé a intentar")
            else:
                valido=False
        except ValueError:
            print("El dni ingresado es incorrecto, por favor vuelva a ingresarlo")
    
    print(entrada)