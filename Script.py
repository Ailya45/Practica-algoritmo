import PyPDF2
from pathlib import Path

def Escribir(nom_archivo):
    try:
        with open(nom_archivo +'.txt', 'w', encoding="utf-8") as archivo:
            archivo.write(input("Ingrese lo que quiere escribir en el archivo: "))
            print("Archivo creado con exito!")
    except IOError as e:
        print(f"Error al escribir el archivo: {e}")

def Leer(nom_archivo):
    try:
        with open(nom_archivo + '.txt', 'r', encoding="utf-8") as archivo:
            contenido = archivo.read()
            print(contenido)
            lineas = 0
            palabras = 0
            caracteres = 0
            if contenido:
                lineas = len(contenido.splitlines())
                palabras = len(contenido.split())
                caracteres = len(contenido)
            
            else: # Archivo vacío
                lineas = 0
                palabras = 0
                caracteres = 0

            print(f"Líneas: {lineas}")
            print(f"Palabras: {palabras}")
            print(f"Caracteres: {caracteres}")

    except FileNotFoundError:
            print(f"Error: El archivo '{nom_archivo}.txt' no fue encontrado.")
    except IOError as e:
            print(f"Error al leer el archivo: {e}")

def Agregar(nom_archivo):
    try:
        with open(nom_archivo + '.txt', 'a', encoding="utf-8") as archivo:
            archivo.write('\n' + input("Ingrese el nuevo texto:"))
            print("Contenido agregado con exito!")
    except IOError as e:
        print(f"Error al agregar contenido al archivo: {e}")

def leer_pdf(ruta_archivo):
    try:
        with open(ruta_archivo, 'rb') as archivo:
            lector_pdf = PyPDF2.PdfReader(archivo)

            for pagina in lector_pdf.pages:
                texto = pagina.extract_text()
                print(texto.strip())
                
    except FileNotFoundError:
        print(f"Error: El archivo '{ruta_archivo}' no existe.")
    except PermissionError:
        print(f"Error: No tienes permiso para leer '{ruta_archivo}'.")
    except PyPDF2.errors.PdfReadError:
        print(f"Error: El archivo '{ruta_archivo}' no es un PDF válido o está corrupto.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")        

def Menu():
    print("Seleccione una opcion del siguiente menu: ")
    print("1. Escribir archivo .txt nuevo.")
    print("2. Leer archivo .txt y contar cantidad de lineas y carateres.")
    print("3. Agregar contenido a un archivo .txt.")
    print("4. Leer un archivo .pdf.")
    print("5. Salir")
    selection = input()

    if selection == "1":
        nom_archivo = input("Ingrese el nombre del archivo que quiere crear: ")
        Escribir(nom_archivo)
    elif selection == "2":
        nom_archivo = input("Ingresa el nombre del archivo que quiere leer: ")
        Leer(nom_archivo)
    elif selection == "3":
        nom_archivo = input("Ingrese el nombre del archivo que quiere modificar: ")
        Agregar(nom_archivo)
    elif selection == "4":
        nom_archivo = input("Ingrese la ruta completa del archivo PDF: ").strip()
        archivo_pdf = Path(nom_archivo)
        
        if not archivo_pdf.exists():
            print("El archivo no existe.")
        else:
            leer_pdf(archivo_pdf)    
    elif selection == "5":
        print("\nSaliendo del programa")
        return
    else:
        print("Opción invalida, intente de nuevo")

    Menu()
    
if __name__ == "__main__":
    Menu()
