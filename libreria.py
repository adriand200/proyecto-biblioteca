import datetime 
# Definición de la biblioteca

Biblioteca = { 
    "Nombre" : "Biblioteca",
    "Horario" : "Lunes a viernes de 9:00 am a 6:00pm",
    "Generos" : {
        "Infantil" :{ 
            "Ubicacion: " : "Estanteria 1A",
            "Codigo de libros" : 0.0,
            "Libros" :{
                "El Principito" : {
                    "Author": "Antoine de Saint-Exupéry",
                    "Codigo": 0.1,
                    "Paginas": 96,
                    "Año" : 1946,
                    "etiquetas" : ["Clasico", "Filosofia", "Niños"]
                },
                "Matilda":{
                    "Author": "Roald Dahl",
                    "Codigo": 0.2,
                    "Paginas": 240,
                    "Año" : 1988,
                    "etiquetas" : ["fantasía", "niñez", "lectura"]
                },
                "Charlie y la fábrica de chocolate":{
                    "Author": "Roald Dahl",
                    "Codigo": 0.3,
                    "Paginas": 192,
                    "Año" : 1964,
                    "etiquetas" : ["Aventura", "dulces", "familia", "lecciones"]
                },
                "Donde viven los monstruos":{
                    "Author": "Maurice Sendak",
                    "Codigo": 0.4,
                    "Paginas": 48,
                    "Año" : 1963,
                    "etiquetas" : ["Imaginación", "emociones", "fantasía"]
                },
                "Cuentos por teléfono":{
                    "Author": "Gianni Rodari",
                    "Codigo": 0.5,
                    "Paginas": 192,
                    "Año" : 1962,
                    "etiquetas" : ["Humor", "creatividad", "relatos cortos"]
                },
                "El Grúfalo":{
                    "Author": "Julia Donaldson",
                    "Codigo": 0.6,
                    "Paginas": 32,
                    "Año" : 1999,
                    "etiquetas" : ["Animales", "rima", "valentía", "ingenio"]
                },
                "La telaraña de Carlota":{
                    "Author": "E. B. White",
                    "Codigo": 0.7,
                    "Paginas": 192,
                    "Año" : 1952,
                    "etiquetas" : ["Amistad", "animales", "granja", "vida y muerte"]
                },
                "Caperucita Roja":{
                    "Author": "Hermanos Grimm / Perrault",
                    "Codigo": 0.8,
                    "Paginas": 20,
                    "Año" : "Tradicional",
                    "etiquetas" : ["Peligro", "obediencia", "cuentos de hadas"]
                }
            }
        },
        "Fantasia":{
            "Ubicacion" : "Estantería B2",
            "Codigo de libros" : 1.0,
            "Libros" : {
                "El Hobbit":{
                    "Author": "J.R.R. Tolkien",
                    "Codigo": 1.1,
                    "Paginas": 310,
                    "Año" : 1937,
                    "etiquetas" : ["Aventuras", "dragones", "enanos", "viaje épico"]
                },
                "El Señor de los Anillos (trilogía)":{
                    "Author": "J.R.R. Tolkien",
                    "Codigo": 1.2,
                    "Paginas": 1200,
                    "Año" : 1954-55,
                    "etiquetas" : ["Magia", "amistad", "poder", "guerra", "mitología"]
                },
                "Harry Potter (saga de 7 libros)":{
                    "Author": "J.K. Rowl",
                    "Codigo": 1.3,
                    "Paginas": 3000-800,
                    "Año" : 1997-2007,
                    "etiquetas" : ["Magia", "escuela", "amistad", "lucha entre el bien y el mal"]
                },
                "Las crónicas de Narnia":{
                    "Author": "C.S. Lewis",
                    "Codigo": 1.4,
                    "Paginas": "7 libros",
                    "Año" : 1950-1956,
                    "etiquetas" : ["Mundos paralelos", "leones parlantes", "magia"]
                },
                "Eragon (saga El Legado)":{
                    "Author": "Christopher Paolini",
                    "Codigo": 1.5,
                    "Paginas": "7 libros",
                    "Año" : 1950-1956,
                    "etiquetas" : ["Mundos paralelos", "leones parlantes", "magia"]
                },
                "Coraline":{
                    "Author": "Neil Gaiman",
                    "Codigo": 1.6,
                    "Paginas": 162,
                    "Año" : 2002,
                    "etiquetas" : ["Mundo alternativo", "valentía", "suspenso"]
                },
                "El nombre del viento":{
                    "Author": "Patrick Rothfuss",
                    "Codigo": 1.7,
                    "Paginas": 662,
                    "Año" : 2007,
                    "etiquetas" : ["Magia", "música", "leyendas", "narrador prodigio"]
                },
                "La historia interminable":{
                    "Author": "Michael Ende",
                    "Codigo": 1.8,
                    "Paginas": 400,
                    "Año" : 1979,
                    "etiquetas" : ["Imaginación", "fantasía dentro de la fantasía"]
                },
            }
        },
        "Ciencia Ficcion" : {
            "Ubicación": "Estanteria 3C",
            "Codigo de libros" : 2.0,
            "Libros" : {
                "La máquina del tiempo":{
                    "Author": "H.G. Wells",
                    "Codigo": 2.1,
                    "Paginas": 128,
                    "Año" : 1895,
                    "etiquetas" : ["Viajes temporales", "distopía", "evolución humana"]
                },
                "La guerra de los mundos":{
                    "Author": "H.G. Wells",
                    "Codigo": 2.2,
                    "Paginas": 192,
                    "Año" : 1898,
                    "etiquetas" : ["Invasión alienígena", "humanidad", "supervivencia"]
                },
                "1984":{
                    "Author": "George Orwell",
                    "Codigo": 2.3,
                    "Paginas": 328,
                    "Año" : 1949,
                    "etiquetas" : ["Totalitarismo", "vigilancia", "control social"]
                },
                "Un mundo feliz":{
                    "Author": "Aldous Huxley",
                    "Codigo": 2.4,
                    "Paginas": 288,
                    "Año" : 1932,
                    "etiquetas" : ["Manipulación genética", "control emocional", "distopía"]
                },
                "Fahrenheit 451":{
                    "Author": "Ray Bradbury",
                    "Codigo": 2.5,
                    "Paginas": 190,
                    "Año" : 1953,
                    "etiquetas" : ["Censura", "quema de libros", "rebelión cultural"]
                },
                "2001: Odisea del espacio":{
                    "Author": "Arthur C. Clarke",
                    "Codigo": 2.6,
                    "Paginas": 190,
                    "Año" : 1968,
                    "etiquetas" : ["Evolución", "inteligencia artificial", "espacio"]
                },
                "Yo, Robot":{
                    "Author": "Isaac Asimov",
                    "Codigo": 2.7,
                    "Paginas":	224,
                    "Año" : 1950,
                    "etiquetas" : ["Evolución", "inteligencia artificial", "espacio"]
                },
            }
        },
        "Terror" : {
            "Ubicación": "Estanteria 4D",
            "Codigo de libros" : 3.0,
            "Libros" : {
                "Drácula":{
                    "Author": "Bram Stoker",
                    "Codigo": 3.1,
                    "Paginas": 400,
                    "Año" : 1897,
                    "etiquetas" : ["Vampiros", "suspenso", "romántico"]
                },
                "Frankenstein":{
                    "Author": "Mary Shelley",
                    "Codigo": 3.2,
                    "Paginas": 280,
                    "Año" : 1818,
                    "etiquetas" : ["Ciencia", "creación", "monstruo"]
                },
                "El resplandor":{
                    "Author": "Stephen King",
                    "Codigo": 3.3,
                    "Paginas": 688,
                    "Año" : 1977,
                    "etiquetas" : ["Locura", "hotel embrujado", "familia"]
                },
                "Cementerio de animales":{
                    "Author": "Stephen King",
                    "Codigo": 3.4,
                    "Paginas": 560,
                    "Año" : 1983,
                    "etiquetas" : ["Resurrección", "muerte", "pérdida"]
                },
                "El exorcista":{
                    "Author":	"William Peter Blatty",
                    "Codigo": 3.5,
                    "Paginas": 400,
                    "Año" : 1971,
                    "etiquetas" : ["Demonios",	"posesión",	"exorcismo"]
                },
            }
        },
        "Aventura" : {
            "Ubicación": "Estanteria 5E",
            "Codigo de libros" : 4.0,
            "Libros" : {
                "Por quien doblan las campanas":{
                    "Author": "Ernest Hemingway",
                    "Codigo": 4.1,
                    "Paginas": 480,
                    "Año" : 1940,
                    "etiquetas" : ["Guerra", "amor", "sacrificio"]
                },
                "El viejo y el mar":{
                    "Author": "Ernest Hemingway",
                    "Codigo": 4.2,
                    "Paginas": 128,
                    "Año" : 1952,
                    "etiquetas" : ["Superación", "naturaleza", "soledad"]
                },
                "Los tres mosqueteros":{
                    "Author": "Alexandre Dumas",
                    "Codigo": 4.3,
                    "Paginas": 700,
                    "Año" : 1844,
                    "etiquetas" : ["Espadas", "honor", "amistad"]
                },
                "El conde de Montecristo":{
                    "Author":	"Alexandre Dumas",
                    "Codigo": 4.4,
                    "Paginas": 1276,
                    "Año" : 1844,
                    "etiquetas" : ["Venganza",	"traición",	"justicia"]
                },
                "La isla del tesoro":{
                    "Author":	"Robert Louis Stevenson",
                    "Codigo": 4.5,
                    "Paginas": 240,
                    "Año" : 1883,
                    "etiquetas" : ["Piratas",	"mapas",	"tesoros"]
                },
            }
        },
        "Autobiografia" : {
            "Ubicación": "Estanteria 6F",
            "Codigo de libros" : 5.0,
            "Libros" : {   
                "El diario de Ana Frank":{
                    "Author": "Ana Frank", 
                    "Codigo": 5.1,
                    "Paginas": 352,
                    "Año" : 1947,          
                    "etiquetas" : ["Guerra", "refugio", "diario"]
                }, 
                "Larga camino hacia la libertad":{
                    "Author": "Nelson Mandela",
                    "Codigo": 5.2,
                    "Paginas": 656,
                    "Año" : 1994,
                    "etiquetas" : ["Lucha", "libertad", "Sudáfrica"]
                },
                "Yo soy Malala":{
                    "Author": "Malala Yousafzai",
                    "Codigo": 5.3,
                    "Paginas": 288,
                    "Año" : 2013,
                    "etiquetas" : ["Educación", "valentía", "Pakistán"]
                },
                "El hombre en busca de sentido":{
                    "Author": "Viktor Frankl",
                    "Codigo": 5.4,
                    "Paginas": 200,
                    "Año" : 1946,
                    "etiquetas" : ["Supervivencia", "psicología", "sentido"]
                }
            }
        },
        "Romance" : {
            "Ubicación": "Estanteria 7G",
            "Codigo de libros" : 6.0,
            "Libros" : {
                "Orgullo y prejuicio":{
                    "Author": "Jane Austen",
                    "Codigo": 6.1,
                    "Paginas": 432,
                    "Año" : 1813,
                    "etiquetas" : ["Amor", "sociedad", "orgullo"]
                },
                "Cumbres borrascosas":{
                    "Author": "Emily Brontë",
                    "Codigo": 6.2,
                    "Paginas": 416,
                    "Año" : 1847,
                    "etiquetas" : ["Amor", "venganza", "naturaleza"]
                },
                "El amor en los tiempos del cólera":{
                    "Author":	"Gabriel García Márquez",
                    "Codigo": 6.3,
                    "Paginas": 368,
                    "Año" : 1985,
                    "etiquetas" : ["Amor",	"paciencia",	"vida"]
                },
                "Bajo el mismo techo":{
                    "Author":	"Sophie Kinsella",
                    "Codigo": 6.4,
                    "Paginas": 400,
                    "Año" : 2000,
                    "etiquetas" : ["Romántico",	"comedia",	"relaciones"]
                },
            }
        },
        "Novelas" : { 
            "Ubicación": "Estanteria 8H",
            "Codigo de libros" : 7.0,
            "Libros" : {
                "Cien años de soledad":{
                    "Author": "Gabriel García Márquez",
                    "Codigo": 7.1,
                    "Paginas": 432,
                    "Año" : 1967,
                    "etiquetas" : ["Realismo mágico", "familia", "soledad"]
                },
                "El túnel":{
                    "Author": "Ernesto Sabato",
                    "Codigo": 7.2,
                    "Paginas": 288,
                    "Año" : 1948,
                    "etiquetas" : ["Existencialismo", "obsesión", "amor"]
                },
                "Rayuela":{
                    "Author": "Julio Cortázar",
                    "Codigo": 7.3,
                    "Paginas": 560,
                    "Año" : 1963,
                    "etiquetas" : ["Literatura experimental", "amor", "búsqueda"]
                },
                "El Coronel no tiene quien le escriba":{
                    "Author": "Gabriel García Márquez",
                    "Codigo": 7.4,
                    "Paginas": 96,
                    "Año" : 1958,
                    "etiquetas" : ["Esperanza", "soledad", "crítica social"]
                },
                "Pedro Páramo":{
                    "Author": "Juan Rulfo",
                    "Codigo": 7.5,
                    "Paginas": 124,
                    "Año" : 1955,
                    "etiquetas" : ["Realismo mágico", "memoria", "muerte"]
                },
                "Los miserables":{
                    "Author": "Victor Hugo",
                    "Codigo": 7.6,
                    "Paginas": 1232,
                    "Año" : 1862,
                    "etiquetas" : ["Redención", "justicia", "sociedad"]
                },
                "La Maria":{
                    "Author": "Jorge Isaac",
                    "Codigo": 7.7,
                    "Paginas": 400,
                    "Año" : 1865,
                    "etiquetas" : ["Amor", "naturaleza", "sociedad"]
                },
                "El Quijote de la Mancha":{
                    "Author": "Miguel de Cervantes",
                    "Codigo": 7.8,
                    "Paginas": 1023,
                    "Año" : 1605,
                    "etiquetas" : ["Aventura", "locura", "caballería"]
                }
            }
        }
    },
    "Libros mas leidos" : ["El Principito", "Harry Potter", "Cien años de soledad", "Orgullo y prejuicio", "1984"],
    "Libros recomendados" : ["El Hobbit", "El viejo y el mar", "Drácula", "Cien años de soledad", "El amor en los tiempos del cólera"],
    "Libros disponibles" : ["El Principito", "Matilda", "Charlie y la fábrica de chocolate", "Donde viven los monstruos", "Cuentos por teléfono", "El Grúfalo", "La telaraña de Carlota", "Caperucita Roja", "El Hobbit", "El Señor de los Anillos (trilogía)", "Harry Potter (saga de 7 libros)", "Las crónicas de Narnia", "Eragon (saga El Legado)", "Coraline", "El nombre del viento", "La historia interminable", "La máquina del tiempo", "La guerra de los mundos", "1984", "Un mundo feliz", "Fahrenheit 451", "2001: Odisea del espacio", "Yo, Robot", "Drácula", "Frankenstein", "El resplandor", "Cementerio de animales", "El exorcista", "Por quien doblan las campanas", "El viejo y el mar", "Los tres mosqueteros", "El conde de Montecristo", "La isla del tesoro"],
    "Libros prestados" : {},
}



