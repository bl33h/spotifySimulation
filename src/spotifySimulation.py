#/**
 #* *Copyright (C), 2022-2023, Sara Echeverria (bl33h)
    # *@author Sara Echeverria
    # *FileName: spotifySimulation
    # @version: I
    #- Creacion: 25/04/2021
    #- Ultima modificacion: 20/07/2022

# Definicion
def Exhibir_tabla( ):
    print(header[0], end = "\t\t\t")
    for i in range(1, 7):
        print(header[i], end = "\t")
    print()

    for canciones in registros:
        print(canciones, end = "\t\t\t")
        for dato in registros[canciones]:
            print(registros[canciones][dato], end = "\t")
        print()

# Utilizar archivo CSV y separación
with open("SongsRegister.csv", "r", encoding = "latin-1") as myFile:
    registros = {}
    
    header = myFile.readline().rstrip().split(",")
    
    for line in myFile.readlines():
        canciones = line.rstrip().split(",")
        
        registros[ canciones[0] ] = { header[1] : (canciones[1]),
                                 header[2] : (canciones[2]),
                                 header[3] : (canciones[3]),
                                 header[4] : (canciones[4]),
                                 header[5] : int(canciones[5]),
                                 header[6] : (canciones[6]),
                                 header[7] : int(canciones[7])}
        
# Booleano        
continuar = True

# Ciclo while con las opciones en el menú
while continuar:
    print("REGISTROS DE CANCIONES EN CASO DE EMERGENCIA\n")
    print("1. Mostrar registros")
    print("2. Modificar registro")
    print("3. Agregar un nuevo registro")
    print("4. Mostrar reporte")
    print("5. Cerrar programa")
    
    Opciones = input("Ingrese el número de la opción que desea ejecutar: ")
    
    if Opciones == "1": #Mostrar registros
        print()
        Exhibir_tabla()
        print()
        
    elif Opciones == "2": #Modificar datos de registro
        print()
        canciones = input("Ingrese la canción que desea modificar: ")
        
        if canciones in registros.keys():
            datosRegistro = {}
            datosRegistro["Nombre Canción"] = (input("Nombre Canción: "))
            datosRegistro["Fecha"] = (input("Fecha en formato dd/mm/aaaa: "))
            datosRegistro["Género"] = (input("Género: "))
            datosRegistro["Duración"] = str(input("Ingrese la duración de la canción en el formato mm:ss"))
            datosRegistro["Autor"] = (input("Autor: "))
            datosRegistro["Reproducciones al día"] = int(input("Reproducciones al día: "))
            datosRegistro["Playlist"] = (input("Playlist: "))
            datosRegistro["Calificación"] = int(input("Calificación: "))
            registros[canciones] = datosRegistro
        
    elif Opciones == "3": #Agregar registro
        print()
        
        nuevoRegistro = input("Ingrese la canción nueva: ")
        
        if nuevoRegistro in registros.keys():
                print("ERROR, registro existente.")
        else:
            datosRegistro = {}
            datosRegistro["Fecha"] = (input("Fecha en formato dd/mm/aaaa: "))
            datosRegistro["Género"] = (input("Género: "))
            datosRegistro["Autor"] = (input("Autor: "))
            datosRegistro["Duración"] = str(input("Ingrese la duración de la canción en el formato mm:ss "))
            datosRegistro["Reproducciones al dia"] = int(input("Reproducciones al día: "))
            datosRegistro["Playlist"] = (input("Playlist: "))
            datosRegistro["Calificación"] = int(input("Calificación: "))
            registros[nuevoRegistro] = datosRegistro
                
        print()
    
    elif Opciones == "4": # Imprimir reporte
            # Canción más larga
            c = []
            for element in registros:
                cancion_mas_larga = []
                cancion_mas_larga.append(registros[element]["Duración"])
                cancion_mas_larga.append(element)
                c.append(cancion_mas_larga)
            c.sort (reverse = True)
            print ("La canción más larga es: ")
            print ((c[0]))
            
        
    elif Opciones == "5": # Cerrar programa
        
        with open("Registros_canciones.csv", "w") as myFile:
            myFile.write(header[0] + ",")
            myFile.write(header[1] + ",")
            myFile.write(header[2] + ",")
            myFile.write(header[3] + ",")
            myFile.write(header[4] + ",")
            myFile.write(header[5] + ",")
            myFile.write(header[6] + ",")
            
            for canciones in registros:
                myFile.write(canciones)
                for dato in registros[canciones]:
                    valor = str(registros[canciones][dato])
                    myFile.write("," + valor)
                myFile.write("\n")
            
        
        continuar = False
    else:
        print("ERROR: Debe ingresar un numero del 1 al 5.")
        print()
