def muestromenu ():
  print("\n\n**********************************************************\n")
  print("0- Gestión de alquiler de películas \n1- Gestión de clientes\n2- Gestión de Películas\n4- Salir")


def prestamopelicula():
  print("\n ------- Gestión de Préstamo de Películas ------- \n")
  print("\nDesea:\n0- Buscar peliculas \n1- Alquilar una película \n2- Devolver una película\n3- Salir" )


def gestionclientes():
    
    def menuCliente():
        print("\n ------- Gestión de Clientes ------- \n")
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
        
        if choice=="X":
            muestromenu ()
    
    menuCliente()





def gestionpelicula():
    print("\n ------- Gestión de Películas ------- \n")
   
    choice= input ("Desea: \n A - Dar de alta una película \n B - Consultar datos de una película \n C - Modificar una película \n D - Eliminar una película \n X - Volver al menú anterior\n Selección: ").upper()
    while choice!="A" and choice!="B" and choice!="C" and choice!="D" and choice!="X":
        print("\n\n------------------------\nPor favor, ingrese una de las opciones especificadas\n------------------------\n\n")
        choice= input ("Desea: \n A - Dar de alta una película \n B - Consultar datos de una película \n C - Modificar una película \n D - Eliminar una película \n X - Volver al menú anterior\n Selección: ").upper()
    print(choice)
    if choice=="A":
        def altaPelicula():
            with open("peliculas.txt", "r+") as archi:
                contenido = archi.readlines()
                while True:
                    try:
                        codigoPel = input("Ingrese el código de barra de la película que desea dar de alta: ")
                    except ValueError:
                        print("El código de barras debe ser una combinación de números")
                    else:
                        if codigoPel.isnumeric():
                            break
                        else:
                            print ("El código de barras debe ser una combinación de números")
                existe = 0
                for parte in contenido:
                    renglon = parte.split(",")
                    if codigoPel == renglon[0]:
                        existe = 1
                if existe == 1:
                    print("Ya existe una película con ese código")
                else:
                    nombrePel = input("Ingrese el nombre de la película: ")
                    generoPel = input("Ingrese el género: ")
                    print("Verifique los datos ingresados. Código:", codigoPel, "Nombre:", nombrePel, "Género:", generoPel)
                    seguro = input("Si está seguro escriba S, de lo contrario presione otra tecla: ").lower()
                    
                    if seguro == "s":
                        archi.write(codigoPel + "," + nombrePel + "," + generoPel + "," + "0" + "\n")
                        print ("Se ha dado de alta la película")
                    else:
                        print("Se ha cancelado la operación")
        altaPelicula()               
    if choice=="B":                   
        def consultarPelicula():
            with open("peliculas.txt", "r") as rArchi:
                while True:
                    try:
                        codigoPelicula = input("Ingrese el código de la película que desea consultar: ")
                    except ValueError:
                        print("El código de barras debe ser una combinación de números")
                    else:
                        if codigoPelicula.isnumeric():
                            break
                        else:
                            print ("El código de barras debe ser una combinación de números")
                contenido = rArchi.readlines()
                encontrado = 0
                for linea in contenido:
                    renglon = linea.split(",")
                    if renglon[0] == codigoPelicula:
                        encontrado = 1
                        if len(renglon) == 4:
                            print("Codigo de película:", renglon[0], "\ Nombre:", renglon[1], "\ Género:", renglon[2], "\ No se encuentra alquilada")
                        else:
                            print("Codigo de película:", renglon[0], "\ Nombre:", renglon[1], "\ Género:", renglon[2], "\ En alguiler", "\ Dni:", renglon[4])
                    else:
                        continue
                if encontrado == 0:
                    print("No existe una película con ese código")

        consultarPelicula()
    if choice=="C":
        def modificarPelicula():
            with open("peliculas.txt", "r+") as archi:
                with open("auxiliar.txt", "w") as aArchi:
                    while True:
                        try:
                            codigoPeli = input("Ingrese el código de la película que desea modificar: ")
                        except ValueError:
                            print("El código de barras debe ser una combinación de números")
                        else:
                            if codigoPeli.isnumeric():
                                break
                            else:
                                print ("El código de barras debe ser una combinación de números")
                    peliculas = archi.readlines()
                    encontrada = 0
                    for partes in peliculas:
                        renglones = partes.split(",")
                        if renglones[0] == codigoPeli:
                            print("Ingrese los siguientes datos como quiere guardarlos")
                            while True:
                                try:
                                    nuevoCod = input("Ingrese el código de la película que desea modificar: ")
                                except ValueError:
                                    print("El código de barras debe ser una combinación de números")
                                else:
                                    if nuevoCod.isnumeric():
                                        break
                                    else:
                                        print ("El código de barras debe ser una combinación de números")
                            nuevoNom = input("Ingrese el nombre de la película: ")
                            nuevoGen = input("Ingrese el género de la película: ") #agregar para que pida si esta prestada esos datos
                            aArchi.writelines(nuevoCod + "," + nuevoNom + "," + nuevoGen + "," + "0" + "\n")
                            encontrada = 1
                        else:
                            aArchi.writelines(partes)
                    if encontrada == 1:
                        print ("La película ha sido modificada")
                    else:
                        print("No se ha encontrado una película con ese código")
                    aArchi.close()
                archi.close()
            with open("auxiliar.txt", "r") as copia:
                with open("peliculas.txt", "w") as original:
                    for registro in copia:
                        original.write(registro)
        modificarPelicula()
    if choice=="D":
        def eliminarPelicula():
            with open("peliculas.txt", "r+") as archi:
                with open("auxiliar.txt", "w") as aArchi:
                    while True:
                        try:
                            codigoPeli = input("Ingrese el codigo de la pelicula que desea eliminar: ")
                        except ValueError:
                            print("El código de barras debe ser una combinación de números")
                        else:
                            if codigoPeli.isnumeric():
                                break
                            else:
                                print ("El código de barras debe ser una combinación de números")
                    peliculas = archi.readlines()
                    encontrada = 0
                    for partes in peliculas:
                        renglones = partes.split(",")
                        if renglones[0] != codigoPeli:
                            aArchi.writelines(partes)
                        else:
                            encontrada = 1
                    aArchi.close()
                archi.close()
            with open("auxiliar.txt", "r") as copia:
                with open("peliculas.txt", "w") as original:
                    for registro in copia:
                        original.write(registro)
                    original.close()
                copia.close()
            if encontrada == 1:
                print("La película ha sido eliminada")
            else:
                print("No pudimos encontrar el código ingresado")
        eliminarPelicula()
    if choice=="X":
        muestromenu()

    


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
def buscarpeli(nombrepeli):
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
    
    #ingreso y validación de DNI
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
    #validación de existencia de cliente
    def buscarDNI(entrada):
    
            file1 = open("clientes.txt", "r")
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
    
    documento = ingresoDNI()
    datosUser=buscarDNI(documento)
    if len(datosUser)>0:
        dni=documento

    ##validacion de que el usuario no tenga alquilada una pelicula
    if "Estado: 1" in datosUser:
        print("El usuario ya tiene un alquiler registrado")
    else:
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
        
        with open("peliculas.txt", "r+") as archi:
            with open("auxiliar.txt", "w") as qArchi:
                
                peliculas = archi.readlines()
                for partes in peliculas:
                    renglones = partes.split(",")
                    if codigoPeli == renglones[0]:
                        if renglones [3] == "1":
                            qArchi.writelines(partes)
                            print(renglones[1], "está alquilado")
                        else:
                            qArchi.writelines(renglones[0] + "," + renglones[1] + "," + renglones[2] + "," + "1" + "," + str(dni) +"\n")
                            print("Gracias por alquilar ", renglones[1]," con nosotros")
                    else:
                        qArchi.writelines(partes)
                        print("Esa peli no la tenemos")
            qArchi.close()
        archi.close()
        with open("auxiliar.txt", "r") as copia:
            with open("peliculas.txt", "w") as original:
                for registro in copia:
                    original.write(registro)
            original.close()
        copia.close()

    #### Asignación de pelicula alquilada a cliente

        def buscarPelienCliente(entrada):
            file1 = open("clientes.txt", "r")
            flag = 0
            index = 0
            for line in file1:  
                index += 1 
                if entrada in line:
                    flag = 1
                    texto=line
                    break  
            return texto  
            file1.close() 
        esta=buscarPelienCliente(dni) # trae la linea entera del cli que alquiló la peli
        
        pte1=esta[:esta.find("Estado")-2] # almacena lo anterior al Estado
        NEstado= ", Estado: 1, codigo: "+codigoPeli

        modificado=pte1+NEstado
        #hace una lista de todas las lineas del archivo, y reescribe el archivo salteando la linea ignorada
        with open("clientes.txt", "r+") as f:
            d = f.readlines()
            f.seek(0)
            for i in d:
                if i != esta: #ignora la linea modificada
                    f.write(i)
                if i == esta: #donde está la linea modif, agrega la linea nueva
                    f.write(modificado+"\n")
                
            f.truncate()

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
            existe = 0
            for partes in peliculas: 
                renglones = partes.split(",")
                if codigoPeli == renglones[0]:
                        aArchi.writelines(renglones[0] + "," + renglones[1] + "," + renglones[2] + "," + "0" +"\n")
                        print("Gracias por devolver la película")
                else:
                        aArchi.writelines(partes)
            if existe == 0:
                print("No existe una película que coincida con el código ingresado")
        aArchi.close()
    archi.close()
    with open("auxiliar.txt", "r") as copia:
            with open("peliculas.txt", "w") as original:
                for registro in copia:
                    original.write(registro)
            original.close()
    copia.close()
 
  ##Modificación de alquiler en cliente
        #Busca el codigo de la pelicula en el txt de clientes y devuelve la linea entera de datos
   

    def buscarPelienCliente(entrada):
        file1 = open("clientes.txt", "r")
        flag = 0
        index = 0
        for line in file1:  
            index += 1 
            if entrada in line:
                flag = 1
                texto=line
                break  
        return texto  
        file1.close() 
    esta=buscarPelienCliente(codigoPeli) # trae la linea entera del cli que alquiló la peli

    pte1=esta[:esta.find("Estado")-2] # almacena lo anterior al Estado
    NEstado= ", Estado: 0, codigo: 0"

    modificado=pte1+NEstado
    #hace una lista de todas las lineas del archivo, y reescribe el archivo salteando la linea ignorada
    with open("clientes.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i != esta: #ignora la linea modificada
                f.write(i)
            if i == esta: #donde está la linea modif, agrega la linea nueva
                f.write(modificado+"\n")
            
        f.truncate()
	

#### Menú
opcion = 0
while opcion != 4:
	muestromenu()
	while True:
		try:
			opcion = int(input("\nElija una opción: "))
		except ValueError:
			print("Debe ingresar una opción válida")
		else:
			if opcion != 0 and opcion != 1 and opcion != 2 and opcion != 4:
				print("Debe ingresar una opción válida")
			else:
				break
	if opcion == 0:
		prestamopelicula()
		while True:
			try:
				opcionpelicula = int(input("Elija una opción: "))
			except ValueError:
				print ("Debe ingresar una opción válida")
			else:
				if opcionpelicula != 0 and opcionpelicula != 2 and opcionpelicula != 2 and opcionpelicula != 3:
					print("Debe ingresar una opción válida")
				else:
					break
		if opcionpelicula == 0:
			nombrepeli = input("Ingrese el nombre de la película: ").lower()
			buscarpeli(nombrepeli)
		elif opcionpelicula == 1:
			alquilarpeli()
		elif opcionpelicula == 2:
			devolverpeli()
		elif opcionpelicula == 3:
			continue
       
	if opcion==1:
		gestionclientes()
	if opcion==2:
		gestionpelicula()
