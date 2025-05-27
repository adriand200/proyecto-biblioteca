from libreria import Biblioteca
import datetime
import unicodedata

def mostrar_genero(): # Mostrar los géneros disponibles
    genero = (input("Selecione algun genero: ")) # Pedir el género al usuario
    if (genero) in Biblioteca["Generos"]: # Verificar si el género existe 
        print(f"Libros de {genero}:") # Mostrar los libros del género
        for titulo in Biblioteca["Generos"][genero]["Libros"]: # Acceder a los libros del género
            print(f"Titulo: {titulo}") # Mostrar el título del libro
    else:
        print("Este genero no existe en la biblioteca")

def buscar_libro():
    titulo_buscado = input("Escribe el título del libro: ")
    encontrado = False
    for genero, info in Biblioteca["Generos"].items(): # Acceder a los géneros
        for titulo in info["Libros"]: # Acceder a los libros del género
            if titulo == titulo_buscado:
                datos = info["Libros"][titulo] # Acceder a los datos del libro
                print(f"Detalles de '{titulo}' (Género: {genero}):")
                print(f"Autor: {datos['Author']}")
                print(f"Codigo del libro: {datos['Codigo']}")
                print(f"Páginas: {datos['Paginas']}")
                print(f"Año: {datos['Año']}")
                print(f"Etiquetas: {', '.join(datos['etiquetas'])}")
                encontrado = True
    if not encontrado: # Si no se encuentra el libro
        print("Libro no encontrado en ningún género.")
        
def buscar_autor():# Buscar un autor
    autor_buscado = input("Escribe el nombre del autor: ")
    encontrado = False
    for genero, info in Biblioteca["Generos"].items(): # Acceder a los géneros
        libros = info["Libros"] # Acceder a los libros del género
        for titulo, datos in libros.items():# Acceder a los datos del libro
            # Normaliza ambos para comparar correctamente
            if datos["Author"] == autor_buscado:
                print(f"Detalles de '{titulo}' (Género: {genero}):")
                print(f"Autor: {datos['Author']}")
                print(f"Páginas: {datos['Paginas']}")
                print(f"Año: {datos['Año']}")
                print(f"Etiquetas: {', '.join(datos['etiquetas'])}")
                encontrado = True
    if not encontrado:
        print("Autor no encontrado en ningún libro.")

# Pedir un libro prestado
def pedir_libro(): 
    libro = input("Escribe el título del libro que deseas pedir: ")
    
    if libro not in Biblioteca["Libros disponibles"]: # Verificar si el libro está disponible
        print("Este libro no está disponible.")
    else:
        fecha_prestamo = datetime.date.today() # Fecha de hoy
        fecha_devolucion = fecha_prestamo + datetime.timedelta(days=15) # 15 días de préstamo
        usuario = input("Escribe tu nombre: ")
        
        Biblioteca["Libros prestados"][libro] = { # Agregar el libro a los libros prestados
            "Fecha de prestamo": fecha_prestamo,
            "Fecha de devolucion": fecha_devolucion,
            "Usuario": usuario,
            "Estado": "Pendiente"
        }

        Biblioteca["Libros disponibles"].remove(libro) # Eliminar el libro de los libros disponibles
        print(f"Libro '{libro}' prestado a {usuario}. Fecha de devolución: {fecha_devolucion}.") # Mensaje de confirmación

def devolver_libro(): # Devolver un libro prestado
    libro =input("Escribe el título del libro que deseas devolver: ")

    if libro in Biblioteca["Libros prestados"]:
        del Biblioteca["Libros prestados"][libro] # Eliminar el libro de los libros prestados
        Biblioteca["Libros disponibles"].append(libro) # Agregar el libro a los libros disponibles
        print(f"Libro '{libro}' devuelto.") 
    else:
        print("Este libro no está en préstamo.")


def agregar_libro(): # Agregar un nuevo libro a la biblioteca
    titulo = input("Escribe el título del libro: ")
    autor = input("Escribe el autor del libro: ")
    paginas = int(input("Escribe el número de páginas: "))
    año = int(input("Escribe el año de publicación: "))
    etiquetas = input("Escribe las etiquetas: ")
    genero_agregado = input("Escribe el género del libro: ")

    Biblioteca["Generos"][genero_agregado]["Libros"][titulo] = { # Acceder a los géneros y agrega el libro
        "Author": autor,
        "Paginas": paginas,
        "Año": año,
        "etiquetas": etiquetas
    }
    print(f"Libro '{titulo}' agregado al género '{genero_agregado}'.")
    
# Mostrar los libros recomendados
def mostrar_libros_recomendados():
    print("Libros recomendados:")
    for libros_recomendados in Biblioteca["Libros recomendados"]:
        print(f"- {libros_recomendados}")
