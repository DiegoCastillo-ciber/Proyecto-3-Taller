#Proyecto 3
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import random


# Clase Personaje
class Personaje:

#Atributos:
    def __init__(self, tipo, sexo, nombre, alter, imagen,
                 velocidad, fuerza, inteligencia, defensa,
                 magia, telepatia, estrategia, volar,
                 elasticidad, regeneracion):

        self.tipo = tipo
        self.sexo = sexo
        self.nombre = nombre
        self.alter = alter
        self.imagen = imagen
        self.velocidad = velocidad
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.magia = magia
        self.telepatia = telepatia
        self.estrategia = estrategia
        self.volar = volar
        self.elasticidad = elasticidad
        self.regeneracion = regeneracion
#Metodos
    def __str__(self):
        return f"'{self.tipo}', '{self.sexo}', '{self.nombre}', '{self.alter}', '{self.imagen}', " + \
               f"{self.velocidad},{self.fuerza},{self.inteligencia},{self.defensa}," + \
               f"{self.magia},{self.telepatia},{self.estrategia},{self.volar}," + \
               f"{self.elasticidad},{self.regeneracion}"# metodo para guardar atributos mas adelante en luchadores.txt

#Clase Torneo
class Torneo:

#Atributos
    def __init__(self, nombre, lugar, cantidad_luchas):
        self.nombre = nombre
        self.lugar = lugar
        self.cantidad_luchas = cantidad_luchas
        self.victorias = {"bando1": 0, "bando2": 0}
#Metodos
    def guardar_resultado(self):
        fecha = self.obtener_fecha_desde_datos()
        if fecha:
            linea = f"{self.nombre},{fecha},{self.lugar},{self.cantidad_luchas},{self.victorias['bando1']},{self.victorias['bando2']}\n"
            with open("Programa/Torneos.txt", "a", encoding="utf-8") as archivo:
                archivo.write(linea)# con los valores de nombre del torneo fecha lugar y demas los agrupa y guarda como append en torneos.txt
        else:
            print("No se pudo encontrar la fecha en Datos.txt.")

    def obtener_fecha_desde_datos(self):
        try:
            with open("Programa/Datos.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    if linea.strip().startswith(self.nombre + ","):# inicia desde el nombre de los torneos
                        partes = linea.strip().split(",")#.split():Elimina los espacios en blanco al inicio y al final de la línea, incluyendo saltos de línea \n, tabulaciones, y espacios. 
                        if len(partes) >= 3:#si lo largo de cada valor mayor o igual que en teoria siempre tiene que ser se agarra partes uno q es la fecha
                            return partes[1].strip()#.strip elimina posibles espacios vacios y retorna la fecha del torneo
            print(f"No se encontró la fecha del torneo '{self.nombre}' en Datos.txt.")
        except Exception as e:
            print(f"Error leyendo Datos.txt: {e}")# si no se puede abrir muestra error
#Clase Lucha
class Lucha:

#Atributos
    def __init__(self, luchador1, luchador2, torneo):
        self.luchador1 = luchador1
        self.luchador2 = luchador2
        self.round1 = "Por definir"
        self.round2 = "Por definir"
        self.round3 = "Por definir"
        self.ganador = "Por definir"
        self.torneo = torneo
        self.pelear()

#Metodos
    def pelear(self):
        rondas = []
        for _ in range(3): #no necesito la variable entonces le pongo _
            ganador_ronda = random.choice([self.luchador1, self.luchador2])
            rondas.append(ganador_ronda)#Usa la función random.choice() para elegir aleatoriamente entre luchador1 y luchador2 simulando el ganador de una ronda.

        self.round1 = rondas[0]
        self.round2 = rondas[1]
        self.round3 = rondas[2]#como rondas es una lista manejo indices ya que cada personaje ganador de la ronda se guarda separado como indices

        if rondas.count(self.luchador1) > rondas.count(self.luchador2):
            self.ganador = self.luchador1# rondas.count(valor): cuenta en la lista cuantas veces aparece el luchador a ver cuantos rounds gano
        else:# retorna el ganador
            self.ganador = self.luchador2

    def guardar_resultado(self):
        try:
            with open("Programa/Luchas.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"{self.luchador1}, {self.luchador2}, R1, {self.round1}, {self.torneo}\n")
                archivo.write(f"{self.luchador1}, {self.luchador2}, R2, {self.round2}, {self.torneo}\n")
                archivo.write(f"{self.luchador1}, {self.luchador2}, R3, {self.round3}, {self.torneo}\n")# Se guardan los valores en luchas.txt con la escructura solicitada
        except:
            print("Error al guardar los resultados de la lucha.")


# E: torneo (Torneo), luchas (list de objetos Lucha)
# S: Muestra secuencialmente ventanas por cada lucha del torneo
# R: La lista de luchas no debe estar vacía
# O: Presentar el desarrollo del torneo con rondas y actualizar las victorias
def mostrar_lucha_secuencial(torneo, luchas):
    index = [0]  # Controla qué lucha se está mostrando

    def mostrar_lucha():
        if index[0] >= len(luchas):  # Si ya no hay más luchas
            mostrar_resultado_final(torneo)
            return

        lucha = luchas[index[0]]  # Lucha actual
        ventana = tk.Toplevel()
        ventana.title(f"Lucha {index[0] + 1}")
        ventana.geometry("600x400")
        ventana.configure(bg="black")

        # Muestra el nombre del torneo y número de lucha
        tk.Label(ventana, text=f"Torneo: {torneo.nombre}", fg="yellow", bg="black", font=("Arial", 18, "bold")).pack(pady=5)
        tk.Label(ventana, text=f"Lucha {index[0] + 1}", fg="white", bg="black", font=("Arial", 14)).pack(pady=5)

        contenedor = tk.Frame(ventana, bg="black")
        contenedor.pack()

        # Información del Bando 1
        izquierda = tk.Frame(contenedor, bg="black")
        izquierda.grid(row=0, column=0, padx=40)
        tk.Label(izquierda, text="Bando 1", fg="skyblue", bg="black", font=("Arial", 12)).pack()
        tk.Label(izquierda, text=lucha.luchador1, fg="cyan", bg="black", font=("Arial", 14)).pack()

        # Etiqueta "VS"
        tk.Label(contenedor, text="VS", fg="white", bg="black", font=("Arial", 14)).grid(row=0, column=1, padx=20)

        # Información del Bando 2
        derecha = tk.Frame(contenedor, bg="black")
        derecha.grid(row=0, column=2, padx=40)
        tk.Label(derecha, text="Bando 2", fg="orange", bg="black", font=("Arial", 12)).pack()
        tk.Label(derecha, text=lucha.luchador2, fg="orange", bg="black", font=("Arial", 14)).pack()

        # Muestra los resultados de cada ronda
        colores = {lucha.luchador1: "cyan", lucha.luchador2: "orange"}
        resultados = [("R1", lucha.round1), ("R2", lucha.round2), ("R3", lucha.round3)]

        for ronda, ganador in resultados:
            color = colores.get(ganador, "white")
            tk.Label(ventana, text=f"Ganador {ronda}: {ganador}", fg=color, bg="black", font=("Arial", 12)).pack()

        # Suma la victoria al bando correspondiente
        if lucha.ganador == lucha.luchador1:
            torneo.victorias["bando1"] += 1
        else:
            torneo.victorias["bando2"] += 1

        # Guarda los resultados de la lucha
        lucha.guardar_resultado()

        # Botón para pasar a la siguiente lucha
        def siguiente():
            ventana.destroy()
            index[0] += 1
            mostrar_lucha()

        tk.Button(ventana, text="Siguiente Lucha", command=siguiente, font=("Arial", 12), bg="gray").pack(pady=15)

    mostrar_lucha()

# E: nombre_torneo: nombre del torneo que se busca en Datos.txt
# S:  llama a la función que muestra las luchas si el torneo se encuentra
# R: El archivo "Datos.txt" debe existir y tener el formato correcto
# O: Leer la información del torneo desde el archivo y comenzar a mostrar las luchas
def iniciar_torneo_desde_archivo(nombre_torneo):
    try:
        with open("Programa/Datos.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()  # Lee todas las líneas del archivo
    except:
        tk.messagebox.showerror("Error", "No se pudo abrir el archivo Datos.txt")
        return

    i = 0
    while i < len(lineas):  # Busca línea por línea el nombre del torneo
        if lineas[i].split(",")[0].strip() == nombre_torneo:
            encabezado = lineas[i].strip().split(",")
            lugar = encabezado[2].strip()
            cantidad_luchas = int(encabezado[3])

            bando1 = lineas[i + 2].strip().split(", ")  # Línea con personajes del bando 1
            bando2 = lineas[i + 4].strip().split(", ")  # Línea con personajes del bando 2

            torneo = Torneo(nombre_torneo, lugar, cantidad_luchas)  # Se crea el objeto Torneo
            luchas = []

            # Crea las luchas según el número de luchas y personajes disponibles
            for j in range(min(len(bando1), len(bando2), cantidad_luchas)):
                luchador1 = bando1[j].strip()
                luchador2 = bando2[j].strip()
                if luchador1 and luchador2:
                    luchas.append(Lucha(luchador1, luchador2, nombre_torneo))  # Crea la Lucha

            mostrar_lucha_secuencial(torneo, luchas)  # Inicia la visualización
            return
        i += 1

    tk.messagebox.showwarning("No encontrado", f"No se encontró el torneo '{nombre_torneo}'")


# E: torneo  – objeto que contiene nombre y victorias por bando
# S: Muestra ventana con el resultado final del torneo y lo guarda en archivo
# R: El torneo debe tener su nombre y estadísticas ya calculadas
# O: Mostrar el bando ganador y guardar los datos del torneo en archivo
def mostrar_resultado_final(torneo):
    ventana = tk.Toplevel()
    ventana.title("Resultado Final")
    ventana.geometry("500x300")
    ventana.configure(bg="black")

    # Título del torneo
    tk.Label(ventana, text=f"🏆 Torneo: {torneo.nombre} 🏆", fg="yellow", bg="black", font=("Arial", 16, "bold")).pack(pady=20)

    # Determina quién ganó
    if torneo.victorias["bando1"] > torneo.victorias["bando2"]:# llama a la clase torneo selecciona el atributo victorias q es un diccionario donde se guarda el valor con bando1 y sus vicotria y bando 2 con sus victorias
        resultado = "Bando 1"
    elif torneo.victorias["bando2"] > torneo.victorias["bando1"]:
        resultado = "Bando 2"
    else:
        resultado = "Empate"

    # Muestra el resultado
    tk.Label(ventana, text=f"Ganador del Torneo: {resultado}", fg="cyan", bg="black", font=("Arial", 14)).pack(pady=10)

    # Guarda los datos en el archivo Torneos.txt
    torneo.guardar_resultado()

    # Botón para cerrar
    tk.Button(ventana, text="Finalizar Torneo", command=lambda:menu_inicio(""), font=("Arial", 12), bg="red", fg="white").pack(pady=20)


# Ventana de inicio
ventana = tk.Tk()
ventana.title("Bienvenidos a El Gran Torneo")
ventana.configure(bg="#000000")
#Utilizamos 3 tipos de marco para separar botones la ventana principal y la imagen con el fin de un manejo mas estructurado de la ventana
# Ventana centrada
marco_principal = tk.Frame(ventana, bg="#000000")
marco_principal.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_columnconfigure(0, weight=1)
# Centrar ventana en la pantalla
ancho_ventana = 400
alto_ventana = 700
pantalla_ancho = ventana.winfo_screenwidth()
pantalla_alto = ventana.winfo_screenheight()
x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
y = int((pantalla_alto / 2) - (alto_ventana / 2))
ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
# Cargar imagen
imagen = Image.open("Programa/imagenes/logo1.png")
imagen = imagen.resize((300, 300), Image.Resampling.LANCZOS)# Sirve para 
imagen_tk = ImageTk.PhotoImage(imagen)
#marco logo
marco_izquierda = tk.Frame(marco_principal, bg="#000000")
marco_izquierda.grid(row=0, column=0, pady=(10, 0))  # Imagen arriba
logo = tk.Label(marco_izquierda, image=imagen_tk, bg="#000000")
logo.grid(row=0, column=0)

# Marco para las etiquetas y botones
marco_derecha = tk.Frame(marco_principal, bg="#000000")
marco_derecha.grid(row=1, column=0, pady=40)
#Usuario ingresa los datos personales
titulo= tk.Label(marco_derecha, text="Ingrese sus datos", font=("Arial", 24), bg="#000000", fg="white")
titulo.grid(row=0, columnspan=2, pady=10)
#Usuario
usuario = tk.Label(marco_derecha, text="Usuario:", font=("Arial", 14), bg="#000000", fg="white")
usuario.grid(row=1, column=0, pady=10, sticky="e")
entrada_usuario = tk.Entry(marco_derecha, font=("Arial", 14), width=20)
entrada_usuario.grid(row=1, column=1, pady=10)
#Contraseña
contrasena = tk.Label(marco_derecha, text="Contraseña:", font=("Arial", 14), bg="#000000", fg="white")
contrasena.grid(row=2, column=0, pady=10, sticky="e")
entrada_contrasena = tk.Entry(marco_derecha, show="", font=("Arial", 14), width=20)
entrada_contrasena.grid(row=2, column=1, pady=10)
#Boton para pasar del menu
boton_login = tk.Button(marco_derecha, text="Iniciar Juego", font=("Arial", 14), command=lambda: validadorcredenciales())
boton_login.grid(row=3, column=0, columnspan=2, pady=20)#Column es de arriba a abajo y row de derecha a izquierda como celdas

#E:usuario y contraseña ingresados por el usuario
#S:Entra a menu_inicio si las credenciales son correctas, o muestra un mensaje de error si no lo son.
#R:debe coincidir con los datos que ya estan en el archivo usuarios.txt
#Descripcion: esta funcion valida que los datos ingresados por el usuario coincidan con los que ya estan en usuarios.txt
def validadorcredenciales():
    archivo = open("Programa/usuarios.txt", "r", encoding="utf-8")
    UsuContra = archivo.readlines()
    i = 0
    usuario_input = entrada_usuario.get()
    contrasena_input = entrada_contrasena.get()

    while i < len(UsuContra):
        x = UsuContra[i]
        veri = x.split(";")
        Persona = veri[0].strip()
        usu = veri[1].strip()#separa el nombre; usuario; contraseña y los va agarrando para validar si se puede entrar
        con = veri[2].strip()

        if usuario_input == usu and contrasena_input == con:
            messagebox.showinfo("Bienvenido", f"Hola {Persona}, acceso concedido.")
            return menu_inicio(Persona)  # Sale de la función si las credenciales son correctas

        i += 1

    # Si terminó el ciclo y no encontró nada válido
    messagebox.showerror("Error", "Usuario o contraseña incorrectos")
#E:-
#S: manda a los diferentes submenus como crear torneo, estadisticas y demas
#R:seleccionar un boton
#O:Mostrar un menu al usuario de manera que precione el boton de la accion que desea Hacer
def menu_inicio(Persona):
    ventana.withdraw()  # Oculta la ventana principal sin cerrarla solo en este ya que las demas tienen funciones propias
    P=Persona
    # Crea una nueva ventana para el menú de inicio
    menu_ventana = tk.Toplevel()
    menu_ventana.title("Menú de Inicio")
    menu_ventana.configure(bg="#000000")
    # Centrar ventana en la pantalla
    ancho_ventana = 650
    alto_ventana = 450
    pantalla_ancho = menu_ventana.winfo_screenwidth()
    pantalla_alto = menu_ventana.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
    y = int((pantalla_alto / 2) - (alto_ventana / 2))
    menu_ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    # Aquí puedes agregar más elementos al menú de inicio
    bienvenida = tk.Label(menu_ventana, text=f"¡Bienvenido al Menú de Inicio,{P}!", font=("Arial", 24), bg="#000000", fg="white")
    bienvenida.grid(row=0, column=0, pady=10, sticky="ew")
    etiqueta = tk.Label(menu_ventana, text=f"¿Que deseas hacer?", font=("Arial", 24), bg="#000000", fg="red")
    etiqueta.grid(row=1, column=0, pady=10, sticky="ew")

    #Botones
    boton_Personajes = tk.Button(menu_ventana, text="Crear/Borrar Personajes", font=("Arial", 14), bg="#000000", fg="white", command=lambda: menupersonajes(menu_ventana))
    boton_Personajes.grid(row=2, column=0, pady=10, sticky="ew")

    boton_torneos = tk.Button(menu_ventana, text="Crear/Borrar Torneos", font=("Arial", 14), bg="#000000", fg="white", command=lambda: submenutorneos(menu_ventana))
    boton_torneos.grid(row=3, column=0, pady=10, sticky="ew")

    boton_Jugar = tk.Button(menu_ventana, text="Jugar", font=("Arial", 14), bg="#000000", fg="white", command=lambda: jugar(menu_ventana))
    boton_Jugar.grid(row=4, column=0, pady=10, sticky="ew")

    boton_estadisticas = tk.Button(menu_ventana, text="Estadisticas", font=("Arial", 14), bg="#000000", fg="white", command=lambda: estadisticas(menu_ventana))
    boton_estadisticas.grid(row=5, column=0, pady=10, sticky="ew")

    salir_boton = tk.Button(menu_ventana, text="Salir del Juego", font=("Arial", 14), bg="#000000", fg="white", command=menu_ventana.destroy)
    salir_boton.grid(row=6, column=0, pady=5, sticky="ew")

    

#E:-
#S:crear o borrar torneo
#R:seleccionar en los botones las opciones 
#O:menu de subtorneos donde el usuario selecciona que opcion desea realizar mediante un boton
def submenutorneos(menuant):
    menuant.destroy()
    ventana_st = tk.Toplevel()
    ventana_st.title("Submenú de Torneos")
    ventana_st.configure(bg="#000000")
    # Centrar ventana en la pantalla
    ancho_ventana = 550
    alto_ventana = 300
    pantalla_ancho = ventana_st.winfo_screenwidth()
    pantalla_alto = ventana_st.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
    y = int((pantalla_alto / 2) - (alto_ventana / 2))
    ventana_st.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    # Widgets
    bienvenida = tk.Label(ventana_st, text="¡Bienvenido al Submenú de Torneos!", font=("Arial", 24), bg="#000000", fg="white")
    bienvenida.grid(row=0, column=0, pady=10, sticky="ew")
    etiqueta = tk.Label(ventana_st, text="¿Qué deseas hacer?", font=("Arial", 24), bg="#000000", fg="red")
    etiqueta.grid(row=1, column=0, pady=10, sticky="ew")
    # Botones
    boton_crear_torneo = tk.Button(ventana_st, text="Crear Torneo", font=("Arial", 14), bg="#000000", fg="white", command=lambda: crear_torneo(ventana_st))
    boton_crear_torneo.grid(row=2, column=0, pady=10, sticky="ew")
    boton_borrar_torneo = tk.Button(ventana_st, text="Borrar Torneo", font=("Arial", 14), bg="#000000", fg="white", command=lambda:ventana_borrar_torneo(ventana_st))
    boton_borrar_torneo.grid(row=3, column=0, pady=10, sticky="ew")
    boton_volver = tk.Button(ventana_st, text="Volver al Menú Principal", font=("Arial", 14), bg="#000000", fg="white", command=lambda:[menu_inicio(""),ventana_st.destroy()])
    boton_volver.grid(row=4, column=0, pady=10, sticky="ew")

#E:-
#S:Todos los atributos del objeto: heroe creado
#R:Los atributos deben sumar 100 y que todos los campos de informacion esten
#O:Formulario para que el usuario cree su personaje y se guarde  
def heroe(menu):
    menu.destroy()
    ventana_cp = tk.Toplevel()
    ventana_cp.title("Crear Personaje")
    ventana_cp.configure(bg="#0800FF")

    ventana_cp.geometry("400x700")

    marco = tk.Frame(ventana_cp, bg="#0800FF")
    marco.grid(row=0, column=1, padx=20, pady=20)
    #E:-
    #S:muestra el panel de documentos del usuario
    #R:-
    #O:Busca el archivo de la imagen y la muestra en pantalla para seleccionar
    def seleccionar_imagen():
        archivo = filedialog.askopenfilename(#Abre una ventana emergente de diálogo usando filedialog.askopenfilename().
                                            #Esa ventana permite al usuario buscar y seleccionar un archivo en su computadora.
                                            #El parámetro title="Seleccionar imagen" pone un título en la ventana emergente.
            title="Seleccionar imagen",
            filetypes=[("Archivos de imagen", "*.jpg *.png *.jpeg *.gif")])#Filtra los archivos visibles para que solo se vean imágenes con esas extensiones.
        if archivo:
            ruta_imagen.set(archivo)
            ruta_label.config(text=archivo.split("/")[-1])  # muestra solo el nombre de archivo

    tk.Label(marco, text="Crea tu Heroe:", fg="yellow", bg="#0800FF",font=("Arial", 16,"bold")).grid(row=0, column=1, sticky="e")

    # Datos básicos
    tk.Label(marco, text="Tipo (H/V):", fg="white", bg="#0800FF").grid(row=1, column=0, sticky="e")
    entrada_tipo = tk.Entry(marco)
    entrada_tipo.grid(row=1, column=1)

    tk.Label(marco, text="Sexo (H/M/N):", fg="white", bg="#0800FF").grid(row=2, column=0, sticky="e")
    entrada_sexo = tk.Entry(marco)
    entrada_sexo.grid(row=2, column=1)

    tk.Label(marco, text="Nombre completo:", fg="white", bg="#0800FF").grid(row=3, column=0, sticky="e")
    entrada_nombre = tk.Entry(marco)
    entrada_nombre.grid(row=3, column=1)

    tk.Label(marco, text="Alter ego:", fg="white", bg="#0800FF").grid(row=4, column=0, sticky="e")
    entrada_alter = tk.Entry(marco)
    entrada_alter.grid(row=4, column=1)

    tk.Label(marco, text="Seleccionar imagen:", fg="white", bg="#0800FF").grid(row=5, column=0, sticky="e")
    boton_imagen = tk.Button(marco, text="Buscar imagen", command=seleccionar_imagen)
    boton_imagen.grid(row=5, column=1,pady=10)
    ruta_label = tk.Label(marco, text="", fg="yellow", bg="#0800FF")
    ruta_label.grid(row=6, column=0, columnspan=2)

    # Atributos sin lista
    tk.Label(marco, text="Velocidad:", fg="white", bg="#0800FF").grid(row=7, column=0, sticky="e")
    entrada1 = tk.Entry(marco)
    entrada1.grid(row=7, column=1)

    tk.Label(marco, text="Fuerza:", fg="white", bg="#0800FF").grid(row=8, column=0, sticky="e")
    entrada2 = tk.Entry(marco)
    entrada2.grid(row=8, column=1)

    tk.Label(marco, text="Inteligencia:", fg="white", bg="#0800FF").grid(row=9, column=0, sticky="e")
    entrada3 = tk.Entry(marco)
    entrada3.grid(row=9, column=1)

    tk.Label(marco, text="Defensa:", fg="white", bg="#0800FF").grid(row=10, column=0, sticky="e")
    entrada4 = tk.Entry(marco)
    entrada4.grid(row=10, column=1)

    tk.Label(marco, text="Magia:", fg="white", bg="#0800FF").grid(row=11, column=0, sticky="e")
    entrada5 = tk.Entry(marco)
    entrada5.grid(row=11, column=1)

    tk.Label(marco, text="Telepatía:", fg="white", bg="#0800FF").grid(row=12, column=0, sticky="e")
    entrada6 = tk.Entry(marco)
    entrada6.grid(row=12, column=1)

    tk.Label(marco, text="Estrategia:", fg="white", bg="#0800FF").grid(row=13, column=0, sticky="e")
    entrada7 = tk.Entry(marco)
    entrada7.grid(row=13, column=1)

    tk.Label(marco, text="Volar:", fg="white", bg="#0800FF").grid(row=14, column=0, sticky="e")
    entrada8 = tk.Entry(marco)
    entrada8.grid(row=14, column=1)

    tk.Label(marco, text="Elasticidad:", fg="white", bg="#0800FF").grid(row=15, column=0, sticky="e")
    entrada9 = tk.Entry(marco)
    entrada9.grid(row=15, column=1)

    tk.Label(marco, text="Regeneración:", fg="white", bg="#0800FF").grid(row=16, column=0, sticky="e")
    entrada10 = tk.Entry(marco)
    entrada10.grid(row=16, column=1)

    
    ruta_imagen = tk.StringVar(value="")  # variable para guardar ruta
    #E:atributos del personaje
    #S:guarda en luchadores.txt
    #R:Tiene que llenar todos los campos
    #O:Guardar los datos en luchadores.txt
    def guardar():
        try:
            a1 = int(entrada1.get())
            a2 = int(entrada2.get())
            a3 = int(entrada3.get())
            a4 = int(entrada4.get())
            a5 = int(entrada5.get())
            a6 = int(entrada6.get())
            a7 = int(entrada7.get())
            a8 = int(entrada8.get())
            a9 = int(entrada9.get())
            a10 = int(entrada10.get())#para conseguir los valores de los entry de la pantalla
        except:
            messagebox.showerror("Error", "Todos los atributos deben ser números")
            return

        if a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 != 100:
            messagebox.showerror("Error", "La suma de atributos debe ser 100")
            return
        imagen = ruta_imagen.get()#agarra el valor que da el stringvar
        if imagen == "":
            messagebox.showerror("Error", "Debe seleccionar una imagen")
            return
        tipo = entrada_tipo.get().upper()#muestra H si es hombre y V o H si es villano o heroe upper se usa para la mayuscula
        sexo = entrada_sexo.get().upper()
        nombre = entrada_nombre.get()
        alter = entrada_alter.get()

        if (tipo != 'H' and tipo != 'V') or (sexo != 'H' and sexo != 'M' and sexo != 'N') or nombre == "" or alter == "":# si faltan valores muestra eror
            messagebox.showerror("Error", "Complete todos los campos correctamente")
            return

        p = Personaje(tipo, sexo, nombre, alter, imagen, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)#da los atributos a la clase personajes

        with open("Programa/Luchadores.txt", "a", encoding="utf-8") as archivo:
            archivo.write(str(p) + "\n")#llama a la clase del torneo y usa los parametros que da __str__() y los guarda

        messagebox.showinfo("Listo", "Personaje guardado")
        ventana_cp.destroy()

    boton_guardar = tk.Button(marco, text="Guardar Personaje", command=lambda:[guardar,menu_inicio("")])
    boton_guardar.grid(row=17, column=0, columnspan=2, pady=20)

#E:-
#S:Todos los atributos del objeto: heroe creado
#R:Los atributos deben sumar 100 y que todos los campos de informacion esten
#O:Formulario para que el usuario cree su personaje y se guarde  
def Villano(menu):
    menu.destroy()
    ventana_cp = tk.Toplevel()
    ventana_cp.title("Crear Personaje")
    ventana_cp.configure(bg="#FF0000")

    ventana_cp.geometry("400x700")

    marco = tk.Frame(ventana_cp, bg="#FF0000")
    marco.grid(row=0, column=1, padx=20, pady=20)
    
    #E:-
    #S:muestra el panel de documentos del usuario
    #R:-
    #O:Busca el archivo de la imagen y la muestra en pantalla para seleccionar
    def seleccionar_imagen():
        archivo = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Archivos de imagen", "*.jpg *.png *.jpeg *.gif")])
        if archivo:
            ruta_imagen.set(archivo)
            ruta_label.config(text=archivo.split("/")[-1])  # muestra solo el nombre de archivo

    tk.Label(marco, text="Crea tu Villano:", fg="yellow", bg="#FF0000",font=("Arial", 16,"bold")).grid(row=0, column=1, sticky="e")

    # Datos básicos
    tk.Label(marco, text="Tipo (H/V):", fg="white", bg="#FF0000").grid(row=1, column=0, sticky="e")
    entrada_tipo = tk.Entry(marco)
    entrada_tipo.grid(row=1, column=1)

    tk.Label(marco, text="Sexo (H/M/N):", fg="white", bg="#FF0000").grid(row=2, column=0, sticky="e")
    entrada_sexo = tk.Entry(marco)
    entrada_sexo.grid(row=2, column=1)

    tk.Label(marco, text="Nombre completo:", fg="white", bg="#FF0000").grid(row=3, column=0, sticky="e")
    entrada_nombre = tk.Entry(marco)
    entrada_nombre.grid(row=3, column=1)

    tk.Label(marco, text="Alter ego:", fg="white", bg="#FF0000").grid(row=4, column=0, sticky="e")
    entrada_alter = tk.Entry(marco)
    entrada_alter.grid(row=4, column=1)

    tk.Label(marco, text="Seleccionar imagen:", fg="white", bg="#FF0000").grid(row=5, column=0, sticky="e")
    boton_imagen = tk.Button(marco, text="Buscar imagen", command=seleccionar_imagen)
    boton_imagen.grid(row=5, column=1,pady=10)
    ruta_label = tk.Label(marco, text="", fg="yellow", bg="#FF0000")
    ruta_label.grid(row=6, column=0, columnspan=2)

    # Atributos sin lista
    tk.Label(marco, text="Velocidad:", fg="white", bg="#FF0000").grid(row=7, column=0, sticky="e")
    entrada1 = tk.Entry(marco)
    entrada1.grid(row=7, column=1)

    tk.Label(marco, text="Fuerza:", fg="white", bg="#FF0000").grid(row=8, column=0, sticky="e")
    entrada2 = tk.Entry(marco)
    entrada2.grid(row=8, column=1)

    tk.Label(marco, text="Inteligencia:", fg="white", bg="#FF0000").grid(row=9, column=0, sticky="e")
    entrada3 = tk.Entry(marco)
    entrada3.grid(row=9, column=1)

    tk.Label(marco, text="Defensa:", fg="white", bg="#FF0000").grid(row=10, column=0, sticky="e")
    entrada4 = tk.Entry(marco)
    entrada4.grid(row=10, column=1)

    tk.Label(marco, text="Magia:", fg="white", bg="#FF0000").grid(row=11, column=0, sticky="e")
    entrada5 = tk.Entry(marco)
    entrada5.grid(row=11, column=1)

    tk.Label(marco, text="Telepatía:", fg="white", bg="#FF0000").grid(row=12, column=0, sticky="e")
    entrada6 = tk.Entry(marco)
    entrada6.grid(row=12, column=1)

    tk.Label(marco, text="Estrategia:", fg="white", bg="#FF0000").grid(row=13, column=0, sticky="e")
    entrada7 = tk.Entry(marco)
    entrada7.grid(row=13, column=1)

    tk.Label(marco, text="Volar:", fg="white", bg="#FF0000").grid(row=14, column=0, sticky="e")
    entrada8 = tk.Entry(marco)
    entrada8.grid(row=14, column=1)

    tk.Label(marco, text="Elasticidad:", fg="white", bg="#FF0000").grid(row=15, column=0, sticky="e")
    entrada9 = tk.Entry(marco)
    entrada9.grid(row=15, column=1)

    tk.Label(marco, text="Regeneración:", fg="white", bg="#FF0000").grid(row=16, column=0, sticky="e")
    entrada10 = tk.Entry(marco)
    entrada10.grid(row=16, column=1)

    
    ruta_imagen = tk.StringVar(value="")  # variable para guardar ruta
    #E:atributos del personaje
    #S:guarda en luchadores.txt
    #R:Tiene que llenar todos los campos
    #O:Guardar los datos en luchadores.txt
    def guardar():
        try:
            a1 = int(entrada1.get())
            a2 = int(entrada2.get())
            a3 = int(entrada3.get())
            a4 = int(entrada4.get())
            a5 = int(entrada5.get())
            a6 = int(entrada6.get())
            a7 = int(entrada7.get())
            a8 = int(entrada8.get())
            a9 = int(entrada9.get())
            a10 = int(entrada10.get())
        except:
            messagebox.showerror("Error", "Todos los atributos deben ser números")
            return

        if a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 != 100:
            messagebox.showerror("Error", "La suma de atributos debe ser 100")
            return
        imagen = ruta_imagen.get()
        if imagen == "":
            messagebox.showerror("Error", "Debe seleccionar una imagen")
            return
        tipo = entrada_tipo.get().upper()
        sexo = entrada_sexo.get().upper()
        nombre = entrada_nombre.get()
        alter = entrada_alter.get()

        if (tipo != 'H' and tipo != 'V') or (sexo != 'H' and sexo != 'M' and sexo != 'N') or nombre == "" or alter == "":
            messagebox.showerror("Error", "Complete todos los campos correctamente")
            return

        p = Personaje(tipo, sexo, nombre, alter, imagen, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)

        with open("Programa/Luchadores.txt", "a", encoding="utf-8") as archivo:
            archivo.write(str(p) + "\n")

        messagebox.showinfo("Listo", "Personaje guardado")
        ventana_cp.destroy()

    boton_guardar = tk.Button(marco, text="Guardar Personaje", command=lambda:guardar)
    boton_guardar.grid(row=17, column=0, columnspan=2, pady=20)
  
#E:-
#S:Personaje borrado
#R:Debe existir el personaje
#O:Menu para que el usuario borre el personaje que desee.
def borrar_personaje(menu):
    menu.destroy()
    ventana_bp = tk.Toplevel()
    ventana_bp.title("Eliminar Personaje")
    ventana_bp.geometry("600x700")
    ventana_bp.configure(bg="#1e1e1e")

    titulo = tk.Label(ventana_bp, text="Eliminar Personaje", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="white")
    titulo.pack(pady=10)

    archivo = open("Programa/Luchadores.txt", "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    if len(lineas) == 0:
        sin_pj = tk.Label(ventana_bp, text="No hay personajes disponibles.", bg="#1e1e1e", fg="white")
        sin_pj.pack(pady=20)
        return

    # Scroll funcional con barra
    contenedor = tk.Frame(ventana_bp, bg="#000000")
    contenedor.pack(fill="both", expand=True)# contenedor se colocara el canvas y el scrollbar

    canvas = tk.Canvas(contenedor, bg="#000000", highlightthickness=0)#highlightthickness=0 elimina el borde por defecto.
    scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)#configura para que en el canvas se enlace con el srcoll y se actualize el canvas cuand lo mueves

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    frame_scroll = tk.Frame(canvas, bg="#000000")
    canvas.create_window((0, 0), window=frame_scroll, anchor="nw")#crea un mini contenerdor donde se van a poner las variables del lo que se puede mover botones y etiquetas

    # Ajustar área visible al tamaño de contenido
    def actualizar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_scroll.bind("<Configure>", actualizar_scroll)#Cada vez que el frame_scroll cambie de tamaño, se llama a actualizar_scroll,Así el canvas ajusta su zona de scroll automáticamente.

    # Redirigir widgets al frame_scroll sin modificar lógica existente
    ventana_bp = frame_scroll#Este truco redirige la variable ventana_bp (la ventana original) para que, de ahora en adelante, los nuevos widgets (etiquetas, botones) se agreguen dentro del contenedor

    for linea in lineas:#para cada luchador realiza:
        datos = linea.strip().split(",")#elimina algun espacio mal puesto y separa en las comas

        if len(datos) >= 15:
            tipo = datos[0].strip(" '")
            sexo = datos[1].strip(" '")
            nombre = datos[2].strip(" '")
            alter = datos[3].strip(" '")
            ruta = datos[4].strip(" '")# se separa cada atributo

            marco = tk.Frame(ventana_bp, bg="#2b2b2b", bd=2, relief="ridge")
            marco.pack(padx=10, pady=10, fill="x")#se crea un mini cuadro con la informacion del personaje 

            try:
                imagen = Image.open(ruta)
                imagen = imagen.resize((100, 100), Image.Resampling.LANCZOS)#ayuda a q la imagen sea de buena calidad(lanczos) y que se ajuste a un nuevo tamaño
                imagen_tk = ImageTk.PhotoImage(imagen)
                etiqueta_img = tk.Label(marco, image=imagen_tk, bg="#2b2b2b")
                etiqueta_img.image = imagen_tk
                etiqueta_img.grid(row=0, column=0, rowspan=4, padx=10)
                #busca la imagen del personaje
            except:
                etiqueta_img = tk.Label(marco, text="Imagen no disponible", bg="#2b2b2b", fg="red")
                etiqueta_img.grid(row=0, column=0, rowspan=4, padx=10)

            texto = tk.Label(marco, text=f"{alter} ({nombre}) - Tipo: {tipo} - Sexo: {sexo}", bg="#2b2b2b", fg="white")
            texto.grid(row=0, column=1, sticky="w")

            atributos = "Vel: " + datos[5] + "  Fue: " + datos[6] + "  Int: " + datos[7] + "  Def: " + datos[8] + "\n" + \
                        "Mag: " + datos[9] + "  Tel: " + datos[10] + "  Est: " + datos[11] + "  Vol: " + datos[12] + "\n" + \
                        "Eli: " + datos[13] + "  Reg: " + datos[14]

            info = tk.Label(marco, text=atributos, bg="#2b2b2b", fg="yellow", justify="left")
            info.grid(row=1, column=1, sticky="w")
            #E:
            #S:
            #R:
            #O:
            def eliminar_personaje(al=alter):
                respuesta = messagebox.askyesno("Confirmar", "¿Deseas eliminar a " + al + "?")# muestra una ventana emergente al usuario con dos botones: "Yes" y "No" (o "Sí" y "No", si está en español).
                if respuesta:
                    archivo = open("Programa/Luchadores.txt", "w", encoding="utf-8")#se reescribe todos los personajes sin el q se borro
                    for l in lineas:
                        if al in l:
                            continue  # omite escribir la línea ya que el personaje se borra
                        archivo.write(l)
                    archivo.close()
                    messagebox.showinfo("Listo", "Personaje eliminado")
                    ventana_bp.destroy()
                    borrar_personaje()

            boton = tk.Button(marco, text="Eliminar", bg="red", fg="white", command=lambda al=alter: eliminar_personaje(al))
            boton.grid(row=2, column=1, sticky="w")#cambiar
#E:-
#S:opcion del boton precionado por el usuario
#R:solo los botones mostrados se pueden precionar
#O:Muestra un menu de que desea hacer si desea crear o borrar personaje
def menupersonajes(ventana_anterior):
    ventana_anterior.destroy()  # Esto sí cierra la ventana anterior
    
    menu_personajes = tk.Toplevel()  # Nueva ventana
    menu_personajes.title("Menú de Personajes")
    menu_personajes.configure(bg="#000000")

    # Centrar la ventana
    ancho_ventana = 525
    alto_ventana = 350
    pantalla_ancho = menu_personajes.winfo_screenwidth()
    pantalla_alto = menu_personajes.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
    y = int((pantalla_alto / 2) - (alto_ventana / 2))
    menu_personajes.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    # Widgets
    bienvenida = tk.Label(menu_personajes, text="¡Bienvenido al Menú de Personajes!", font=("Arial", 24), bg="#000000", fg="white")
    bienvenida.grid(row=0, column=0, pady=10, sticky="ew")

    etiqueta = tk.Label(menu_personajes, text="¿Qué deseas hacer?", font=("Arial", 24), bg="#000000", fg="red")
    etiqueta.grid(row=1, column=0, pady=10, sticky="ew")

    boton_crear = tk.Button(menu_personajes, text="Crear Personaje", font=("Arial", 14), bg="#000000", fg="white", command=lambda: [crear_personaje(menu_personajes), menu_personajes.destroy()])
    boton_crear.grid(row=2, column=0, pady=10, sticky="ew")

    boton_borrar = tk.Button(menu_personajes, text="Borrar Personaje", font=("Arial", 14), bg="#000000", fg="white", command=lambda:borrar_personaje(menu_personajes))
    boton_borrar.grid(row=3, column=0, pady=10, sticky="ew")

    salir_boton = tk.Button(menu_personajes, text="Volver al menu principal", font=("Arial", 14), bg="#000000", fg="white", command=lambda: [menu_inicio(""), menu_personajes.destroy()])
    salir_boton.grid(row=4, column=0, pady=5, sticky="ew")

    menu_personajes.mainloop()

#E:.-
#S:crea un objeto personaje
#R:botones unica seleccion
#O:menu para crear personaje que se le muestra al usuario
def crear_personaje(menu):
    menu.destroy()
    personaje=tk.Toplevel()
    personaje.title("Crear Personaje") 
    personaje.configure(bg="#000000")
    # Centrar ventana en la pantalla
    ancho_ventana = 220
    alto_ventana = 220
    pantalla_ancho = personaje.winfo_screenwidth()
    pantalla_alto = personaje.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
    y = int((pantalla_alto / 2) - (alto_ventana / 2))
    personaje.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
    # Etiquetas y campos de entrada
    mensaje = tk.Label(personaje, text="¿Deseas crear un:?", font=("Arial", 14), bg="#000000", fg="white")
    mensaje.grid(row=0, column=0, pady=10, sticky="ew")

    boton_Heroe = tk.Button(personaje, text="Heroe", font=("Arial", 14), bg="#4C00FF", fg="yellow", command=lambda: heroe(personaje))
    boton_Heroe.grid(row=1, column=0, pady=10, sticky="ew")

    boton_Villano = tk.Button(personaje, text="Villano", font=("Arial", 14), bg="#FF0000", fg="black", command=lambda: Villano(personaje))
    boton_Villano.grid(row=2, column=0, pady=10, sticky="ew")

    salir_boton = tk.Button(personaje, text="Volver al menu principal", font=("Arial", 14), bg="#FFFFFF", fg="black", command=lambda:[menupersonajes(personaje), personaje.destroy()])
    salir_boton.grid(row=4, column=0, pady=5, sticky="ew")

    personaje.mainloop()
#E:-
#S:Torneo creado guardado en datos.txt
#R:modos ya brindados
#O:Muestra un menu al usuario para que pueda crear un torneo
def crear_torneo(menu):
    menu.destroy()
    crea_torneo = tk.Toplevel()
    crea_torneo.title("Crear Torneo")
    crea_torneo.configure(bg="#000000")
    #centrar ventana
    ancho_ventana = 450
    alto_ventana = 520
    pantalla_ancho = crea_torneo.winfo_screenwidth()
    pantalla_alto = crea_torneo.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
    y = int((pantalla_alto / 2) - (alto_ventana / 2))
    crea_torneo.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    marco1 = tk.Frame(crea_torneo, bg="#000000")
    marco1.grid(row=0, column=1, padx=20, pady=20)


    mensaje1 = tk.Label(marco1, text="Crea tu Torneo:", fg="yellow", bg="#000000", font=("Arial", 20, "bold"))
    mensaje1.grid(row=0, column=0, sticky="w")

    # Datos básicos
    tk.Label(marco1, text="Nombre:", fg="white", bg="#000000").grid(row=1, column=0, sticky="w")
    entrada_nombre = tk.Entry(marco1)
    entrada_nombre.grid(row=1, column=0)

    tk.Label(marco1, text="Fecha:", fg="white", bg="#000000").grid(row=2, column=0, sticky="w")
    entrada_fecha = tk.Entry(marco1)
    entrada_fecha.grid(row=2, column=0)

    tk.Label(marco1, text="Lugar:", fg="white", bg="#000000").grid(row=3, column=0, sticky="w")
    entrada_lugar = tk.Entry(marco1)
    entrada_lugar.grid(row=3, column=0)

    tk.Label(marco1, text="Numero de luchas:", fg="white", bg="#000000").grid(row=4, column=0, sticky="w")
    entrada_luchas = tk.Entry(marco1)
    entrada_luchas.grid(row=4, column=0)

    mensaje = tk.Label(marco1, text="Selecciona el modo de seleccionar personajes:?", font=("Arial", 14), bg="#000000", fg="white")
    mensaje.grid(row=8, column=0, pady=10, sticky="ew")

    etiqueta = tk.Label(marco1, text="Guarda tus datos antes de seguir", font=("Arial", 14), bg="#000000", fg="white")
    etiqueta.grid(row=8, column=0, pady=10, sticky="ew")

    boton_guardar = tk.Button(marco1, text="Guardar Datos del Torneo", font=("Arial", 14), bg="green", fg="white",
                          command=lambda: guardar_datos(entrada_nombre, entrada_fecha, entrada_lugar, entrada_luchas))
    boton_guardar.grid(row=7, column=0, pady=10, sticky="ew")

    boton_manual = tk.Button(marco1, text="Manual", font=("Arial", 14), bg="gray", fg="black", command=lambda: manual(crea_torneo))
    boton_manual.grid(row=9, column=0, pady=10, sticky="ew")

    boton_vsbot = tk.Button(marco1, text="Persona vs Programa", font=("Arial", 14), bg="gray", fg="black", command=lambda: vsbot(crea_torneo))
    boton_vsbot.grid(row=10, column=0, pady=10, sticky="ew")

    boton_auto = tk.Button(marco1, text = "Programa vs Programa", font = ("Arial", 14), bg="gray", fg="black", command=lambda: auto(crea_torneo))
    boton_auto.grid(row=11, column=0, pady=10, sticky="ew")

    salir_boton = tk.Button(marco1, text="Volver al menu principal", font=("Arial", 14), bg="#FFFFFF", fg="black", command=lambda:[menu_inicio(""),crea_torneo.destroy()])
    salir_boton.grid(row=12, column=0, pady=10, sticky="ew")

    def guardar_datos(nombre_e, fecha_e, lugar_e, luchas_e):
        nombre = nombre_e.get()
        fecha = fecha_e.get()
        lugar = lugar_e.get()
        numero_de_luchas = luchas_e.get()

        if nombre == "" or fecha == "" or lugar == "" or numero_de_luchas == "":
            messagebox.showwarning("Campos incompletos", "Por favor, completa todos los campos.")
            return

        with open("Programa/Datos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{fecha},{lugar},{numero_de_luchas}\n")

        messagebox.showinfo("Guardado", "Datos Guardados exitosamente.")
        
    
#E:-
#S:llama a manual final
#R:seleccionar todos los personajes
#O:Muestra un submenu para que el usuario cree su torneo
def manual(menu):
    menu.destroy()
    ventana_manual = tk.Toplevel()
    ventana_manual.title("Modo Manual")
    ventana_manual.configure(bg="#000000")
    ancho_ventana = 450
    alto_ventana = 400
    pantalla_ancho = ventana_manual.winfo_screenwidth()
    pantalla_alto = ventana_manual.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
    y = int((pantalla_alto / 2) - (alto_ventana / 2))
    ventana_manual.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    marco = tk.Frame(ventana_manual, bg="#000000")
    marco.grid(row=0, column=0, padx=20, pady=20)

    mensaje = tk.Label(marco, text="Modo Manual Seleccionado", font=("Arial", 16), bg="#000000", fg="white")
    mensaje.grid(row=0, column=1, sticky="ew", pady=20)

    instrucciones = tk.Label(marco, text="Selecciona manualmente 5 personajes por bando", bg="#000000", fg="white")
    instrucciones.grid(row=1, column=1, sticky="ew", pady=10)

    def iniciar_seleccion():
        bando1 = seleccionar_personajes1()
        if len(bando1) < 5:
            messagebox.showwarning("Advertencia", "Debe seleccionar 5 personajes para el Bando 1")
            return
        bando2 = seleccionar_personajes2()
        if len(bando2) < 5:
            messagebox.showwarning("Advertencia", "Debe seleccionar 5 personajes para el Bando 2")
            return
        
        manualfinal(bando1, bando2)

    boton_iniciar = tk.Button(marco, text="Iniciar Selección de Bandos", font=("Arial", 14), bg="green", fg="white",
                              command=iniciar_seleccion)
    boton_iniciar.grid(row=4, column=1, pady=20)
    etiquetamensaje = tk.Label(marco, text="nota: Se te abrira un menu para seleccionar los primeros 5 seran bando 1 los otros 5 seran bando 2", font=("Arial", 16), bg="#000000", fg="white")
    etiquetamensaje.grid(row=5, column=1, sticky="ew", pady=20)

#E:-
#S:la seleccion de personajes que el usuario selecciono
#R:solo selecciona lo que se le muestra
#O: Menu donde el usuario selecciona los personajes que quiere en su bando
def seleccionar_personajes1():
    bando1 = []

    ventana_sp = tk.Toplevel()
    ventana_sp.title("Seleccionar Personajes")
    ventana_sp.geometry("600x700")
    ventana_sp.configure(bg="#000000")

    titulo = tk.Label(ventana_sp, text="Selecciona 5 personajes", font=("Arial", 16, "bold"),
                      bg="#000000", fg="yellow")
    titulo.pack(pady=10)

    try:
        with open("Programa/Luchadores.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except:
        messagebox.showerror("Error", "No se pudo leer el archivo de luchadores.")
        return []

    # Scroll
    contenedor = tk.Frame(ventana_sp, bg="#000000")
    contenedor.pack(fill="both", expand=True)

    canvas = tk.Canvas(contenedor, bg="#000000", highlightthickness=0)
    scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    frame_scroll = tk.Frame(canvas, bg="#000000")
    canvas.create_window((0, 0), window=frame_scroll, anchor="nw")

    def actualizar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_scroll.bind("<Configure>", actualizar_scroll)

    for linea in lineas:
        datos = linea.strip().split(",")
        if len(datos) >= 15:
            tipo = datos[0].strip(" '")
            sexo = datos[1].strip(" '")
            nombre = datos[2].strip(" '")
            alter = datos[3].strip(" '")
            ruta = datos[4].strip(" '")

            marco = tk.Frame(frame_scroll, bg="#1a1a1a", bd=2, relief="ridge")
            marco.pack(padx=10, pady=10, fill="x")

            # Imagen
            try:
                imagen = Image.open(ruta)
                imagen = imagen.resize((100, 100), Image.Resampling.LANCZOS)
                imagen_tk = ImageTk.PhotoImage(imagen)
                etiqueta_img = tk.Label(marco, image=imagen_tk, bg="#1a1a1a")
                etiqueta_img.image = imagen_tk
                etiqueta_img.grid(row=0, column=0, rowspan=4, padx=10)
            except:
                etiqueta_img = tk.Label(marco, text="Sin imagen", bg="#1a1a1a", fg="red")
                etiqueta_img.grid(row=0, column=0, rowspan=4, padx=10)

            # Nombre y tipo
            texto = tk.Label(marco, text=f"{alter} ({nombre}) - Tipo: {tipo} - Sexo: {sexo}",
                             bg="#1a1a1a", fg="white")
            texto.grid(row=0, column=1, sticky="w")

            # Atributos
            atributos = "Vel: " + datos[5] + "  Fue: " + datos[6] + "  Int: " + datos[7] + "  Def: " + datos[8] + "\n" + \
                        "Mag: " + datos[9] + "  Tel: " + datos[10] + "  Est: " + datos[11] + "  Vol: " + datos[12] + "\n" + \
                        "Eli: " + datos[13] + "  Reg: " + datos[14]

            info = tk.Label(marco, text=atributos, bg="#1a1a1a", fg="yellow", justify="left")
            info.grid(row=1, column=1, sticky="w")

            # Botón seleccionar
            #E:en al se guarda el valor del alter que se selecciona y en marco se guarda el frame que muestra el personaje en pantalla
            #S:se selecciona el personaje
            #R:seleccionar unicamente
            #O:brindar una seleccion al usuario
            def seleccionar(al=alter, marco_ref=marco):
                if len(bando1) < 5:
                    bando1.append(al)
                    marco_ref.destroy()
                    if len(bando1) == 5:
                        ventana_sp.destroy()
                else:
                    messagebox.showinfo("Listo", "Ya seleccionaste 5 personajes.")

            boton = tk.Button(marco, text="Seleccionar", bg="green", fg="white",
                              command=lambda al=alter, marco_ref=marco: seleccionar(al, marco_ref))
            boton.grid(row=2, column=1, sticky="w")

    ventana_sp.wait_window()
    return bando1
#E:-
#S:la seleccion de personajes que el usuario selecciono
#R:solo selecciona lo que se le muestra
#O: Menu donde el usuario selecciona los personajes que quiere en su bando
def seleccionar_personajes2():
    bando2 = []

    ventana_sp = tk.Toplevel()
    ventana_sp.title("Seleccionar Personajes")
    ventana_sp.geometry("600x700")
    ventana_sp.configure(bg="#000000")

    titulo = tk.Label(ventana_sp, text="Selecciona 5 personajes", font=("Arial", 16, "bold"),
                      bg="#000000", fg="yellow")
    titulo.pack(pady=10)

    try:
        with open("Programa/Luchadores.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except:
        messagebox.showerror("Error", "No se pudo leer el archivo de luchadores.")
        return []

    # Scroll
    contenedor = tk.Frame(ventana_sp, bg="#000000")
    contenedor.pack(fill="both", expand=True)

    canvas = tk.Canvas(contenedor, bg="#000000", highlightthickness=0)
    scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    frame_scroll = tk.Frame(canvas, bg="#000000")
    canvas.create_window((0, 0), window=frame_scroll, anchor="nw")

    def actualizar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_scroll.bind("<Configure>", actualizar_scroll)

    for linea in lineas:
        datos = linea.strip().split(",")
        if len(datos) >= 15:
            tipo = datos[0].strip(" '")
            sexo = datos[1].strip(" '")
            nombre = datos[2].strip(" '")
            alter = datos[3].strip(" '")
            ruta = datos[4].strip(" '")

            marco = tk.Frame(frame_scroll, bg="#1a1a1a", bd=2, relief="ridge")
            marco.pack(padx=10, pady=10, fill="x")

            # Imagen
            try:
                imagen = Image.open(ruta)
                imagen = imagen.resize((100, 100), Image.Resampling.LANCZOS)
                imagen_tk = ImageTk.PhotoImage(imagen)
                etiqueta_img = tk.Label(marco, image=imagen_tk, bg="#1a1a1a")
                etiqueta_img.image = imagen_tk
                etiqueta_img.grid(row=0, column=0, rowspan=4, padx=10)
            except:
                etiqueta_img = tk.Label(marco, text="Sin imagen", bg="#1a1a1a", fg="red")
                etiqueta_img.grid(row=0, column=0, rowspan=4, padx=10)

            # Nombre y tipo
            texto = tk.Label(marco, text=f"{alter} ({nombre}) - Tipo: {tipo} - Sexo: {sexo}",
                             bg="#1a1a1a", fg="white")
            texto.grid(row=0, column=1, sticky="w")

            # Atributos
            atributos = "Vel: " + datos[5] + "  Fue: " + datos[6] + "  Int: " + datos[7] + "  Def: " + datos[8] + "\n" + \
                        "Mag: " + datos[9] + "  Tel: " + datos[10] + "  Est: " + datos[11] + "  Vol: " + datos[12] + "\n" + \
                        "Eli: " + datos[13] + "  Reg: " + datos[14]

            info = tk.Label(marco, text=atributos, bg="#1a1a1a", fg="yellow", justify="left")
            info.grid(row=1, column=1, sticky="w")

            # Botón seleccionar
            def seleccionar(al=alter, marco_ref=marco):
                if len(bando2) < 5:
                    bando2.append(al)
                    marco_ref.destroy()
                    if len(bando2) == 5:
                        ventana_sp.destroy()
                else:
                    messagebox.showinfo("Listo", "Ya seleccionaste 5 personajes.")

            boton = tk.Button(marco, text="Seleccionar", bg="green", fg="white",
                              command=lambda al=alter, marco_ref=marco: seleccionar(al, marco_ref))
            boton.grid(row=2, column=1, sticky="w")

    ventana_sp.wait_window()
    return bando2
#E:bando1 y bando2
#S:muestra un menu donde se guardan los datos y se crea el torneo
#R:-
#O:Muestra un menu final para que el usuario confirme que quiere crear el torneo
def manualfinal(bando1, bando2):
    ventana_final = tk.Toplevel()
    ventana_final.title("Torneo Manual")
    ventana_final.geometry("1200x600")
    ventana_final.configure(bg="black")

    titulo = tk.Label(ventana_final, text="Torneo Manual", font=("Arial", 24, "bold"),
                      bg="black", fg="white")
    titulo.grid(row=0, column=0, columnspan=3, pady=20)

    mensaje = tk.Label(ventana_final, text="Bandos Seleccionados", font=("Arial", 16),
                       bg="black", fg="white")
    mensaje.grid(row=1, column=0, columnspan=3, pady=10)

    lbl1 = tk.Label(ventana_final, text="Bando 1", font=("Arial", 16, "bold"),
                    bg="black", fg="cyan")
    lbl1.grid(row=2, column=0)

    lblvs = tk.Label(ventana_final, text="VS", font=("Arial", 16, "bold"),
                     bg="black", fg="white")
    lblvs.grid(row=2, column=1)

    lbl2 = tk.Label(ventana_final, text="Bando 2", font=("Arial", 16, "bold"),
                    bg="black", fg="red")
    lbl2.grid(row=2, column=2)

    def mostrar_bando(bando, columna):
        for i in range(5):
            personaje = bando[i]
            etiqueta = tk.Label(ventana_final, text=personaje, bg="black", fg="white", wraplength=100)
            etiqueta.grid(row=3 + i, column=columna, padx=20, pady=10)

    mostrar_bando(bando1, 0)
    mostrar_bando(bando2, 2)

    boton_crear_torneo = tk.Button(ventana_final, text="Crear Torneo", font=("Arial", 14), bg="green", fg="white",
                                    command=lambda: guardartorneo(bando1, bando2))
    boton_crear_torneo.grid(row=8, column=0, columnspan=3, pady=20)

#E:bando1, bando2
#S:guardar datos
#R:-
#O:guarda el torneo creado en datos.txt
def guardartorneo(bando1, bando2):
    with open("Programa/Datos.txt", "a", encoding="utf-8") as archivo:
        archivo.write("Bando 1: "+ "\n" + ", ".join(bando1) + "\n")
        archivo.write("Bando 2: " + "\n"+ ", ".join(bando2) + "\n")

    messagebox.showinfo("Listo", "Torneo guardado exitosamente")
    menu_inicio(Persona="")  # Regresa al menú principal
#E:-
#S:da el bando aleatoriamente
#R:-
#O:Funcion que unicamente crea un bando aleatoriamente
def seleccionar_personajes_random():
    seleccionados = []

    try:
        archivo = open("Programa/Luchadores.txt", "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
    except:
        messagebox.showerror("Error", "No se pudo abrir el archivo Luchadores.txt")
        return []

    # Revisar que hay suficientes personajes
    if len(lineas) < 5:
        messagebox.showwarning("Advertencia", "No hay suficientes personajes para seleccionar 5 al azar")
        return []

    # Seleccionar 5 líneas aleatorias sin repeticion
    seleccionados = random.sample(lineas, 5)

    # Obtener el alter ego de cada personaje (posición 4 del texto)
    resultado = []
    for linea in seleccionados:
        partes = linea.strip().split(",")
        if len(partes) >= 4:
            alter = partes[3].strip(" '")
            resultado.append(alter)

    return resultado
  
#E:-
#S:da el bando aleatoriamente
#R:-
#O:Funcion que unicamente crea un bando aleatoriamente
def seleccionar_personajes_random1():
    seleccionados = []

    try:
        archivo = open("Programa/Luchadores.txt", "r", encoding="utf-8")
        lineas = archivo.readlines()
        archivo.close()
    except:
        messagebox.showerror("Error", "No se pudo abrir el archivo Luchadores.txt")
        return []

    # Revisar que hay suficientes personajes
    if len(lineas) < 5:
        messagebox.showwarning("Advertencia", "No hay suficientes personajes para seleccionar 5 al azar")
        return []

    # Seleccionar 5 líneas aleatorias sin repeticion
    seleccionados = random.sample(lineas, 5)

    # Obtener el alter ego de cada personaje (posición 4 del texto)
    resultado = []
    for linea in seleccionados:
        partes = linea.strip().split(",")
        if len(partes) >= 4:
            alter = partes[3].strip(" '")
            resultado.append(alter)

    return resultado
#E:-
#S:Bando1 seleccionado, bando2 random
#R:-
#O:submenu que selecciona sus personajes para el bando 1 y el bando 2 random
def vsbot(menu):
    menu.destroy()
    ventana_vsbot = tk.Toplevel()
    ventana_vsbot.title("Modo Persona vs Programa")
    ventana_vsbot.configure(bg="#000000")
    ancho_ventana = 300
    alto_ventana = 400
    pantalla_ancho = ventana_vsbot.winfo_screenwidth()
    pantalla_alto = ventana_vsbot.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
    y = int((pantalla_alto / 2) - (alto_ventana / 2))
    ventana_vsbot.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    marco = tk.Frame(ventana_vsbot, bg="#000000")
    marco.grid(row=0, column=0, padx=20, pady=20)

    mensaje = tk.Label(marco, text="Modo Persona vs Programa", font=("Arial", 16), bg="#000000", fg="white")
    mensaje.grid(row=0, column=0, columnspan=2, pady=20)

    # Variables internas para almacenar los bandos
    bando1 = []
    bando_programa = []

    def seleccionar_jugador():
        nonlocal bando1
        bando1 = seleccionar_personajes1()

    def seleccionar_programa():
        nonlocal bando_programa
        bando_programa = seleccionar_personajes_random()
        messagebox.showinfo("Listo", "El programa seleccionó sus personajes.")

    def continuar():
        if len(bando1) < 5 or len(bando_programa) < 5:
            messagebox.showwarning("Advertencia", "Ambos bandos deben tener 5 personajes.")
            return
        ventana_vsbot.destroy()
        vsbotfinal(bando1, bando_programa)

    boton_jugador = tk.Button(marco, text="Seleccionar (Jugador)", font=("Arial", 14), bg="green", fg="white",
                              command=seleccionar_jugador)
    boton_jugador.grid(row=1, column=0, pady=10, columnspan=2)

    boton_programa = tk.Button(marco, text="Seleccionar (Programa)", font=("Arial", 14), bg="green", fg="white",
                               command=seleccionar_programa)
    boton_programa.grid(row=2, column=0, pady=10, columnspan=2)

    boton_siguiente = tk.Button(marco, text="Siguiente", font=("Arial", 14), bg="blue", fg="white",
                                command=continuar)
    boton_siguiente.grid(row=3, column=0, pady=10, columnspan=2)

    ventana_vsbot.mainloop()
#E:equipo1, equipo2
#S:crea torneo con los bandos
#R:-
#O:menu final donde el usuario cre el torneo y se muestran los bandos
def vsbotfinal(equipo1, equipo2):
    ventana_final = tk.Toplevel()
    ventana_final.title("Torneo Manual")
    ventana_final.geometry("1200x600")
    ventana_final.configure(bg="black")

    titulo = tk.Label(ventana_final, text="Torneo Manual vs Programa", font=("Arial", 24, "bold"),
                      bg="black", fg="white")
    titulo.grid(row=0, column=0, columnspan=3, pady=20)

    mensaje1 = tk.Label(ventana_final, text="Bandos Seleccionados", font=("Arial", 16),
                       bg="black", fg="white")
    mensaje1.grid(row=1, column=0, columnspan=3, pady=10)

    b1 = tk.Label(ventana_final, text="Bando 1", font=("Arial", 16, "bold"),
                    bg="black", fg="cyan")
    b1.grid(row=2, column=0)

    b2 = tk.Label(ventana_final, text="VS", font=("Arial", 16, "bold"),
                     bg="black", fg="white")
    b2.grid(row=2, column=1)

    b3 = tk.Label(ventana_final, text="Bando 2", font=("Arial", 16, "bold"),
                    bg="black", fg="red")
    b3.grid(row=2, column=2)

    def mostrar_bando(bando, columna):
        for i in range(5):
            personaje = bando[i]
            etiqueta = tk.Label(ventana_final, text=personaje, bg="black", fg="white", wraplength=100)
            etiqueta.grid(row=3 + i, column=columna, padx=20, pady=10)

    mostrar_bando(equipo1, 0)
    mostrar_bando(equipo2, 2)

    boton_crear_torneo = tk.Button(ventana_final, text="Crear Torneo", font=("Arial", 14), bg="green", fg="white",
                                    command=lambda: guardartorneo(equipo1, equipo2))
    boton_crear_torneo.grid(row=8, column=0, columnspan=3, pady=20)
#E:-
#S:menu final para crear torneo
#R:-
#O:Menu auto que muestra y da para que el programa seleccione sus bandos
def auto(menu):
    menu.destroy()
    ventana_auto = tk.Toplevel()
    ventana_auto.title("Modo Persona vs Programa")
    ventana_auto.configure(bg="#000000")
    ancho_ventana = 250
    alto_ventana = 400
    pantalla_ancho = ventana_auto.winfo_screenwidth()
    pantalla_alto = ventana_auto.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
    y = int((pantalla_alto / 2) - (alto_ventana / 2))
    ventana_auto.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    marco = tk.Frame(ventana_auto, bg="#000000")
    marco.grid(row=0, column=0, padx=20, pady=20)

    mensaje = tk.Label(marco, text="Programa vs Programa", font=("Arial", 16), bg="#000000", fg="white")
    mensaje.grid(row=0, column=0, columnspan=2, pady=20)

    # Variables internas para almacenar los bandos
    bando1 = []
    bando_programa = []

    

    def seleccionar_programa1():
        nonlocal bando1
        bando1 = seleccionar_personajes_random1()
        messagebox.showinfo("Listo", "El programa seleccionó sus personajes.")
    def seleccionar_programa():
        nonlocal bando_programa
        bando_programa = seleccionar_personajes_random()
        messagebox.showinfo("Listo", "El programa seleccionó sus personajes.")
    def continuar():
        if len(bando1) < 5 or len(bando_programa) < 5:
            messagebox.showwarning("Advertencia", "Ambos bandos deben tener 5 personajes.")
            return
        ventana_auto.destroy()
        autofinal(bando1, bando_programa)

    boton_jugador = tk.Button(marco, text="Seleccionar (Programa)", font=("Arial", 14), bg="green", fg="white",
                              command=seleccionar_programa1)
    boton_jugador.grid(row=1, column=0, pady=10, columnspan=2)

    etiqueta = tk.Label(marco, text= " VS ", font=("Arial", 16), bg="#000000", fg="white")
    etiqueta.grid(row=2, column=0, columnspan=2, pady=20)

    boton_programa = tk.Button(marco, text="Seleccionar (Programa)", font=("Arial", 14), bg="green", fg="white",
                               command=seleccionar_programa)
    boton_programa.grid(row=3, column=0, pady=10, columnspan=2)

    boton_siguiente = tk.Button(marco, text="Siguiente", font=("Arial", 14), bg="blue", fg="white",
                                command=continuar)
    boton_siguiente.grid(row=4, column=0, pady=10, columnspan=2)

    ventana_auto.mainloop()
#E:equipos
#S:crea eñ torneo y lo guarda
#R:-
#O:menu final que cuando se presione el boton guarda el torneo
def autofinal(equipo1, equipo2):
    ventana_fi = tk.Toplevel()
    ventana_fi.title("Modo programa vs programa")
    ventana_fi.geometry("1200x600")
    ventana_fi.configure(bg="black")

    titulo = tk.Label(ventana_fi, text="Programa vs Programa", font=("Arial", 24, "bold"),
                      bg="black", fg="white")
    titulo.grid(row=0, column=0, columnspan=3, pady=20)

    mensaje1 = tk.Label(ventana_fi, text="Bandos Seleccionados", font=("Arial", 16),
                       bg="black", fg="white")
    mensaje1.grid(row=1, column=0, columnspan=3, pady=10)

    bo1 = tk.Label(ventana_fi, text="Bando 1", font=("Arial", 16, "bold"),
                    bg="black", fg="cyan")
    bo1.grid(row=2, column=0)

    bo2 = tk.Label(ventana_fi, text="VS", font=("Arial", 16, "bold"),
                     bg="black", fg="white")
    bo2.grid(row=2, column=1)

    bo3 = tk.Label(ventana_fi, text="Bando 2", font=("Arial", 16, "bold"),
                    bg="black", fg="red")
    bo3.grid(row=2, column=2)

    def mostrar_bando(bando, columna, contenedor):
        for i in range(5):
            personaje = bando[i]
            etiqueta = tk.Label(contenedor, text=personaje, bg="black", fg="white", wraplength=100)
            etiqueta.grid(row=3 + i, column=columna, padx=20, pady=10)
            

    mostrar_bando(equipo1, 0, ventana_fi)
    mostrar_bando(equipo2, 2, ventana_fi)

    boton_crear_torneo = tk.Button(ventana_fi, text="Crear Torneo", font=("Arial", 14), bg="green", fg="white",
                                    command=lambda: guardartorneo(equipo1, equipo2))
    boton_crear_torneo.grid(row=8, column=0, columnspan=3, pady=20)
#E:-
#S:borra el torneo
#R:borra los torneos existentes
#O:menu para borrar un torneo existente
def ventana_borrar_torneo(menu):
    menu.destroy()
    ventana = tk.Toplevel()
    ventana.title("Eliminar Torneo")
    ventana.configure(bg="#000000")
    ventana.geometry("500x500")

    marco = tk.Frame(ventana, bg="black")
    marco.grid(row=0, column=0, padx=20, pady=20)

    tk.Label(marco, text="Torneos disponibles:", bg="black", fg="yellow", font=("Arial", 14)).grid(row=0, column=0, sticky="w", pady=10)

    # Leer archivo y mostrar solo los nombres correctos de torneo
    try:
        with open("Programa/Datos.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except:
        messagebox.showerror("Error", "No se pudo abrir el archivo Datos.txt")
        ventana.destroy()
        return

    nombres_torneos = []
    fila = 1
    for linea in lineas:
        partes = linea.strip().split(",")
        if len(partes) == 4:
            nombre = partes[0].strip()
            if nombre != "":
                nombres_torneos.append(nombre)#si el torneo se encuentra lo muestra en pantalla
                tk.Label(marco, text=nombre, bg="black", fg="white", font=("Arial", 12)).grid(row=fila, column=0, sticky="w")
                fila += 1

    # Entrada para escribir el nombre a eliminar
    tk.Label(marco, text="\nEscriba el nombre exacto del torneo a eliminar:", bg="black", fg="white").grid(row=fila + 1, column=0, sticky="w")
    entrada = tk.Entry(marco)
    entrada.grid(row=fila + 2, column=0, pady=5)

    def confirmar_eliminacion():
        nombre = entrada.get().strip()#elimina cualquier espacio o campo que no tenga texto ejemplo "torneo "
        if nombre == "":
            messagebox.showwarning("Campo vacío", "Por favor escriba un nombre de torneo.")
            return

        if nombre not in nombres_torneos:
            messagebox.showwarning("No encontrado", f"No se encontró el torneo '{nombre}'.")
            return

        borrar_torneo_completo(nombre)
        messagebox.showinfo("Éxito", f"Torneo '{nombre}' eliminado correctamente.")
        menu_inicio("")

    # Botón para eliminar
    tk.Button(marco, text="Eliminar Torneo", bg="red", fg="white", command=confirmar_eliminacion).grid(row=fila + 3, column=0, pady=20)

#E:nombre del torneo
#S:borra o limpia datos.txt
#R:debe existir el torneo
#O:Borra un torneo existente
def borrar_torneo_completo(nombre_torneo):
    lineas_nuevas = []
    with open("Programa/Datos.txt", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    i = 0
    while i < len(lineas):
        linea = lineas[i].strip()
        if linea.startswith(nombre_torneo + ","):  # Compara nombre exacto con la primera línea
            i = i + 5  # Salta la línea del torneo y las dos siguientes (bando 1 y bando 2)
        else:
            lineas_nuevas.append(lineas[i])
            i = i + 1

    with open("Programa/Datos.txt", "w", encoding="utf-8") as archivo:
        for linea in lineas_nuevas:
            archivo.write(linea)

#E:-
#S:inicia torneo y se muestran las luchas
#R:debe extir el archivo de datos
#O:funcionalidad de jugar torneo carga un torneo aleatorio       
def jugar(menu):
    menu.destroy()
    ventana_jug = tk.Toplevel()
    ventana_jug.title("Submenú de Torneos")
    ventana_jug.configure(bg="#000000")

    ancho_ventana = 550
    alto_ventana = 400
    pantalla_ancho = ventana_jug.winfo_screenwidth()
    pantalla_alto = ventana_jug.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
    y = int((pantalla_alto / 2) - (alto_ventana / 2))
    ventana_jug.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    marco = tk.Frame(ventana_jug, bg="black")
    marco.grid(row=0, column=0, padx=20, pady=20)

    tk.Label(marco, text="Juega Un Torneo", font=("Arial", 24), bg="black", fg="white").grid(row=0, column=0, pady=10, sticky="w")
    tk.Label(marco, text="Torneos disponibles:", bg="black", fg="yellow", font=("Arial", 14)).grid(row=1, column=0, sticky="w")

    try:
        with open("Programa/Datos.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
    except:
        messagebox.showerror("Error", "No se pudo abrir el archivo Datos.txt")
        ventana_jug.destroy()
        return

    nombres_torneos = []
    fila = 2
    for linea in lineas:
        partes = linea.strip().split(",")
        if len(partes) == 4:
            nombre = partes[0].strip()
            if nombre != "":
                nombres_torneos.append(nombre)
                tk.Label(marco, text=nombre, bg="black", fg="white", font=("Arial", 12)).grid(row=fila, column=0, sticky="w")
                fila += 1

    tk.Label(marco, text="Digite el nombre del torneo:", fg="white", bg="#000000").grid(row=fila, column=0, sticky="w")
    entrada_torneo = tk.Entry(marco)
    entrada_torneo.grid(row=fila + 1, column=0, pady=10)

    def ejecutar_torneo():
        nombre = entrada_torneo.get().strip()
        if nombre == "":
            messagebox.showwarning("Error", "Debe ingresar un nombre.")
        else:
            iniciar_torneo_desde_archivo(nombre)

    tk.Button(marco, text="Iniciar Torneo", bg="green", fg="white", command=ejecutar_torneo).grid(row=fila + 2, column=0, pady=20)

#E:-
#S:estadisticas.txt se escriben las estadisticas
#R:-
#O:menu de estadisticas que muestra las estadisticas 
def estadisticas(menuant):
    menuant.destroy()
    estadisticas_vent = tk.Toplevel()
    estadisticas_vent.configure(bg = "#000000")
    estadisticas_vent.title("Estadisticas")

    ancho_ventana = 750
    alto_ventana = 700
    pantalla_ancho = estadisticas_vent.winfo_screenwidth()
    pantalla_alto = estadisticas_vent.winfo_screenheight()
    x = int((pantalla_ancho / 2) - (ancho_ventana / 2))
    y = int((pantalla_alto / 2) - (alto_ventana / 2))
    estadisticas_vent.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

    marco = tk.Frame(estadisticas_vent, bg="black")
    marco.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    tk.Label(marco, text="Estadísticas del Juego", font=("Arial", 24), bg="black", fg="white").pack(pady=(0, 20))
    
    try:
        heroes, villanos = cantidad_heroes()
        cont_torneos = cantidad_torneos()
        ganadas, perdidas = estadisticas_luchas()
        apariciones = participaciones_por_personaje()
        max_heroe_g = "Ninguno"
        max_ganadas = -1
        for p in ganadas:
            if tipo_personaje(p) == "Héroe":
                if ganadas[p] > max_ganadas:
                    max_ganadas = ganadas[p]
                    max_heroe_g = p

        max_heroe_p = "Ninguno"
        max_perdidas = -1
        for p in perdidas:
            if tipo_personaje(p) == "Héroe":
                if perdidas[p] > max_perdidas:
                    max_perdidas = perdidas[p]
                    max_heroe_p = p

        max_villano_g = "Ninguno"
        max_ganadas_v = -1
        for p in ganadas:
            if tipo_personaje(p) == "Villano":
                if ganadas[p] > max_ganadas_v:
                    max_ganadas_v = ganadas[p]
                    max_villano_g = p

        max_villano_p = "Ninguno"
        max_perdidas_v = -1
        for p in perdidas:
            if tipo_personaje(p) == "Villano":
                if perdidas[p] > max_perdidas_v:
                    max_perdidas_v = perdidas[p]
                    max_villano_p = p

        max_apar_heroe = "Ninguno"
        max_apariciones_h = -1
        for p in apariciones:
            if tipo_personaje(p) == "Héroe":
                if apariciones[p] > max_apariciones_h:
                    max_apariciones_h = apariciones[p]
                    max_apar_heroe = p

        max_apar_villano = "Ninguno"
        max_apariciones_v = -1
        for p in apariciones:
            if tipo_personaje(p) == "Villano":
                if apariciones[p] > max_apariciones_v:
                    max_apariciones_v = apariciones[p]
                    max_apar_villano = p
            
            tk.Label(marco, text=f"Héroes: {heroes}", font=("Arial", 16), fg="cyan", bg="black").pack(pady=10)
            tk.Label(marco, text=f"Villanos: {villanos}", font=("Arial", 16), fg="red", bg="black").pack(pady=10)
            tk.Label(marco, text=f"Torneos: {cont_torneos}", font=("Arial", 16), fg="yellow", bg="black").pack(pady=10)
            tk.Label(marco, text=f"Total de luchadores: {heroes + villanos}", font=("Arial", 16), fg="green", bg="black").pack(pady=10)
            
            with open("Programa/estadisticas.txt", "w", encoding="utf-8") as estadisticas_file:
                estadisticas_file.write(f"Heroes: {heroes}\n")
                estadisticas_file.write(f"Villanos: {villanos}\n")
                estadisticas_file.write(f"Torneos: {cont_torneos}\n")
                estadisticas_file.write(f"Total de luchadores: {heroes + villanos}\n")
            
    except Exception as e:
        tk.Label(marco, text=f"Error al generar estadísticas: {e}", font=("Segoe UI", 12), fg="red", bg="black").pack(pady=10)
    
    tk.Label(marco, text=f"Cantidad de torneos: {cont_torneos}", font=("Arial", 12), fg="blue", bg="black").pack(pady=10)
    tk.Label(marco, text=f"Cantidad de heroes: {heroes}", font=("Arial", 12), fg="yellow", bg="black").pack(pady=10)
    tk.Label(marco, text=f"Cantidad de Villano: {villanos}", font=("Arial", 12), fg="yellow", bg="black").pack(pady=10)
    tk.Label(marco, text=f"Héroe con más luchas ganadas: {max_heroe_g}", font=("Arial", 12), fg="blue", bg="black").pack(pady=10)
    tk.Label(marco, text=f"Héroe con más luchas perdidas: {max_heroe_p}", font=("Arial", 12), fg="yellow", bg="black").pack(pady=10)
    tk.Label(marco, text=f"Villano con más luchas ganadas: {max_villano_g}", font=("Arial", 12), fg="gray", bg="black").pack(pady=10)
    tk.Label(marco, text=f"Villano con más luchas perdidas: {max_villano_p}", font=("Arial", 12), fg="red", bg="black").pack(pady=10)
    tk.Label(marco, text=f"Héroe con más torneos: {max_apar_heroe}", font=("Arial", 12), fg="green", bg="black").pack(pady=10)
    tk.Label(marco, text=f"Villano con más torneos: {max_apar_villano}", font=("Arial", 12), fg="white", bg="black").pack(pady=10)
    
    tk.Button(marco, text="Cerrar", 
              font=("Arial", 12), bg="#FF0000", fg="white",
              command=estadisticas_vent.destroy).pack(pady=10)
        
#E: abre el txt de luchadores
#S: retorna la cantidad de heroes y villanos que hay creados
#R: no tiene restriciones

def cantidad_heroes():
    try:
        with open("Programa/Luchadores.txt", "r", encoding="utf-8") as luchadores:
            villanos = 0
            heroes = 0
            for luchador in luchadores:
                luchador = luchador.strip()
                if luchador and luchador.startswith("'V'"):
                    villanos += 1
                elif luchador and luchador.startswith("'H'"):
                    heroes += 1
            return heroes, villanos
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo Luchadores.txt: {e}")
        return 0, 0

    
#E: abre el txt de torneos
#S:la cantidad de torneos que existen
#R:-
def cantidad_torneos():
    cont = 0
    try:
        with open("Programa/Datos.txt", "r", encoding="utf-8") as torneos:
            lines = torneos.readlines()
            
        for linea in lines:
            partes = linea.strip().split(",")
            if len(partes) == 4:
                cont += 1
        return cont
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo abrir el archivo Datos.txt: {e}")
        return 0

#E:-
#S:añade las estadisticas a estadisticas.txt
#R:-
def añadir_estadisticas():
    try:
        heroes, villanos = cantidad_heroes()
        cont_torneos = cantidad_torneos()

        with open("Programa/estadisticas.txt", "w", encoding="utf-8") as estadisticas:
            estadisticas.write(f"Heroes: {heroes}\n")
            estadisticas.write(f"Villanos: {villanos}\n")
            estadisticas.write(f"Torneos: {cont_torneos}\n")
            estadisticas.write(f"Total de luchadores: {heroes + villanos}\n")

    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar estadísticas: {e}")
# E: No recibe parámetros.
# S: Devuelve dos diccionarios:
#    - ganadas: {nombre_personaje: cantidad_de_victorias}
#    - perdidas: {nombre_personaje: cantidad_de_derrotas}
# R: El archivo "Luchas.txt" debe existir y tener el formato correcto.
# O: Procesa el archivo Luchas.txt para contar cuántas luchas ha ganado y perdido cada personaje.
def estadisticas_luchas():
    ganadas = {}
    perdidas = {}
    try:
        with open("Programa/Luchas.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) < 5:
                    continue
                luchador1 = partes[0].strip()
                luchador2 = partes[1].strip()
                ganador = partes[3].strip()

                perdedor = luchador2 if ganador == luchador1 else luchador1

                ganadas[ganador] = ganadas.get(ganador, 0) + 1
                perdidas[perdedor] = perdidas.get(perdedor, 0) + 1
        return ganadas, perdidas
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo procesar Luchas.txt: {e}")
        return {}, {}

# E: alter: alter ego de un personaje
# S: Devuelve "Héroe", "Villano" o "Desconocido"
# R: El archivo "Luchadores.txt" debe existir y estar bien formateado
# O: Determina si un personaje es Héroe o Villano según su línea en Luchadores.txt
def tipo_personaje(alter):
    try:
        with open("Programa/Luchadores.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                if alter in linea:
                    return "Héroe" if linea.startswith("'H'") else "Villano"
    except:
        return "Desconocido"

# E: No recibe parámetros
# S: Devuelve un diccionario {nombre_personaje: cantidad_de_apariciones}
# R: El archivo "Datos.txt" debe estar bien estructurado
# O: Cuenta cuántas veces aparece cada personaje en los torneos registrados
def participaciones_por_personaje():
    apariciones = {}
    try:
        with open("Programa/Datos.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                if "Bando" in linea:
                    personajes = linea.strip().split(", ")
                    for personaje in personajes[1:]:
                        apariciones[personaje] = apariciones.get(personaje, 0) + 1
        return apariciones
    except:
        return {}
ventana.mainloop()