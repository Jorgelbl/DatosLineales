
#metodo para leer archivos textos
def lectura_De_Archivos_Texto():
    fichero = open("Texto.txt.txt", "r")
    fichero = fichero.read()
    print(fichero)

#metodo para escribir archivos textos
def Escritura_De_Archivos_Texto():
    fichero = open("Texto.txt.txt", "w")
    fichero.write("nueva linea 1\n")
    fichero.write("nueva linea 2\n")
    fichero.close()



lectura_De_Archivos_Texto()
Escritura_De_Archivos_Texto()
