
#faltaria una opcion para salir y volver al menú anterior

#validacion de seleccion de menu cliente
from types import DynamicClassAttribute


def menuCliente():
    
    choice= input ("Desea: \n A - Dar de alta un cliente \n B - Modificar teléfono o dirección del cliente \n C - Eliminar cliente\n X - Volver al menú anterior\n Selección: ").upper()

    while choice!="A" and choice!="B" and choice!="C" and choice!="X":
        print("\n\n------------------------\nPor favor, ingrese una de las opciones especificadas\n------------------------\n\n")
        choice= input ("Desea: \n A - Dar de alta un cliente \n B - Modificar teléfono o dirección del cliente \n C - Eliminar cliente\n X - Volver al menú anterior\n Selección: ").upper()

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
############ funcion para revisar si en di estab en la bd
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
   

    if choice=="A":
        
            entrada=ingresoDNI()
                    #chequear si dni está en la bd    32456534
            with open("clientes.txt") as C:
                esta=-1
                for line in C:
                    esta=line.find("DNI: "+entrada)
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

                    f.write("DNI: "+entrada+ ", Nombre Completo:"+nom +", Telefono:"+ tel + ", Direccion: "+dir + ", Estado:  0, codPelicula:0\n")

    
    ##eliminar cliente
    if choice=="C":
       dni= ingresoDNI()
       print(dni)
       esta=buscarDNI(dni) #esta trae la linea entera a borrar
       #print(esta)
                                             
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



    
menuCliente()