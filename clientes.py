

#faltaria una opcion para salir y volver al menú anterior

choice= input ("Desea: \n A - Dar de alta un cliente \n B - Modificar teléfono o dirección del cliente \n C - Eliminar cliente\n X - Volver al menú anterior\n Selección: ").upper()

#validacion de seleccion de menu cliente

while choice!="A" and choice!="B" and choice!="C" and choice!="X":
    print("\n\n------------------------\nPor favor, ingrese una de las opciones especificadas\n------------------------\n\n")
    choice= input ("Desea: \n A - Dar de alta un cliente \n B - Modificar teléfono o dirección del cliente \n C - Eliminar cliente\n X - Volver al menú anterior\n Selección: ").upper()
