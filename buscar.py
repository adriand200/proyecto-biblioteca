from agregar import buscar_libro, mostrar_genero, buscar_autor, pedir_libro, agregar_libro, mostrar_libros_recomendados, devolver_libro
from libreria import Biblioteca

def menu():
    while True: 
        print("Bienvenido a la biblioteca") #Menu principal
        print("1. Buscar libro")
        print("2. Buscar libros por género")
        print("3. Buscar autor")
        print("4. Pedir libro")
        print("5. Devolver libro")
        print("6. Agregar libro")
        print("7. Mostrar libros recomendados")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            buscar_libro()
        elif opcion == "2":
            mostrar_genero()
        elif opcion == "3":
            buscar_autor()
        elif opcion == "4":
            pedir_libro()
        elif opcion == "5":
            devolver_libro()
        elif opcion == "6":
            codigo = input("Asignar codigo para agregar un nuevo libro: ")
            if codigo == "123":
                agregar_libro()
            else:   
                print("El código no es correcto, no se puede agregar el libro.") 
        elif opcion == "7":
            mostrar_libros_recomendados()
        elif opcion == "8":
            print("Saliendo de la biblioteca...")
            return
        else:
            print("Opción no válida. Intente de nuevo.")

#Iniciar el menú
menu()