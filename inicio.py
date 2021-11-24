def muestromenu ():
  print("\n\n**********************************************************\n")
  print("0- Gestión de películas \n1- Gestión de clientes")


def prestamopelicula():
  print("\n ------- Gestión de Préstamo de Películas ------- \n")
  print("\nDesea:\n0- Buscar peliculas \n1- Alquilar una película \n2- Devolver una película\n" )


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
    ############ funcion para revisar si el dni estab en la bd, devuelve la linea de info si está
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





def gestionpelicula():
    print("\n ------- Gestión de Películas ------- \n")
    print("\n0-Alta de película \n1- Consultar una pelicula \n2- Modificar libro \n3- eliminar libro")

######punto 0 Falta diferenciar los prestados de los disponibles
def mostrarpeli():
  with open("peliculas.txt","r") as jArchi:
        linea = jArchi.readline()
        while linea != "":
          renglon = linea.split(',')
          return renglon
          linea = jArchi.readline()
        jArchi.close()


##### punto 1A
def buscarpeli():
  with open("peliculas.txt","r") as wArchi:
    linea = wArchi.readlines()
    encontrado=0
    for renglon in linea:
      parte = renglon.split(',')  
      if nombrepeli in parte [1]:
        encontrado=1
        if parte [3] == "1":
          print("\n"+nombrepeli, "está alquilado")
        else:
          print("\n"+nombrepeli, " está disponible")
    if encontrado ==0:
      print("No tenemos esa película")
    wArchi.close()


##### punto 1B
def alquilarpeli():
	with open("peliculas.txt", "r+") as archi:
		with open("auxiliar.txt", "w") as qArchi:
			while True:
				try:
					codigoPeli = input("Ingrese el codigo de la pelicula que desea alquilar: ")
				except ValueError:
					print("El código de barras debe ser una combinación de números")
				else:
					if codigoPeli.isnumeric():
						break
					else:
						print ("El código de barras debe ser una combinación de números")
			peliculas = archi.readlines()
			for partes in peliculas:
				renglones = partes.split(",")
				if codigoPeli == renglones[0]:
					qArchi.writelines(renglones[0] + "," + renglones[1] + "," + renglones[2] + "," + "1" + "," + str(dni) +"\n")
					print("Gracias por alquilar ", nombrepeli,"con nosotros")
				else:
					qArchi.writelines(partes)
		qArchi.close()
	archi.close()
	with open("auxiliar.txt", "r") as copia:
		with open("peliculas.txt", "w") as original:
			for registro in copia:
				original.write(registro)
		original.close()
	copia.close()


##### punto 1C
def devolverpeli():
	with open("peliculas.txt", "r+") as archi:
		with open("auxiliar.txt", "w") as aArchi:
			while True:
				try:
					codigoPeli = input("Ingrese el codigo de la pelicula que desea devolver: ")
				except ValueError:
					print("El código de barras debe ser una combinación de números")
				else:
					if codigoPeli.isnumeric():
						break
					else:
						print ("El código de barras debe ser una combinación de números")
			peliculas = archi.readlines()
			for partes in peliculas:
				renglones = partes.split(",")
				if codigoPeli == renglones[0]:
					aArchi.writelines(renglones[0] + "," + renglones[1] + "," + renglones[2] + "," + "0" +"\n")
					print("Gracias por devolver la película")
				else:
					aArchi.writelines(partes)
		aArchi.close()
	archi.close()
	with open("auxiliar.txt", "r") as copia:
		with open("peliculas.txt", "w") as original:
			for registro in copia:
				original.write(registro)
		original.close()
	copia.close()
	#Aca mismo


#### Menú
opc = 0
while opc != 4:
    muestromenu()
    opcion = int(input("\nElija una opción: "))
    if opcion == 0:
        prestamopelicula()
        opcionpelicula = int(input("Elija una opción: "))
        if opcionpelicula == 0:
            nombrepeli = input("Ingrese el nombre de la película: ")
            buscarpeli()
        elif opcionpelicula == 1:
            nombrepeli = input("¿Qué película quiere alquilar?: ")
            dni = int(input("¿Cual es su dni?: "))
            alquilarpeli()
        elif opcionpelicula == 2:
            devolverpeli()
    if opcion==1:
        gestionclientes()
