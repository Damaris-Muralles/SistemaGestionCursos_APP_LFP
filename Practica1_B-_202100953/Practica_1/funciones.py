
import os
import pathlib
from tkinter import messagebox


class funcionesgestion():
    def __init__(self):
        self.listalinea =[]
        self.continuo=0
        
    def leer(self, direccion):
        print(direccion)
        extension= pathlib.Path(direccion)
        
        if str(extension.suffix)==".lfp" and os.path.isfile(direccion):
            if self.continuo ==1:
                respuesta=messagebox.askyesno(title="Cargar archivos", message="Ya hay datos cargados\n¿Desea borrar los datos existentes y cargar nuevos?")
                if not respuesta:
                    print("no")	
                else:
                    self.listalinea.clear()
            self.continuo=1
            archivo = open(direccion,"r", encoding= "utf-8")
            mensaje= archivo.read()
            print("contenido del archivo")
            print(mensaje)
            archivo.close()
            self.enlistar(mensaje)
            messagebox.showinfo(message=str(extension.name)+ "Se ha cargado correctamente ",title="carga de archivo")
        else:
            messagebox.showerror(message="Ha ocurrido un error, porfavor revisar que:\n El archivo existe\n La dirección es correcta\n Se colocó la extensión del archivo, ejemplo: titulo.lfp ",title="carga de archivo")
      
    def enlistar(self,mensaje):
        lista= mensaje.split("\n")
        for i in range(len(lista)):
            curso=lista[i].split(",")
            repeticion=-1
            for j in range(len(self.listalinea)):
                    if self.listalinea[j][0]==curso[0]:
                        repeticion=repeticion+(j+1)
                    else:
                        repeticion=repeticion    
            if not self.listalinea:
                self.listalinea.append(curso)
            elif repeticion==-1:
                self.listalinea.append(curso)
            else:
                self.listalinea[repeticion]=curso
            repeticion=-1
    
    def mostrar(self,codigo):
        for i in range(len(self.listalinea)):
            if self.listalinea[i][0]==codigo:
                return self.listalinea[i]   
        messagebox.showerror(message="No se ha encontrado el curso ",title="Busqueda de curso")
    
            
    def agregar(self,codigo,datolist):
        repeticion=-1
        for j in range(len(self.listalinea)):
                if self.listalinea[j][0]==codigo:
                    repeticion=repeticion+(j+1)
                else:
                    repeticion=repeticion
                
        if not self.listalinea:
            self.listalinea.append(datolist)
            messagebox.showinfo(message="Se agrego correctamente",title="Agregar curso")
        elif repeticion==-1:
            self.listalinea.append(datolist)
            messagebox.showinfo(message="Se agrego correctamente",title="Agregar curso")
        else:
            messagebox.showinfo(message="Este curso ya se encuentra registrado\nSe sobreescribira la información asociada a este",title="Agregar curso")
            self.listalinea[repeticion]=datolist
        repeticion=-1

    def editar(self,codigo,datolist):
        repeticion=-1
        for j in range(len(self.listalinea)):
                if self.listalinea[j][0]==codigo:
                    repeticion=repeticion+(j+1)
                else:
                    repeticion=repeticion
      
        if repeticion!=-1:
            self.listalinea[repeticion]=datolist
            messagebox.showinfo(message="Se edito correctamente",title="Edicion de curso")  
        repeticion=-1

    def eliminar(self,codigo):
        for i in range(len(self.listalinea)):
            if self.listalinea[i][0]==codigo:
                self.posicion=i
        self.listalinea.pop(self.posicion)
        messagebox.showinfo(message="Se elimino correctamente",title="Eliminar de curso")

    def aprobados(self):
        suma=0
        for i in range(len(self.listalinea)):
            if int(self.listalinea[i][6])==0:
                suma=suma+ int(self.listalinea[i][5])
        return suma
    def cursados(self):
        suma=0
        for i in range(len(self.listalinea)):
            if int(self.listalinea[i][6])==1:
                suma=suma+ int(self.listalinea[i][5])
        return suma    
    def pendientes(self):
        suma=0
        for i in range(len(self.listalinea)):
            if int(self.listalinea[i][6])==-1 and int(self.listalinea[i][3])==1:
                suma=suma+ int(self.listalinea[i][5])
        return suma
    def hastasemestre(self,num):
        suma=0
        mayor=0
        for i in range(len(self.listalinea)):
            if int(self.listalinea[i][4])>=mayor:
                mayor=int(self.listalinea[i][4])
        if mayor>=num:
            for j in range(num):
                for i in range(len(self.listalinea)):
                    if int(self.listalinea[i][4])==(j+1) and int(self.listalinea[i][3])==1:
                        suma=suma+ int(self.listalinea[i][5])
            return suma
        else:
            messagebox.showerror(message= f"No hay semestre mayor a {mayor}",title="Conteo de creditos")
            return -1
        
    def desemestre(self,num1):
        suma=0
        apro=0
        cursad=0
        pendobli=0
        pendopci=0
        mayor=0
        for i in range(len(self.listalinea)):
            if int(self.listalinea[i][4])>=mayor:
                mayor=int(self.listalinea[i][4])
        if mayor>=num1:
            for i in range(len(self.listalinea)):
                if int(self.listalinea[i][4])==num1:
                    suma=suma+ int(self.listalinea[i][5])
                    if  int(self.listalinea[i][6])==0:
                        apro=apro+ int(self.listalinea[i][5])
                    if int(self.listalinea[i][6])==1:
                        cursad=cursad+ int(self.listalinea[i][5])
                    if int(self.listalinea[i][6])==-1 and int(self.listalinea[i][3])==1:
                        pendobli=pendobli+ int(self.listalinea[i][5])
                    if int(self.listalinea[i][6])==-1 and int(self.listalinea[i][3])==0:
                        pendopci=pendopci+ int(self.listalinea[i][5])
            listadetalle=[suma,apro,cursad,pendobli,pendopci]
            return listadetalle
        else:
            messagebox.showerror(message= f"No hay semestre mayor a {mayor}",title="Conteo de creditos")
            listadetalle=[-1,-1,-1,-1,-1]
            return listadetalle
       








    



                  
                        
                        
  