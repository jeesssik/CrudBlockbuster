def gestionpelicula():    
    def altaPelicula():
            with open("peliculas.txt", "r+") as archi:
                contenido = archi.readlines()
                while True:
                    try:
                        codigoPel = input("Ingrese el código de barra de la película que desea dar de alta")
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
                    nombrePel = input("Ingrese el nombre de la película")
                    generoPel = input("Ingrese el género")
                    print("Verifique los datos ingresados. Código:", codigoPel, "Nombre:", nombrePel, "Género:", generoPel)
                    seguro = input("Si está seguro escriba S, de lo contrario presione otra tecla")
                    seguro = seguro.lower()
                    if seguro == "s":
                        archi.write(codigoPel + "," + nombrePel + "," + generoPel + "," + "0" + "\n")
                        print ("Se ha dado de alta la película")
                    else:
                        print("Se ha cancelado la operación")
                        
                        
    def consultarPelicula():
        with open("peliculas.txt", "r") as rArchi:
            while True:
                try:
                    codigoPelicula = input("Ingrese el código de la película que desea consultar")
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

        

    def modificarPelicula():
        with open("peliculas.txt", "r+") as archi:
            with open("auxiliar.txt", "w") as aArchi:
                while True:
                    try:
                        codigoPeli = input("Ingrese el código de la película que desea modificar:")
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
                                nuevoCod = input("Ingrese el código de la película que desea modificar:")
                            except ValueError:
                                print("El código de barras debe ser una combinación de números")
                            else:
                                if nuevoCod.isnumeric():
                                    break
                                else:
                                    print ("El código de barras debe ser una combinación de números")
                        nuevoNom = input("Ingrese el nombre de la película:")
                        nuevoGen = input("Ingrese el género de la pelícyla:") #agregar para que pida si esta prestada esos datos
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


    def eliminarPelicula():
        with open("peliculas.txt", "r+") as archi:
            with open("auxiliar.txt", "w") as aArchi:
                while True:
                    try:
                        codigoPeli = input("Ingrese el codigo de la pelicula que desea eliminar")
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
