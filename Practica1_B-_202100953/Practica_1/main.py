
from tkinter import Spinbox, Tk, Button, Entry, Label, messagebox, ttk, PhotoImage
from tkinter import  StringVar,Scrollbar,Frame

import funciones


class Ventana(Frame):
	def __init__(self, master, *args):
		super().__init__( master,*args)

		self.menu = True
		self.funcion = funciones.funcionesgestion()

	    #Creacion de frames de división
		self.frame_inicio = Frame(self.master, bg='black', width=50, height=45)
		self.frame_inicio.grid_propagate(0)
		self.frame_inicio.grid(column=0, row = 0, sticky='nsew')
		self.frame_menu = Frame(self.master, bg='black', width = 50)
		self.frame_menu.grid_propagate(0)
		self.frame_menu.grid(column=0, row = 1, sticky='nsew')
		self.frame_top = Frame(self.master, bg='black', height = 50)
		self.frame_top.grid(column = 1, row = 0, sticky='nsew')
		self.frame_principal = Frame(self.master, bg='black')
		self.frame_principal.grid(column=1, row=1, sticky='nsew')
		self.master.columnconfigure(1, weight=1)
		self.master.rowconfigure(1, weight=1)
		self.frame_principal.columnconfigure(0, weight=1)
		self.frame_principal.rowconfigure(0, weight=1)

		self.codigo = StringVar()
		self.nombre = StringVar()
		self.prerequisito = StringVar()
		self.opcionalidad = StringVar()
		self.semestre = StringVar()
		self.creditos = StringVar()
		self.estado = StringVar()
		self.ruta = StringVar()
		self.aprobado = StringVar()
		self.cursado = StringVar()
		self.pendiente = StringVar()
		self.creditoN = StringVar()
		self.creditosemestre = StringVar()
		self.spin1= StringVar()
		self.spin2= StringVar()
		# configuracion de las ventanas
		self.elementos()

    #Funcion de Botones
	def pantalla_inicial(self):
		self.limpiar()
		self.paginas.select([self.frame_uno])

	def pantalla_carga(self):
		self.paginas.select([self.frame_dos])
		self.frame_dos.columnconfigure(0, weight=1)
		self.frame_dos.columnconfigure(1, weight=1)

	def pantalla_gestion(self):
		self.limpiar()
		self.paginas.select([self.frame_ocho])
		self.frame_ocho.columnconfigure(0, weight=1)
		self.frame_ocho.columnconfigure(1, weight=1)
		
	def pantalla_datos(self):
		self.listarcurso()
		self.paginas.select([self.frame_tres])
		self.frame_tres.columnconfigure(0, weight=1)
		self.frame_tres.columnconfigure(1, weight=1)
		self.frame_tres.rowconfigure(2, weight=1)
		self.frame_tabla_uno.columnconfigure(0, weight=1)
		self.frame_tabla_uno.rowconfigure(0, weight=1)
	
	def pantalla_mostrar(self):

		self.paginas.select([self.frame_nueve])
		self.frame_nueve.columnconfigure(0, weight=1)
		self.frame_nueve.columnconfigure(1, weight=1)

	def pantalla_agregar(self):
		self.paginas.select([self.frame_cuatro])
		self.frame_cuatro.columnconfigure(0, weight=1)
		self.frame_cuatro.columnconfigure(1, weight=1)

	def pantalla_editar(self):
		self.paginas.select([self.frame_cinco])	
		self.frame_cinco.columnconfigure(0, weight=1)
		self.frame_cinco.columnconfigure(1, weight=1)

	def pantalla_eliminar(self):
		self.paginas.select([self.frame_seis])
		self.frame_seis.columnconfigure(0, weight=1)
		self.frame_seis.columnconfigure(1, weight=1)
		
	def pantalla_conteo(self):
		self.aprobado.set(self.funcion.aprobados())
		self.cursado.set(self.funcion.cursados())
		self.pendiente.set(self.funcion.pendientes())
		self.paginas.select([self.frame_siete])
		self.frame_siete.columnconfigure(0, weight=1)
		self.frame_siete.columnconfigure(1, weight=1)
	
	def salir(self):
		self.master.destroy()
		
    #Funcion de animacion y generales
	def menu_lateral(self):
		if self.menu is True:
			for i in range(50,235,15):				
				self.frame_menu.config(width= i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_cerrar.grid_forget()
				if clik_inicio is None:		
					self.bt_inicio.grid(column=0, row=0, padx =10, pady=10)
					self.bt_inicio.grid_propagate(0)
					self.bt_inicio.config(width=i)
					self.pantalla_inicial()
			self.menu = False
		else:
			for i in range(235,50,-15):
				self.frame_menu.config(width=  i)
				self.frame_inicio.config(width= i)
				self.frame_menu.update()
				clik_inicio = self.bt_inicio.grid_forget()
				if clik_inicio is   None:
					self.frame_menu.grid_propagate(0)		
					self.bt_cerrar.grid(column=0, row=0, padx =10, pady=10)
					self.bt_cerrar.grid_propagate(0)
					self.bt_cerrar.config(width=i)
					self.pantalla_inicial()
			self.menu = True

	#Funcion para limpriar  cuadros de entrada
	def limpiar(self):
		self.codigo.set("")
		self.nombre.set("")
		self.prerequisito.set("")
		self.opcionalidad.set("")
		self.semestre.set("")
		self.creditos.set("")
		self.estado.set("")
		self.ruta.set("")
		self.creditoN.set("")
		self.creditosemestre.set("")
	
 # leer archivo
	def leerarchivo(self):
		if self.ruta.get()=="" or self.ruta.get()==" " :
			messagebox.showerror(message= "No ha ingresado ninguna ruta",title="carga de archivo")
		else:
			direccion = self.ruta.get()
			self.funcion.leer(direccion)
			self.pantalla_inicial()
			self.limpiar()
			
	#listar todos los cursos
	def listarcurso(self):
		datos = self.funcion.listalinea
		self.tabla_uno.delete(*self.tabla_uno.get_children())
		i = -1
		for dato in datos:
			i= i+1
			self.tabla_uno.insert('',i, text = datos[i][0:1], values=datos[i][1:7])		
	# mostrar cursos
	def mostrarcurso(self):
		codigo = self.codigo.get()
		self.datos=self.funcion.mostrar(codigo)
		print(self.datos)
		if self.datos==None:
			self.limpiar()
		else:
			self.nombre.set(self.datos[1])
			self.prerequisito.set(self.datos[2])
			self.opcionalidad.set(self.datos[3])
			self.semestre.set(self.datos[4])
			self.creditos.set(self.datos[5])
			self.estado.set(self.datos[6])
	# agregar nuevo curso
	def agregarcurso(self):
		try:
			int(self.opcionalidad.get())
			int(self.semestre.get())
			int(self.creditos.get())
			int(self.estado.get())
			comprobacion=True
		except ValueError:
			comprobacion = False

		if self.codigo.get()=="" or self.nombre.get()=="" or self.opcionalidad.get()==""or self.semestre.get()==""or self.creditos.get()=="" or self.estado.get()=="":
			messagebox.showerror(message= "No ha llenado todos los campos obligatorios",title="Agregar curso")
		elif comprobacion==False:
			messagebox.showerror(message= "Ha ingresado texto en los campos donde se esperaba un valor numerico",title="Agregar curso")
		elif comprobacion==True and (int(self.semestre.get())<=0 or int(self.semestre.get())>10):
			messagebox.showerror(message= "Ha ingresado una cantidad invalida en el campo Semestre\nEl valor debe estar entre 1 y 10 ",title="Agregar curso")	
		else:
			if comprobacion==True and (int(self.opcionalidad.get())== 0 or int(self.opcionalidad.get())==1):
				if int(self.estado.get())== 0 or int(self.estado.get())==1 or int(self.estado.get())==-1:
					codigo =self.codigo.get()
					datolist=[str(codigo),str(self.nombre.get()),str(self.prerequisito.get()),str(self.opcionalidad.get()),str(self.semestre.get()),str(self.creditos.get()),str(self.estado.get())]
					self.funcion.agregar(codigo,datolist)
					self.continuo=1
					self.limpiar()
				else:
					messagebox.showerror(message= "Ha ingresado una cantidad invalida en el campo Estado\nEl valor debe de estar entre -1 y 1",title="Agregar curso")
			else:
				messagebox.showerror(message= "Ha ingresado una cantidad invalida en el campo Opcionalidad\nEl valor debe ser 0 ó 1",title="Agregar curso")	
	
	# editar curso
	def editarcurso(self):
		try:
			int(self.opcionalidad.get())
			int(self.semestre.get())
			int(self.creditos.get())
			int(self.estado.get())
			comprobacion=True
		except ValueError:
			comprobacion = False

		if self.codigo.get()=="":
			messagebox.showerror(message= "No se ha buscado ningur curso a editar",title="Editar curso")
		elif self.nombre.get()=="" or self.opcionalidad.get()==""or self.semestre.get()==""or self.creditos.get()=="" or self.estado.get()=="":
			messagebox.showerror(message= "No ha llenado todos los campos obligatorios",title="Editar curso")
		elif comprobacion==False:
			messagebox.showerror(message= "Ha ingresado texto en los campos donde se esperaba un valor numerico",title="Editar curso")
		elif comprobacion==True and (int(self.semestre.get())<=0 or int(self.semestre.get())>10):
			messagebox.showerror(message= "Ha ingresado una cantidad invalida en el campo Semestre\nEl valor debe estar entre 1 y 10 ",title="Editar curso")	
		else:
			if comprobacion==True and (int(self.opcionalidad.get())== 0 or int(self.opcionalidad.get())==1):
				if int(self.estado.get())== 0 or int(self.estado.get())==1 or int(self.estado.get())==-1:
					codigo=self.codigo.get()
					datolist=[str(codigo),str(self.nombre.get()),str(self.prerequisito.get()),str(self.opcionalidad.get()),
						str(self.semestre.get()),str(self.creditos.get()),str(self.estado.get())]
					self.funcion.editar(codigo,datolist)
					self.limpiar()
				else:
					messagebox.showerror(message= "Ha ingresado una cantidad invalida en el campo Estado\nEl valor debe de estar entre -1 y 1",title="Editar curso")
			else:
				messagebox.showerror(message= "Ha ingresado una cantidad invalida en el campo Opcionalidad\nEl valor debe ser 0 ó 1 ",title="Editar curso")
			
	#eliminar curso
	def eliminarcurso(self):
		if self.nombre.get()!="":
			respuesta=messagebox.askyesno(title="Eliminar curso", message="¿Esta seguro de eliminar este curso?")
			if not respuesta:
				messagebox.showinfo(message= "El curso no se borrara\nSe limpiaran los campos para una nueva busqueda",title="Eliminar curso")
				self.limpiar()
			else:
				codigo=self.codigo.get()
				self.funcion.eliminar(codigo)
				self.limpiar()
	# Funciones para el conteo de creditos --------------------
	def creditoshastaNsemestre(self):
		if int(self.spin1.get())>0:
			dato=self.funcion.hastasemestre(int(self.spin1.get()))
			if dato==-1:
				self.limpiar()
			else:
				self.creditoN.set(dato)
		else:
			messagebox.showerror(message= "Se debe de selleccionar un valor entre 1 y 10 en el campo semestre",title="Conteo de creditos")
	
	def creditosensemestre(self):
		if int(self.spin2.get())>0:
			self.sumascreditos=self.funcion.desemestre(int(self.spin2.get()))
			if self.sumascreditos[0]==-1:
				self.limpiar()
			else:
				self.creditosemestre.set(self.sumascreditos[0])
		else:
			messagebox.showerror(message= "Se debe de seleccionar un valor entre 1 y 10 en el campo semestre",title="Conteo de creditos")
					
	def detallecreditos(self):
		if self.sumascreditos[0]==-1:
				print("no hay dato")
		else:
			messagebox.showinfo(message= f"Los detalles de la sumatoria de creditos en el semestre son:\nCreditos aprobados: {self.sumascreditos[1]}\nCreditos cursados: {self.sumascreditos[2]}\nCreditos pendientes obligatorios: {self.sumascreditos[3]}\nCreditos pendientes opcionales: {self.sumascreditos[4]}",title="Conteo de creditos")

	
  #Creacion de los estilos y formatos de las ventanas
	def elementos(self):

		# definiendo imagenes
		self.imagen_inicio = PhotoImage(file ='inicio.png')
		self.imagen_menu = PhotoImage(file ='menu.png')
		self.imagen_conteo = PhotoImage(file ='abaco.png')
		self.imagen_salir = PhotoImage(file ='salida.png')
		self.imagen_contar = PhotoImage(file ='calculadora.png')
		self.imagen_subir = PhotoImage(file ='subir.png')
		self.gestion = PhotoImage(file ='gestion.png')
		self.logousac =PhotoImage(file='usaclogo.png')
		self.imagen_uno = PhotoImage(file ='subir_1.png')
		self.imagen_dos= PhotoImage(file ='gestion_1.png')
		self.imagen_tres=PhotoImage(file="mostrar.png")
		self.imagen_cuatro = PhotoImage(file="anadir-punto.png")
		self.imagen_cinco = PhotoImage(file="editar-texto.png")
		self.imagen_seis = PhotoImage(file="compartimiento.png")

        # boton de inicio interactivo	
		self.bt_inicio = Button(self.frame_inicio, image= self.imagen_inicio, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
		self.bt_inicio.grid(column=0, row=0, padx=5, pady=10)
		self.bt_cerrar = Button(self.frame_inicio, image= self.imagen_menu, bg='black',activebackground='black', bd=0, command = self.menu_lateral)
		self.bt_cerrar.grid(column=0, row=0, padx=5, pady=10)	

		# Bonotes y etiquetas del menu desplegable 
		Button(self.frame_menu, image= self.imagen_subir, bg='black', activebackground='black', bd=0, command = self.pantalla_carga).grid(column=0, row=1, pady=20,padx=10)
		Button(self.frame_menu, image= self.gestion, bg='black',activebackground='black', bd=0, command =self.pantalla_gestion).grid(column=0, row=2, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_contar, bg= 'black',activebackground='black', bd=0, command = self.pantalla_conteo).grid(column=0, row=3, pady=20,padx=10)
		Button(self.frame_menu, image= self.imagen_salir, bg= 'black',activebackground='black', bd=0, command = self.salir).grid(column=0, row=4, pady=20,padx=10)
		
		Label(self.frame_menu, text= 'Cargar archivo', bg= 'black', fg= 'DeepSkyBlue3', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=1, pady=20, padx=2)
		Label(self.frame_menu, text= 'Gestionar cursos', bg= 'black', fg= 'DeepSkyBlue3', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=2, pady=20, padx=2)
		Label(self.frame_menu, text= 'Conteo de créditos', bg= 'black', fg= 'DeepSkyBlue3', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=3, pady=20, padx=2)
		Label(self.frame_menu, text= 'Salir', bg= 'black', fg= 'DeepSkyBlue3', font= ('Lucida Sans', 12, 'bold')).grid(column=1, row=4, pady=20, padx=2)

        # Definir estilo de paginas 
		estilo_paginas = ttk.Style()
		estilo_paginas.configure("TNotebook", background='black', foreground='black', padding=0, borderwidth=0)
		estilo_paginas.theme_use('default')
		estilo_paginas.configure("TNotebook", background='black', borderwidth=0)
		estilo_paginas.configure("TNotebook.Tab", background="black", borderwidth=0)
		estilo_paginas.map("TNotebook", background=[("selected", 'black')])
		estilo_paginas.map("TNotebook.Tab", background=[("selected", 'black')], foreground=[("selected", 'black')]);

		#creacion de paginas
		self.paginas = ttk.Notebook(self.frame_principal , style= 'TNotebook')
		self.paginas.grid(column=0,row=0, sticky='nsew')
		self.frame_uno = Frame(self.paginas, bg='DeepSkyBlue3')
		self.frame_dos = Frame(self.paginas, bg='white')
		self.frame_tres = Frame(self.paginas, bg='white')
		self.frame_cuatro = Frame(self.paginas, bg='white')
		self.frame_cinco = Frame(self.paginas, bg='white')
		self.frame_seis = Frame(self.paginas, bg='white')
		self.frame_ocho =Frame(self.paginas, bg='white')
		self.frame_siete = Frame(self.paginas, bg='white')
		self.frame_nueve = Frame(self.paginas, bg='white')
		self.paginas.add(self.frame_uno)
		self.paginas.add(self.frame_dos)
		self.paginas.add(self.frame_tres)
		self.paginas.add(self.frame_cuatro)
		self.paginas.add(self.frame_cinco)
		self.paginas.add(self.frame_seis)
		self.paginas.add(self.frame_siete)
		self.paginas.add(self.frame_ocho)
		self.paginas.add(self.frame_nueve)


		#  diseño de paginas

		# frame de titulo
		self.titulo = Label(self.frame_top,text= 'APLICACION PARA LA GESTION DE CURSOS', bg='black', fg= 'DeepSkyBlue3', font= ('Imprint MT Shadow', 15, 'bold'))
		self.titulo.pack(expand=1)

		# ventana principal
		Label(self.frame_uno, text= 'Lenguajes Formales y de Programación', bg='DeepSkyBlue3', fg= 'white', font= ('Freehand521 BT', 20, 'bold')).pack(expand=1)
		Label(self.frame_uno, text= 'Seccion: B-', bg='DeepSkyBlue3', fg= 'white', font= ('Freehand521 BT', 20, 'bold')).pack(expand=1)
		Label(self.frame_uno, text= 'Damaris Julizza Muralles Véliz', bg='DeepSkyBlue3', fg= 'white', font= ('Freehand521 BT', 20, 'bold')).pack(expand=1)
		Label(self.frame_uno, text= '202100953', bg='DeepSkyBlue3', fg= 'white', font= ('Freehand521 BT', 20, 'bold')).pack(expand=1)
		Label(self.frame_uno ,image= self.logousac, bg='DeepSkyBlue3').pack(expand=1)

		# ventana de carga
		Label(self.frame_dos, text = 'Seleccionar archivo',fg='DeepSkyBlue3', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=2, column=1,row=0, pady=5)
		Label(self.frame_dos, text = 'Ruta:',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3)
		Entry(self.frame_dos, textvariable=self.ruta , font=('Comic Sans MS', 12),highlightbackground = "gray64", highlightcolor= "deep sky blue", highlightthickness=2).grid(column=1,row=3,ipadx=80)
		Button(self.frame_dos,command = self.leerarchivo, text='Seleccionar', font=('Arial',10,'bold'), fg="white", bg='DeepSkyBlue4').grid(column=1,row=10, pady=10, padx=4, ipadx=10)
		Label(self.frame_dos, image= self.imagen_uno, bg= 'white').grid(column= 3, rowspan= 5, row = 1, padx= 50)
		
		# Ventana de gestion 
		Label(self.frame_ocho, text = 'Gestionar Cursos',fg='DeepSkyBlue3', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=2, column=1,row=0, pady=5)
		Button(self.frame_ocho, text='Listar Cursos', font=('Arial',10,'bold'), bg='DeepSkyBlue4', fg="white",command = self.pantalla_datos).grid(column=1,row=3, pady=10, padx=4, ipadx=10)
		Button(self.frame_ocho, text='Mostrar Curso', font=('Arial',10,'bold'), bg='DeepSkyBlue4', fg="white",command = self.pantalla_mostrar).grid(column=1,row=4, pady=10, padx=4, ipadx=10)
		Button(self.frame_ocho, text='Agregar Curso', font=('Arial',10,'bold'), bg='DeepSkyBlue4', fg="white",command = self.pantalla_agregar).grid(column=1,row=5, pady=10, padx=4, ipadx=10)
		Button(self.frame_ocho, text='Editar Curso', font=('Arial',10,'bold'), bg='DeepSkyBlue4', fg="white",command = self.pantalla_editar).grid(column=1,row=6, pady=10, padx=4, ipadx=10)
		Button(self.frame_ocho, text='Eliminar Curso', font=('Arial',10,'bold'), bg='DeepSkyBlue4', fg="white",command = self.pantalla_eliminar).grid(column=1,row=7, pady=10, padx=4, ipadx=10)
		Label(self.frame_ocho, image= self.imagen_dos, bg= 'white').grid(column= 3, rowspan= 5, row = 1, padx= 50)
		Button(self.frame_ocho, text="Regresar", font=('Arial',10,'bold'), fg='white', bg='DeepSkyBlue4', command =self.pantalla_inicial).grid(column=3,row=6, pady=10, padx=4)
		# Ventana lista de archivos
		Label(self.frame_tres, text= 'Lista de cursos', bg='white', fg= 'DeepSkyBlue3', font= ('Comic Sans MS', 16, 'bold')).grid(column =0, row=0)
		Button(self.frame_tres, text='Regresar',fg='white' ,font = ('Arial', 11,'bold'),  bg = 'DeepSkyBlue4', bd = 2, borderwidth=2, command =self.pantalla_gestion).grid(column=2, row=0, pady=10, padx=10)
		
		# Estilo de las tablas (Treeview)
		estilo_tabla = ttk.Style()
		estilo_tabla.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white') 
		estilo_tabla.map('Treeview',background=[('selected', 'deep sky blue')], foreground=[('selected','black')] )		
		estilo_tabla.configure('Heading',background = 'white', foreground='navy',padding=3, font= ('Arial', 10, 'bold'))
		estilo_tabla.configure('Item',foreground = 'white', focuscolor ='deep sky blue')
		estilo_tabla.configure('TScrollbar', arrowcolor = 'deep sky blue',bordercolor  ='black', troughcolor= 'deep sky blue',background ='white')
		
		#Tabla uno 
		self.frame_tabla_uno = Frame(self.frame_tres, bg= 'gray90')
		self.frame_tabla_uno.grid(columnspan=3, row=2, sticky='nsew')		
		self.tabla_uno = ttk.Treeview(self.frame_tabla_uno) 
		self.tabla_uno.grid(column=0, row=0, sticky='nsew')
		ladox = ttk.Scrollbar(self.frame_tabla_uno, orient = 'horizontal', command= self.tabla_uno.xview)
		ladox.grid(column=0, row = 1, sticky='ew') 
		ladoy = ttk.Scrollbar(self.frame_tabla_uno, orient ='vertical', command = self.tabla_uno.yview)
		ladoy.grid(column = 1, row = 0, sticky='ns')

		self.tabla_uno.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
		self.tabla_uno['columns'] = ( 'Nombre','Prerequisito','Opcionalidad','Semestre','Creditos','Estado')
		self.tabla_uno.column('#0', minwidth=100, width=120, anchor='center')
		self.tabla_uno.column('Nombre', minwidth=100, width=120, anchor='center' )
		self.tabla_uno.column('Prerequisito', minwidth=100, width=120 , anchor='center')
		self.tabla_uno.column('Opcionalidad', minwidth=100, width=105, anchor='center')
		self.tabla_uno.column('Semestre', minwidth=100, width=105, anchor='center')
		self.tabla_uno.column('Creditos', minwidth=100, width=105, anchor='center')
		self.tabla_uno.column('Estado', minwidth=100, width=105, anchor='center')

		self.tabla_uno.heading('#0', text='Codigo', anchor ='center')
		self.tabla_uno.heading('Nombre', text='Nombre', anchor ='center')
		self.tabla_uno.heading('Prerequisito', text='Prerequisito', anchor ='center')
		self.tabla_uno.heading('Opcionalidad', text='Opcionalidad', anchor ='center')
		self.tabla_uno.heading('Semestre', text='Semestre', anchor ='center')
		self.tabla_uno.heading('Creditos', text='Creditos', anchor ='center')
		self.tabla_uno.heading('Estado', text='Estado', anchor ='center')
		self.tabla_uno.bind("<<TreeviewSelect>>") 

		# Ventana de mostrar curso
		Label(self.frame_nueve, text = 'Mostrar Curso',fg='DeepSkyBlue3', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
		Label(self.frame_nueve, text = 'Codigo',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15, padx=5)
		Label(self.frame_nueve, text = 'Nombre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
		Label(self.frame_nueve, text = 'Prerequisito',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_nueve, text = 'Opcionalidad', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_nueve, text = 'Semestre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)  
		Label(self.frame_nueve, text = 'Creditos',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15) 
		Label(self.frame_nueve, text = 'Estado',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15) 

		Entry(self.frame_nueve, textvariable=self.codigo , font=('Comic Sans MS', 12),highlightbackground = "gray64",highlightcolor= "deep sky blue", highlightthickness=2).grid(column=1,row=1)
		Button(self.frame_nueve, text='Buscar', font=('Arial',10,'bold'),fg='white', bg='DeepSkyBlue4',command =self.mostrarcurso).grid(column=3,row=5, pady=10, padx=4)
		Label(self.frame_nueve, textvariable = self.nombre,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=2, pady=15)
		Label(self.frame_nueve, textvariable = self.prerequisito,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=3, pady=15)
		Label(self.frame_nueve, textvariable = self.opcionalidad, fg='navy',bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=4, pady=15)
		Label(self.frame_nueve, textvariable = self.semestre,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=5, pady=15)  
		Label(self.frame_nueve, textvariable = self.creditos,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=6, pady=15) 
		Label(self.frame_nueve, textvariable = self.estado,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=7, pady=15) 
		Button(self.frame_nueve, text="Regresar", font=('Arial',10,'bold'), fg='white', bg='DeepSkyBlue4', command =self.pantalla_gestion).grid(column=3,row=6, pady=10, padx=4)
		Label(self.frame_nueve, image= self.imagen_tres, bg= 'white').grid(column= 3, rowspan= 5, row = 0, padx= 50)


		
		# Ventana de registro de curso
		Label(self.frame_cuatro, text = 'Agregar Nuevos Cursos',fg='DeepSkyBlue3', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
		Label(self.frame_cuatro, text = '* Codigo',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15, padx=5)
		Label(self.frame_cuatro, text = '* Nombre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
		Label(self.frame_cuatro, text = 'Prerequisito',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_cuatro, text = '* Opcionalidad', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_cuatro, text = '* Semestre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)  
		Label(self.frame_cuatro, text = '* Creditos',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15) 
		Label(self.frame_cuatro, text = '* Estado',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15) 

		Entry(self.frame_cuatro, textvariable=self.codigo , font=('Comic Sans MS', 12),highlightbackground="gray64",highlightcolor = "deep sky blue",  highlightthickness=2).grid(column=1,row=1)
		Entry(self.frame_cuatro, textvariable=self.nombre , font=('Comic Sans MS', 12),highlightbackground="gray64",highlightcolor = "deep sky blue",  highlightthickness=2).grid(column=1,row=2)
		Entry(self.frame_cuatro, textvariable=self.prerequisito , font=('Comic Sans MS', 12),highlightbackground="gray64",highlightcolor = "deep sky blue", highlightthickness=2).grid(column=1,row=3)
		Entry(self.frame_cuatro, textvariable=self.opcionalidad , font=('Comic Sans MS', 12),highlightbackground="gray64",highlightcolor = "deep sky blue",  highlightthickness=2).grid(column=1,row=4)
		Entry(self.frame_cuatro, textvariable=self.semestre , font=('Comic Sans MS', 12),highlightbackground="gray64",highlightcolor = "deep sky blue",  highlightthickness=2).grid(column=1,row=5)
		Entry(self.frame_cuatro, textvariable=self.creditos , font=('Comic Sans MS', 12),highlightbackground="gray64",highlightcolor = "deep sky blue",  highlightthickness=2).grid(column=1,row=6)
		Entry(self.frame_cuatro, textvariable=self.estado , font=('Comic Sans MS', 12),highlightbackground="gray64",highlightcolor = "deep sky blue",  highlightthickness=2).grid(column=1,row=7)

		Button(self.frame_cuatro, text='Registrar',fg='white', font=('Arial',10,'bold'), bg='DeepSkyBlue4',command =self.agregarcurso).grid(column=3,row=6, pady=10, padx=4)
		Button(self.frame_cuatro, text='Regresar',fg='white', font=('Arial',10,'bold'), bg='DeepSkyBlue4', command =self.pantalla_gestion).grid(column=3,row=7, pady=10, padx=4)
		Label(self.frame_cuatro, image= self.imagen_cuatro, bg= 'white').grid(column= 3, rowspan= 5, row = 0, padx= 50)
		
		#ventana de edicion de datos
		Label(self.frame_cinco, text = 'Editar curso',fg='DeepSkyBlue3', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=4, row=0)		
		Label(self.frame_cinco, text = 'Ingrese el codigo del curso a editar',fg='black', bg ='white', font=('Rockwell',12)).grid(columnspan=2,row=1)
		Entry(self.frame_cinco, textvariable= self.codigo , font=('Comic Sans MS', 12), highlightbackground = "gray64",highlightcolor = "deep sky blue", width=12, highlightthickness=2).grid(column=2,row=1, padx=5)
		Button(self.frame_cinco,  text='Buscar', font=('Arial',12,'bold'), bg='deep sky blue',command=self.mostrarcurso).grid(column=3,row=1, pady=5, padx=15)

		Label(self.frame_cinco, text = '* Nombre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15, padx=10)
		Label(self.frame_cinco, text = 'Prerequisito',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_cinco, text = '* Opcionalidad',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_cinco, text = '* Semestre', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)
		Label(self.frame_cinco, text = '* Creditos',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15)  
		Label(self.frame_cinco, text = '* Estado',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15) 
		Entry(self.frame_cinco, textvariable=self.nombre , font=('Comic Sans MS', 12), highlightbackground = "gray64", highlightcolor= "deep sky blue", highlightthickness=2).grid(column=1,row=2)
		Entry(self.frame_cinco, textvariable=self.prerequisito , font=('Comic Sans MS', 12), highlightbackground = "gray64", highlightcolor= "deep sky blue", highlightthickness=2).grid(column=1,row=3)
		Entry(self.frame_cinco, textvariable=self.opcionalidad , font=('Comic Sans MS', 12), highlightbackground = "gray64", highlightcolor= "deep sky blue", highlightthickness=2).grid(column=1,row=4)
		Entry(self.frame_cinco, textvariable=self.semestre , font=('Comic Sans MS', 12), highlightbackground = "gray64", highlightcolor= "deep sky blue", highlightthickness=2).grid(column=1,row=5)
		Entry(self.frame_cinco, textvariable=self.creditos, font=('Comic Sans MS', 12), highlightbackground = "gray64", highlightcolor= "deep sky blue", highlightthickness=2).grid(column=1,row=6)
		Entry(self.frame_cinco, textvariable=self.estado, font=('Comic Sans MS', 12), highlightbackground = "gray64", highlightcolor= "deep sky blue", highlightthickness=2).grid(column=1,row=7)

		Button(self.frame_cinco, text='Actualizar',fg='white', font=('Arial',12,'bold'), bg='DeepSkyBlue4', command =self.editarcurso).grid(column=2,row=7, pady=2)
		Button(self.frame_cinco,  text='Regresar',fg='white', font=('Arial',12,'bold'), bg='DeepSkyBlue4', command =self.pantalla_gestion).grid(column=2,row=8, pady=5, padx=15)
		Label(self.frame_cinco, image= self.imagen_cinco, bg='white').grid(column= 2,columnspan= 2, rowspan= 5, row = 2, padx=2)

		# ventana eliminar
		Label(self.frame_seis, text = 'Eliminar Curso',fg='DeepSkyBlue3', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan= 4,  row=0,sticky='nsew',padx=2)
		Label(self.frame_seis, text = 'Codigo',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15, padx=5)
		Label(self.frame_seis, text = 'Nombre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
		Label(self.frame_seis, text = 'Prerequisito',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_seis, text = 'Opcionalidad', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_seis, text = 'Semestre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)  
		Label(self.frame_seis, text = 'Creditos',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15) 
		Label(self.frame_seis, text = 'Estado',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15) 
		Entry(self.frame_seis, textvariable=self.codigo , font=('Comic Sans MS', 12),highlightbackground = "gray64",highlightcolor= "deep sky blue", highlightthickness=2).grid(column=1,row=1)
		Button(self.frame_seis, text='Buscar', font=('Arial',10,'bold'),fg='white', bg='DeepSkyBlue4',command =self.mostrarcurso).grid(column=2,row=1, pady=10, padx=4)
		Label(self.frame_seis, textvariable = self.nombre,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=2, pady=15)
		Label(self.frame_seis, textvariable = self.prerequisito,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=3, pady=15)
		Label(self.frame_seis, textvariable = self.opcionalidad, fg='navy',bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=4, pady=15)
		Label(self.frame_seis, textvariable = self.semestre,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=5, pady=15)  
		Label(self.frame_seis, textvariable = self.creditos,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=6, pady=15) 
		Label(self.frame_seis, textvariable = self.estado,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=7, pady=15) 
		Button(self.frame_seis, text='Eliminar', font=('Arial',10,'bold'),fg='white', bg='red', command =self.eliminarcurso).grid(column = 3, row=5, pady=10,padx=4)
		Button(self.frame_seis, text="Regresar", font=('Arial',10,'bold'),fg='white', bg='DeepSkyBlue4', command =self.pantalla_gestion).grid(column=3,row=6, pady=10, padx=4)
		Label(self.frame_seis, image= self.imagen_seis, bg= 'white').grid(column= 3, rowspan= 5, row = 0, padx= 50)

		# ventana de conteo 
		Label(self.frame_siete, text = 'Conteo de Creditos:',fg='DeepSkyBlue3', bg ='white', font=('Kaufmann BT',24,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
		Label(self.frame_siete, text = 'Creditos Aprobados:',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15, padx=5)
		Label(self.frame_siete, text = 'Creditos Cursando:',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
		Label(self.frame_siete, text = 'Creditos Pendientes:',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
		Label(self.frame_siete, text = 'Creditos Obligatorios hasta Semestre N:', fg='navy',bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
		Label(self.frame_siete, text = '* Semestre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)  
		Label(self.frame_siete, text = 'Creditos del semestre:',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=6, pady=15) 
		Label(self.frame_siete, text = '* semestre',fg='navy', bg ='white', font=('Rockwell',13,'bold')).grid(column=0,row=7, pady=15) 
		
		Label(self.frame_siete, textvariable = self.aprobado,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=1, pady=15)
		Label(self.frame_siete, textvariable = self.cursado,fg='navy', bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=2, pady=15)
		Label(self.frame_siete, textvariable = self.pendiente, fg='navy',bg ='white', font=('Comic Sans MS', 12)).grid(column=1,row=3, pady=15)
		Entry(self.frame_siete, textvariable=self.creditoN ,state="readonly", font=('Comic Sans MS', 12),highlightbackground="gray64",highlightcolor = "deep sky blue",  highlightthickness=2, width=15).grid(column=1,row=4)
		Spinbox(self.frame_siete,from_=0, to=10, increment=1,width=5,textvariable=self.spin1).grid(column=1,row=5, pady=5)
		Button(self.frame_siete, text='Contar',fg='white', font=('Arial',10,'bold'),bg='deep sky blue',command =self.creditoshastaNsemestre).grid(column=2,row=5, pady=10, padx=4)
		Entry(self.frame_siete, textvariable=self.creditosemestre ,state="readonly", font=('Comic Sans MS', 12),highlightbackground="gray64",highlightcolor = "deep sky blue",  highlightthickness=2, width=15).grid(column=1,row=6)
		Spinbox(self.frame_siete,from_=0, to=10, increment=1,width=5,textvariable=self.spin2).grid(column=1,row=7, pady=5)
		Button(self.frame_siete, text='Contar',fg='white', font=('Arial',10,'bold'), bg='deep sky blue',command =self.creditosensemestre).grid(column=2,row=7, pady=10, padx=4)
		Button(self.frame_siete, text='Detalle',fg='white', font=('Arial',10,'bold'), bg='deep sky blue',command =self.detallecreditos).grid(column=2,row=6, pady=10, padx=4)
		Button(self.frame_siete, text='Regresar',fg='white', font=('Arial',10,'bold'), bg='DeepSkyBlue4', command =self.pantalla_inicial).grid(column=3,row=6, pady=10, padx=4)
		Label(self.frame_siete, image= self.imagen_conteo, bg= 'white').grid(column= 3, rowspan= 5, row = 0, padx= 50)

	
if __name__ == "__main__":
	ventana = Tk()
	ventana.title('Practica 1')
	ventana.minsize(height= 475, width=795)
	ventana.geometry('1000x500+180+80')
	ventana.iconbitmap("logov.ico")
	app = Ventana(ventana)
	app.mainloop()