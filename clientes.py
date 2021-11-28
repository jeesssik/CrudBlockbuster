
#faltaria una opcion para salir y volver al menú anterior

#validacion de seleccion de menu cliente

def gestionclientes():
    def menuCliente():
        print("\n\n-----------------------------------\n")
        choice= input ("Desea: \n A - Dar de alta un cliente \n B - Modificar teléfono o dirección del cliente \n C - Eliminar cliente\n D - Consultar estado de cliente \n X - Volver al menú anterior\n Selección: ").upper()

        while choice!="A" and choice!="B" and choice!="C" and choice!="D" and choice!="X":
            print("\n\n------------------------\nPor favor, ingrese una de las opciones especificadas\n------------------------\n\n")
            choice= input ("Desea: \n A - Dar de alta un cliente \n B - Modificar teléfono o dirección del cliente \n C - Eliminar cliente \n D - Consultar estado de cliente \n X - Volver al menú anterior\n Selección: ").upper()

    ############# funcion para validacion de ingreso de DNI
        def ingresoDNI():   
                valido=True
                while valido:
                    entrada=input("\n++++++++++++++++++++++++++\nIngrese el DNI del cliente: ")
                    print("++++++++++++++++++++++++++\n")
                    try:
                        dni= int(entrada)
                        if dni<=0:
                            print("El numero no puede ser 0 ni negativo, volvé a intentar")
                        elif len(entrada)<8 or len(entrada)>8:
                            print("El dni consta de 8 numeros")
                        else:
                            valido=False
                    except ValueError:
                        print("El dni ingresado es incorrecto, por favor vuelva a ingresarlo")
                
                print("\n")
                return entrada
    #############
    ############ funcion para revisar si en dni estab en la bd, devuelve la linea de info si está
        def buscarDNI(entrada):
            # opening a text file
            file1 = open("clientes.txt", "r")
            
            # setting flag and index to 0
            flag = 0
            index = 0
            
            for line in file1:  
                index += 1 
                
                if entrada in line:
                    flag = 1
                    texto=line
                    break  

            if flag == 0: 
                print("\nEl dni ingresado no se encuentra registrado como cliente, por favor vuelva a ingresarlo")
                return buscarDNI(ingresoDNI())
            else: 
                return texto
            # closing text file    
            file1.close()  
    
        #alta cliente
        if choice=="A":
            
            documento = ingresoDNI()
            datosUser=buscarDNI(documento)
            if len(datosUser)>0:
                entrada=documento
                                    

            ##aca se da el ingreso al usuario
                with open("clientes.txt","a") as f:
                    nom=input("Ingrese el nombre completo: ")
                    tel=input("Ingrese el telefono de contacto: ")
                    dir=input("Ingrese la dirección: ")

                    f.write("DNI: "+entrada+ ", Nombre Completo:"+nom +", Telefono:"+ tel + ", Direccion: "+dir + ", Estado:  0, codPelicula:0\n")

        #modificacion tel/dir cliente
        if choice=="B":
            dni= ingresoDNI()
            esta=buscarDNI(dni) #esta trae la linea entera

            elect= input("\nDesea modificar el teléfono o la dirección del cliente?\n\nA- Teléfono\nB- Dirección\nSelección:").upper()
            
            while elect!="A" and elect!="B":
                print("\n\n------------------------\nPor favor, ingrese una de las opciones especificadas\n------------------------\n\n")
                elect= input("\nDesea modificar el teléfono o la dirección del cliente?\nA- Teléfono\nB- Dirección\nSelección:").upper()

            if elect=="A": #telefono
                
                pte1=esta[:esta.find("Telefono")-2] # almacena lo anterior al telefono
                #print(pte1)
                
                #### aca insertar nuevo telefono
                tel=input("Ingrese el telefono de contacto: ")
                tel= " Telefono: "+tel+", "

                pte2= esta[esta.find("Direccion"):] #lo que hay despues del telefono
                #print(pte2)

                modificado=pte1+tel+pte2

                #hace una lista de todas las lineas del archivo, y reescribe el archivo salteando la linea ignorada
                with open("clientes.txt", "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != esta: #ignora la linea modificada
                            f.write(i)
                        if i == esta: #donde está la linea modif, agrega la linea nueva
                            f.write(modificado)
                        
                    f.truncate()

                print("\n\*** ¡Telefono modificado con éxito! *** \n")

                ###modificacion de direccion####

            if elect=="B": #modificacion de direccion
            
                pte1=esta[:esta.find("Direccion")-2] # almacena lo anterior a la direccion
            
                #### aca insertar nuevo telefono
                dire=input("Ingrese la nueva direccion: ")
                dire= ", Direccion: "+dire+", "

                pte2= esta[esta.find("Estado"):] #lo que hay despues de direccion
                

                modificado=pte1+dire+pte2

                #hace una lista de todas las lineas del archivo, y reescribe el archivo salteando la linea ignorada
                with open("clientes.txt", "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != esta: #ignora la linea modificada
                            f.write(i)
                        if i == esta: #donde está la linea modif, agrega la linea nueva
                            f.write(modificado)
                        
                    f.truncate()

                print("\n\*** ¡Direccion modificada con éxito! *** \n")
    

        ##eliminar cliente
        if choice=="C":
            dni= ingresoDNI()
            print(dni)
            esta=buscarDNI(dni) #esta trae la linea entera a borrar
        
                                                
            elegir=input("Quiere borrar a este cliente?\nS - Sí\nN - No\nC - Cancelar\n").upper() 
            while elegir!="S" and elegir!="N" and elegir!="C":
                    print("\n\n------------------------\nPor favor, ingrese una de las opciones especificadas\n------------------------\n\n")
                    elegir= input ("Desea: \n S - Sí\nN - No\nC - Cancelar\n").upper()


                #si elige S elimina
            if elegir=="S":
                #hace una lista de todas las lineas del archivo, y reescribe el archivo salteando la linea ignorada
                    with open("clientes.txt", "r+") as f:
                        d = f.readlines()
                        f.seek(0)
                        for i in d:
                            if i != esta:
                                f.write(i)
                        f.truncate()

            if elegir=="N":
                    print("\nNo se ha modificado al cliente con DNI: " +dni+"\n")
                    menuCliente()

            if elegir=="C":
                menuCliente()

            # estado del cliente
        
        if choice=="D":  
            dni= ingresoDNI()
            esta=buscarDNI(dni) #esta trae la linea entera a borrar
            #print(esta)

            if "Estado: 0" in esta:
                print("El cliente "+ dni+" no tiene deudas")
            else:
                print("El cliente "+ dni+" debe la película con el : "+ esta[esta.find("codigo"):]+"\n\n")  ##OJO ACA, ASUMO QUE EL CODIGO TIENE 4 CARACTERES
        
        menuCliente()
    menuCliente()