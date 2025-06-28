#Proyecto 4 
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import filedialog
import random

# Clase Personaje
class Personaje:
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

    def __str__(self):
        return f"'{self.tipo}', '{self.sexo}', '{self.nombre}', '{self.alter}', '{self.imagen}', " + \
               f"{self.velocidad},{self.fuerza},{self.inteligencia},{self.defensa}," + \
               f"{self.magia},{self.telepatia},{self.estrategia},{self.volar}," + \
               f"{self.elasticidad},{self.regeneracion}"

class Torneo:
    def __init__(self, Nombredeltorneo, Fecha, Lugardeltorneo, Numerosdeluchas, Bandoganador):
        self.Nombredeltorneo = Nombredeltorneo
        self.Fecha = Fecha
        self.Lugardeltorneo = Lugardeltorneo
        self.Numerosdeluchas = Numerosdeluchas
        self.Luchas = []
        self.Bandoganador = Bandoganador
       
class Lucha:
    def __init__(self, luchador1, luchador2, ganadorround1, ganadorround2, ganadorround3, ganadorlucha):
        self.luchador1 = luchador1
        self.luchador2 = luchador2
        self.ganadorround1 = ganadorround1
        self.ganadorround2 = ganadorround2
        self.ganadorround3 = ganadorround3
        self.ganadorlucha = ganadorlucha


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
imagen = Image.open("imagenes/logo1.png")
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
    archivo = open("usuarios.txt", "r", encoding="utf-8")
    UsuContra = archivo.readlines()
    i = 0
    usuario_input = entrada_usuario.get()
    contrasena_input = entrada_contrasena.get()

    while i < len(UsuContra):
        x = UsuContra[i]
        veri = x.split(";")
        Persona = veri[0].strip()
        usu = veri[1].strip()
        con = veri[2].strip()

        if usuario_input == usu and contrasena_input == con:
            messagebox.showinfo("Bienvenido", f"Hola {Persona}, acceso concedido.")
            return menu_inicio(Persona)  # Sale de la función si las credenciales son correctas

        i += 1

    # Si terminó el ciclo y no encontró nada válido
    messagebox.showerror("Error", "Usuario o contraseña incorrectos")

def menu_inicio(Persona):
    ventana.withdraw()  # Oculta la ventana principal sin cerrarla solo en este ya que las demas tienen funciones propias
    P=Persona
    # Crea una nueva ventana para el menú de inicio
    menu_ventana = tk.Tk()
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
    boton_Personajes = tk.Button(menu_ventana, text="Crear/Borrar Personajes", font=("Arial", 14), bg="#000000", fg="white", command=lambda: [menupersonajes(), menu_ventana.destroy()])
    boton_Personajes.grid(row=2, column=0, pady=10, sticky="ew")

    boton_torneos = tk.Button(menu_ventana, text="Crear/Borrar Torneos", font=("Arial", 14), bg="#000000", fg="white", command=lambda: submenutorneos())
    boton_torneos.grid(row=3, column=0, pady=10, sticky="ew")

    boton_Jugar = tk.Button(menu_ventana, text="Jugar", font=("Arial", 14), bg="#000000", fg="white", command=lambda: validadorcredenciales())
    boton_Jugar.grid(row=4, column=0, pady=10, sticky="ew")

    boton_estadisticas = tk.Button(menu_ventana, text="Estadisticas", font=("Arial", 14), bg="#000000", fg="white", command=lambda: validadorcredenciales())
    boton_estadisticas.grid(row=5, column=0, pady=10, sticky="ew")

    salir_boton = tk.Button(menu_ventana, text="Salir del Juego", font=("Arial", 14), bg="#000000", fg="white", command=menu_ventana.destroy)
    salir_boton.grid(row=6, column=0, pady=5, sticky="ew")

    menu_ventana.mainloop()

def submenutorneos():

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
    boton_crear_torneo = tk.Button(ventana_st, text="Crear Torneo", font=("Arial", 14), bg="#000000", fg="white", command=lambda: [crear_torneo(), ventana_st.destroy()])
    boton_crear_torneo.grid(row=2, column=0, pady=10, sticky="ew")
    boton_borrar_torneo = tk.Button(ventana_st, text="Borrar Torneo", font=("Arial", 14), bg="#000000", fg="white", command=crear_torneo)
    boton_borrar_torneo.grid(row=3, column=0, pady=10, sticky="ew")
    boton_volver = tk.Button(ventana_st, text="Volver al Menú Principal", font=("Arial", 14), bg="#000000", fg="white", command=lambda: [ventana_st.destroy(), menu_inicio()])
    boton_volver.grid(row=4, column=0, pady=10, sticky="ew")

    
    
def heroe():
    ventana_cp = tk.Toplevel()
    ventana_cp.title("Crear Personaje")
    ventana_cp.configure(bg="#0800FF")

    ventana_cp.geometry("400x700")

    marco = tk.Frame(ventana_cp, bg="#0800FF")
    marco.grid(row=0, column=1, padx=20, pady=20)

    def seleccionar_imagen():
        archivo = filedialog.askopenfilename(
            title="Seleccionar imagen",
            filetypes=[("Archivos de imagen", "*.jpg *.png *.jpeg *.gif")])
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

        with open("Luchadores.txt", "a", encoding="utf-8") as archivo:
            archivo.write(str(p) + "\n")

        messagebox.showinfo("Listo", "Personaje guardado")
        ventana_cp.destroy()

    boton_guardar = tk.Button(marco, text="Guardar Personaje", command=guardar)
    boton_guardar.grid(row=17, column=0, columnspan=2, pady=20)

def Villano():
    ventana_cp = tk.Toplevel()
    ventana_cp.title("Crear Personaje")
    ventana_cp.configure(bg="#FF0000")

    ventana_cp.geometry("400x700")

    marco = tk.Frame(ventana_cp, bg="#FF0000")
    marco.grid(row=0, column=1, padx=20, pady=20)

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

        with open("Luchadores.txt", "a", encoding="utf-8") as archivo:
            archivo.write(str(p) + "\n")

        messagebox.showinfo("Listo", "Personaje guardado")
        ventana_cp.destroy()

    boton_guardar = tk.Button(marco, text="Guardar Personaje", command=guardar)
    boton_guardar.grid(row=17, column=0, columnspan=2, pady=20)
  

def borrar_personaje():
    ventana_bp = tk.Toplevel()
    ventana_bp.title("Eliminar Personaje")
    ventana_bp.geometry("600x700")
    ventana_bp.configure(bg="#1e1e1e")

    titulo = tk.Label(ventana_bp, text="Eliminar Personaje", font=("Arial", 16, "bold"), bg="#1e1e1e", fg="white")
    titulo.pack(pady=10)

    archivo = open("Luchadores.txt", "r", encoding="utf-8")
    lineas = archivo.readlines()
    archivo.close()

    if len(lineas) == 0:
        sin_pj = tk.Label(ventana_bp, text="No hay personajes disponibles.", bg="#1e1e1e", fg="white")
        sin_pj.pack(pady=20)
        return

    # Scroll funcional con barra (sin rueda del mouse)
    contenedor = tk.Frame(ventana_bp, bg="#000000")
    contenedor.pack(fill="both", expand=True)

    canvas = tk.Canvas(contenedor, bg="#000000", highlightthickness=0)
    scrollbar = tk.Scrollbar(contenedor, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)

    frame_scroll = tk.Frame(canvas, bg="#000000")
    canvas.create_window((0, 0), window=frame_scroll, anchor="nw")

    # Ajustar área visible al tamaño de contenido
    def actualizar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame_scroll.bind("<Configure>", actualizar_scroll)

    # Redirigir widgets al frame_scroll sin modificar lógica existente
    ventana_bp = frame_scroll

    for linea in lineas:
        datos = linea.strip().split(",")

        if len(datos) >= 15:
            tipo = datos[0].strip(" '")
            sexo = datos[1].strip(" '")
            nombre = datos[2].strip(" '")
            alter = datos[3].strip(" '")
            ruta = datos[4].strip(" '")

            marco = tk.Frame(ventana_bp, bg="#2b2b2b", bd=2, relief="ridge")
            marco.pack(padx=10, pady=10, fill="x")

            try:
                imagen = Image.open(ruta)
                imagen = imagen.resize((100, 100), Image.Resampling.LANCZOS)
                imagen_tk = ImageTk.PhotoImage(imagen)
                etiqueta_img = tk.Label(marco, image=imagen_tk, bg="#2b2b2b")
                etiqueta_img.image = imagen_tk
                etiqueta_img.grid(row=0, column=0, rowspan=4, padx=10)
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

            def eliminar_personaje(al=alter):
                respuesta = messagebox.askyesno("Confirmar", "¿Deseas eliminar a " + al + "?")
                if respuesta:
                    archivo = open("Luchadores.txt", "w", encoding="utf-8")
                    for l in lineas:
                        if al not in l:
                            archivo.write(l)
                    archivo.close()
                    messagebox.showinfo("Listo", "Personaje eliminado")
                    ventana_bp.destroy()
                    borrar_personaje()

            boton = tk.Button(marco, text="Eliminar", bg="red", fg="white", command=lambda al=alter: eliminar_personaje(al))
            boton.grid(row=2, column=1, sticky="w")#cambiar
    
def menupersonajes(): # Oculta la ventana principal sin cerrarla
    ventana.withdraw()
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

    boton_crear = tk.Button(menu_personajes, text="Crear Personaje", font=("Arial", 14), bg="#000000", fg="white", command=lambda: [crear_personaje(), menu_personajes.destroy()])
    boton_crear.grid(row=2, column=0, pady=10, sticky="ew")

    boton_borrar = tk.Button(menu_personajes, text="Borrar Personaje", font=("Arial", 14), bg="#000000", fg="white", command=borrar_personaje)
    boton_borrar.grid(row=3, column=0, pady=10, sticky="ew")

    salir_boton = tk.Button(menu_personajes, text="Volver al menu principal", font=("Arial", 14), bg="#000000", fg="white", command=lambda: [menu_inicio(), menu_personajes.destroy()])
    salir_boton.grid(row=4, column=0, pady=5, sticky="ew")

    menu_personajes.mainloop()

def crear_personaje():
    personaje=tk.Tk()
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

    boton_Heroe = tk.Button(personaje, text="Heroe", font=("Arial", 14), bg="#4C00FF", fg="yellow", command=lambda: heroe())
    boton_Heroe.grid(row=1, column=0, pady=10, sticky="ew")

    boton_Villano = tk.Button(personaje, text="Villano", font=("Arial", 14), bg="#FF0000", fg="black", command=lambda: Villano())
    boton_Villano.grid(row=2, column=0, pady=10, sticky="ew")

    salir_boton = tk.Button(personaje, text="Volver al menu principal", font=("Arial", 14), bg="#FFFFFF", fg="black", command=[menupersonajes, personaje.destroy])
    salir_boton.grid(row=4, column=0, pady=5, sticky="ew")

    personaje.mainloop()

def crear_torneo():
    crea_torneo = tk.Tk()
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
    mensaje.grid(row=6, column=0, pady=10, sticky="ew")

    boton_manual = tk.Button(marco1, text="Manual", font=("Arial", 14), bg="gray", fg="black", command=lambda: manual())
    boton_manual.grid(row=7, column=0, pady=10, sticky="ew")

    boton_vsbot = tk.Button(marco1, text="Persona vs Programa", font=("Arial", 14), bg="gray", fg="black", command=lambda: vsbot())
    boton_vsbot.grid(row=8, column=0, pady=10, sticky="ew")

    boton_auto = tk.Button(marco1, text = "Programa vs Programa", font = ("Arial", 14), bg="gray", fg="black", command=lambda: auto())
    boton_auto.grid(row=9, column=0, pady=10, sticky="ew")

    salir_boton = tk.Button(marco1, text="Volver al menu principal", font=("Arial", 14), bg="#FFFFFF", fg="black", command=[menu_inicio, crea_torneo.destroy])
    salir_boton.grid(row=10, column=0, pady=10, sticky="ew")

    nombre = entrada_nombre.get()
    fecha = entrada_fecha.get()
    lugar = entrada_lugar.get()
    numero_de_luchas = entrada_luchas.get()

    with open("EL GRAN TORNEO/Torneos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{fecha},{lugar},{numero_de_luchas}")
    

def manual():
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
        with open("Luchadores.txt", "r", encoding="utf-8") as archivo:
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
        with open("Luchadores.txt", "r", encoding="utf-8") as archivo:
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
            try:
                ruta = f"personajes/{personaje.lower().strip().replace(' ', '_')}.png"
                img = Image.open(ruta)
                img = img.resize((100, 100), Image.Resampling.LANCZOS)
                img_tk = ImageTk.PhotoImage(img)
                etiqueta = tk.Label(ventana_final, image=img_tk, bg="black")
                etiqueta.image = img_tk
            except:
                etiqueta = tk.Label(ventana_final, text=personaje, bg="black", fg="white", wraplength=100)

            etiqueta.grid(row=3 + i, column=columna, padx=20, pady=10)

    mostrar_bando(bando1, 0)
    mostrar_bando(bando2, 2)

    boton_crear_torneo = tk.Button(ventana_final, text="Crear Torneo", font=("Arial", 14), bg="green", fg="white",
                                    command=lambda: guardartorneo(bando1, bando2))
    boton_crear_torneo.grid(row=8, column=0, columnspan=3, pady=20)

def guardartorneo(bando1, bando2):
    with open("Torneos.txt", "a", encoding="utf-8") as archivo:
        archivo.write("Bando 1: " + ", ".join(bando1) + "\n")
        archivo.write("Bando 2: " + ", ".join(bando2) + "\n")

    messagebox.showinfo("Listo", "Torneo guardado exitosamente")
    menu_inicio(Persona="")  # Regresa al menú principal

def seleccionar_personajes_random():
    seleccionados = []

    try:
        archivo = open("Luchadores.txt", "r", encoding="utf-8")
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
  # Inicia el bucle principal de la ventana

def vsbot():
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
    mensaje.grid(row=0, column=1, sticky="ew", pady=20)

    boton_sele= tk.Button(marco, text="Seleccionar Personajes", font=("Arial", 14), bg="green", fg="white",
                                  command=lambda: [seleccionar_personajes1(), ventana_vsbot.destroy()])
    boton_sele.grid(row=1, column=1, pady=20)

    etiqueta = tk.Label(marco, text=" VS ", bg="#000000", fg="white")
    etiqueta.grid(row=2, column=1, sticky="ew", pady=20)

    boton_q= tk.Button(marco, text="Programa", font=("Arial", 14), bg="green", fg="white",
                                  command=lambda: seleccionar_personajes_random())
    boton_q.grid(row=3, column=1, pady=20)

    bando_programa = seleccionar_personajes_random()
    bando1 = seleccionar_personajes1()
    if bando1==len(bando_programa)==0 or len(bando1)<5:
        messagebox.showwarning("Advertencia", "Debe seleccionar al menos 5 personajes para ambos bandos")
        return
    crear= tk.Button(marco, text="Siguiente", font=("Arial", 14), bg="blue", fg="white", command=lambda: guardartorneo(bando1, bando_programa))
    crear.grid(row=4, column=1, pady=20)
    

    ventana_vsbot.mainloop()  # Mantiene la ventana abierta

def vsbotfinal(equipo1, equipo2):
    pass
    



vsbot()
ventana.mainloop()