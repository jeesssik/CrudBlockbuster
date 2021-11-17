

#faltaria una opcion para salir y volver al menú anterior

#validacion de seleccion de menu cliente
def menuCliente():
    
    choice= input ("Desea: \n A - Dar de alta un cliente \n B - Modificar teléfono o dirección del cliente \n C - Eliminar cliente\n X - Volver al menú anterior\n Selección: ").upper()

    while choice!="A" and choice!="B" and choice!="C" and choice!="X":
        print("\n\n------------------------\nPor favor, ingrese una de las opciones especificadas\n------------------------\n\n")
        choice= input ("Desea: \n A - Dar de alta un cliente \n B - Modificar teléfono o dirección del cliente \n C - Eliminar cliente\n X - Volver al menú anterior\n Selección: ").upper()


    if choice=="A":
        #para dar de alta a un cliente tengo que validar que no exista en la db
        #ingresa DNI y lo busca, si está salta alerta, sino procede a la creación
        def ingresoDNI():   
            valido=True
            while valido:
                entrada=input("\n++++++++++++++++++++++++++\nIngrese el DNI del nuevo cliente: ")
                print("++++++++++++++++++++++++++\n")
                try:
                    dni= int(entrada)
                    if dni<=0:
                        print("El numero no puede ser 0 ni negativo, volvé a intentar")
                    else:
                        valido=False
                except ValueError:
                    print("El dni ingresado es incorrecto, por favor vuelva a ingresarlo")
            
            print("\n")
            
            ## chequeo del ingreso del dni
            # print(entrada)

                #chequear si dni está en la bd    32456534
            with open("clientes.txt") as C:
                esta=-1
                for line in C:
                    esta=line.find(entrada)
                    if esta>=0:
                        print("\nEl dni "+entrada+ " ya se encuentra registrado\n")
                        ele= input("A - Volver a ingresar el DNI de un nuevo cliente\nX - Volver al menú anterior: ").upper()
                        while ele!="A" and ele!="X":
                            print("Por favor ingrese una de las dos opciones correctas")
                            ele= input("A - Volver a ingresar el DNI de un nuevo cliente\nX - Volver al menú anterior\n").upper()
                        
                        if ele=="X":
                            menuCliente()
                        elif ele=="A":
                            ingresoDNI()
                        
                if esta==-1:
                ##aca se da el ingreso al usuario
                    with open("clientes.txt","a") as f:
                        nom=input("Ingrese el nombre completo: ")
                        tel=input("Ingrese el telefono de contacto: ")
                        dir=input("Ingrese la dirección: ")

                        f.write("DNI: "+entrada+ ", Nombre Completo:"+nom +", Telefono:"+ tel + ", Direccion: "+dir + ", Estado:  0, codPelicula:0")


    ingresoDNI()
menuCliente()