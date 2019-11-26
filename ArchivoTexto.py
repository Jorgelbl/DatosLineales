#se importa la libreria pickle
import pickle

#se declara la clase archivos textos
class ArchivoTexto:

    #metodo para guardar archivos textos
    def guardarArchivo(self, Archivo, lista):
        #guardamos datos al archivo texto
        file = open(Archivo, 'w')
        pickle.dump(lista, file)
        file.close()
        #se elimina
        del (file)

    #metodo para abrir archivos textos
    def abrirArchivo(self, Archivo):
        #abrimos el archivo texto
        file = open(Archivo, 'r')
        lista = pickle.load(file)
        file.close()
        del (file)
        #se retornan valores
        return lista

#se ejecuta el metodo principal
def main():
    #se guardan valores en una lista
    Lista = ['alondra', 'beto', 'casas', 'dados', 'elote']
    #se declara la clase pricipal
    archivo_dos = ArchivoTexto()
    #se guardan valores de la lista a un archivo texto
    archivo_dos.guardarArchivo('Texto.txt', Lista)
    #se muestran resultados del archivo texto
    mostrar = archivo_dos.abrirArchivo('Texto.csv')
    print(mostrar)

if __name__ == '_main_':
    main()
