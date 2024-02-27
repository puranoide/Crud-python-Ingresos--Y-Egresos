from tkinter import *
import sqlite3
import customtkinter
from tkcalendar import DateEntry
##import pandas as pd
##import openpyxl
from tkinter import ttk
##from tkinter.filedialog import asksaveasfilename
import datetime
import pandas as pd
ventana=customtkinter.CTk()
ventana.title("Gestor de finanzas")
ventana.geometry("1000x800")
ventana.resizable(False,FALSE)
ventana.configure(fg_color="#FFFFFF")




nombre=StringVar()
motivo=StringVar()
monto=StringVar()

Fechacompleta=StringVar()
categoria=StringVar()
total=IntVar()
modificar=False

            
def show_selected_record(event):
    selected_item = tbpagos.focus()
    if selected_item:
        values = tbpagos.item(selected_item, "values")
        if values:
            nombre.set(values[1])
            motivo.set(values[2])
            monto.set(values[3])
            
            categoria.set(values[4])
            
def show_selected_record2(event):
    selected_item = tbpagos2.focus()
    if selected_item:
        values = tbpagos2.item(selected_item, "values")
        if values:
            nombre.set(values[1])
            motivo.set(values[2])
            monto.set(values[3])
            
            categoria.set(values[4])
            
lblNombre=customtkinter.CTkLabel(ventana,text="Nombre",fg_color="#FFFFFF",text_color="black").grid(column=0,row=0,padx=50,pady=5)
txtNombre=customtkinter.CTkEntry(ventana,textvariable=nombre)
txtNombre.grid(column=1,row=0)

lblMonto=customtkinter.CTkLabel(ventana,text="Monto",fg_color="#FFFFFF",text_color="black").grid(column=0,row=1,padx=1,pady=5)
txtMonto=customtkinter.CTkEntry(ventana,textvariable=monto)
txtMonto.grid(column=1,row=1)

lbldesc=customtkinter.CTkLabel(ventana,text="Motivo",fg_color="#FFFFFF",text_color="black").grid(column=0,row=2,padx=1,pady=1)
txtdesc=customtkinter.CTkEntry(ventana,textvariable=motivo)
txtdesc.grid(column=1,row=2)
lblfecha=customtkinter.CTkLabel(ventana,text="Fecha",fg_color="#FFFFFF",text_color="black").grid(column=2,row=0,padx=1,pady=1)
calendario = DateEntry(ventana, width=12, background='darkblue',
                       foreground='white', borderwidth=2, date_pattern='dd/MM/yyyy')
calendario.grid(column=3,row=0)
lblcategoria=customtkinter.CTkLabel(ventana,text="categoria",fg_color="#FFFFFF",text_color="black").grid(column=2,row=1,padx=1,pady=1)
txtcategoria=customtkinter.CTkEntry(ventana,textvariable=categoria)
txtcategoria.grid(column=3,row=1)

txtmensaje=customtkinter.CTkLabel(ventana,text="MENSAJES",pady=1,fg_color="#FFFFFF",text_color="black")
txtmensaje.grid(column=0,row=7,columnspan=1)
txttotal=customtkinter.CTkLabel(ventana,text="total ingresos")
txttotal.grid(column=3,row=8)
txttotalegresos=customtkinter.CTkLabel(ventana,text="total egresos")
txttotalegresos.grid(column=3,row=9)
txttotalbalance=customtkinter.CTkLabel(ventana,text="balance total")
txttotalbalance.grid(column=3,row=10)

tbpagos=ttk.Treeview(ventana,selectmode=NONE,height=4)
tbpagos.grid(column=0,row=5,columnspan=6,padx=30,pady=10)

tbpagos["columns"]=("ID","NOMBRE","MOTIVO","MONTO","CATEGORIA","FECHA")
tbpagos.column("#0",width=0,stretch=NO)
tbpagos.column("ID",width=40,anchor=CENTER)
tbpagos.column("NOMBRE",width=200,anchor=CENTER)
tbpagos.column("MOTIVO",width=400,anchor=CENTER)
tbpagos.column("MONTO",width=100,anchor=CENTER)
tbpagos.column("FECHA",width=100,anchor=CENTER)
tbpagos.column("CATEGORIA",width=100,anchor=CENTER)

tbpagos.heading("#0",text="")
tbpagos.heading("ID",text="ID")
tbpagos.heading("NOMBRE",text="PERSONA RESPONSABLE")
tbpagos.heading("MOTIVO",text="MOTIVO")
tbpagos.heading("MONTO",text="MONTO")
tbpagos.heading("FECHA",text="FECHA")
tbpagos.heading("CATEGORIA",text="CATEGORIA")
tbpagos.bind("<<TreeviewSelect>>", show_selected_record)

tbpagos2=ttk.Treeview(ventana,selectmode=NONE,height=4)
tbpagos2.grid(column=0,row=6,columnspan=6,padx=10,pady=10)

tbpagos2["columns"]=("ID","NOMBRE","MOTIVO","MONTO","CATEGORIA","FECHA")
tbpagos2.column("#0",width=0,stretch=NO)
tbpagos2.column("ID",width=40,anchor=CENTER)
tbpagos2.column("NOMBRE",width=200,anchor=CENTER)
tbpagos2.column("MOTIVO",width=400,anchor=CENTER)
tbpagos2.column("MONTO",width=100,anchor=CENTER)
tbpagos2.column("FECHA",width=100,anchor=CENTER)
tbpagos2.column("CATEGORIA",width=100,anchor=CENTER)

tbpagos2.heading("#0",text="")
tbpagos2.heading("ID",text="ID")
tbpagos2.heading("NOMBRE",text="PERSONA RESPONSABLE")
tbpagos2.heading("MOTIVO",text="MOTIVO")
tbpagos2.heading("MONTO",text="MONTO")
tbpagos2.heading("FECHA",text="FECHA")
tbpagos2.heading("CATEGORIA",text="CATEGORIA")
tbpagos2.bind("<<TreeviewSelect>>", show_selected_record2)

btnnuevo=customtkinter.CTkButton(ventana,text="guardar",command=lambda:agregar_registro(),border_color="#332424",border_width=2,text_color="black",fg_color="#3BFF5E",hover_color="white")
btnnuevo.grid(column=0,row=8,pady=10)
btnguardaralexcel=customtkinter.CTkButton(ventana,text="Generar excel",command=lambda:crearExcel())
btnguardaralexcel.grid(column=0,row=9)
btnEliminar=customtkinter.CTkButton(ventana,text="eliminar ingreso ",command=lambda:eliminarRegistroIngreso(),border_color="#332424",border_width=2,text_color="black",fg_color="#188C28",hover_color="white")
btnEliminar.grid(column=1,row=8,pady=10)
btnEliminaregreso=customtkinter.CTkButton(ventana,text="eliminar egreso",command=lambda:eliminarRegistroegreso(),border_color="#332424",border_width=2,text_color="black",fg_color="#D51D41",hover_color="white")
btnEliminaregreso.grid(column=1,row=9,pady=10)
btnmodificar=customtkinter.CTkButton(ventana,text="seleccionar ingreso",command=lambda:actualizarPAGOS(),border_color="#332424",border_width=2,text_color="black",fg_color="#188C28",hover_color="white")
btnmodificar.grid(column=2,row=8)
btnmodificaregresos=customtkinter.CTkButton(ventana,text="seleccionar egreso",command=lambda:actualizarEGRESOS(),border_color="#332424",border_width=2,text_color="black",fg_color="#D51D41",hover_color="white")
btnmodificaregresos.grid(column=2,row=9)


##funciones

def validar():
    return len(motivo.get()) 


def limpiar():
    nombre.set("")
    motivo.set("")
    monto.set("")
    categoria.set("")


def vaciartabla():
    tbpagos.delete(*tbpagos.get_children())

def vaciartablanega():
    tbpagos2.delete(*tbpagos2.get_children())
    

def mostrar_datos():
    # Conectarse a la base de datos
    conexion = sqlite3.connect("bdDatosFechas.db")
    cursor = conexion.cursor()
    
    # Obtener los datos de la tabla "pagos"
    cursor.execute("SELECT ID,NOMBREPAGO,MOTIVO,MONTO,CATEGORIA,FECHA FROM REGISTROS")
    datos_pagos = cursor.fetchall()
    
    # Limpiar los datos existentes en el Treeview
    
    vaciartabla()
        # Insertar los nuevos datos en el Treeview
    for dato in datos_pagos:
        
        if dato[3]>0:
            tbpagos.insert("", "end", values=dato,tags=("ingreso"))
            
    tbpagos.tag_configure("ingreso",background="#3BFF5E")
    
    # Cerrar la conexión a la base de datos
    conexion.close()
    modificarFalse()
    modificarFalseegresos()
    mostrartotal()
    mostrarbalancetotal()
    
    

def mostrarnegativos():
    # Conectarse a la base de datos
    conexion = sqlite3.connect("bdDatosFechas.db")
    cursor = conexion.cursor()
    
    # Obtener los datos de la tabla "pagos"
    cursor.execute("SELECT ID,NOMBREPAGO,MOTIVO,MONTO,CATEGORIA,FECHA FROM REGISTROS")
    datos_pagos = cursor.fetchall()
    
    # Limpiar los datos existentes en el Treeview
    
    vaciartablanega()
        # Insertar los nuevos datos en el Treeview
    for dato in datos_pagos:
        
        if dato[3]<=0:
            tbpagos2.insert("", "end", values=dato,tags=("egreso"))
            
    tbpagos2.tag_configure("egreso",background="#F08275")
    
    # Cerrar la conexión a la base de datos
    conexion.close()
    modificarFalse()
    modificarFalseegresos()
    mostrartotalneagtivo()
    
    
    
def agregar_registro():
    if validar():
        # Conectarse a la base de datos
        conexion = sqlite3.connect("bdDatosFechas.db")
        cursor = conexion.cursor()
        fecha=calendario.get_date()

        # Insertar el nuevo registro en la tabla "pagos"
        cursor.execute("INSERT INTO REGISTROS (NOMBREPAGO,MOTIVO,MONTO,CATEGORIA,FECHA) VALUES (?,?,?,?,?)", (nombre.get(),motivo.get(),monto.get(),categoria.get(),fecha))
    
        # Confirmar los cambios en la base de datos
        conexion.commit()
    
        # Cerrar la conexión a la base de datos
        conexion.close()
        limpiar()
        txtmensaje.configure(text="registro agregado correctamente",text_color="green")
    else:
        txtmensaje.configure(text="los campos no deben estar vacios",text_color="red")
    mostrar_datos()
    mostrarnegativos()

def eliminarRegistroIngreso():
        seleccion = tbpagos.selection()
        if seleccion:
            id_seleccionado = tbpagos.item(seleccion)["values"][0]
        
            # Conectarse a la base de datos
            conexion = sqlite3.connect("bdDatosFechas.db")
            cursor = conexion.cursor()
        
        # Eliminar el dato de la tabla "pagos" con el ID seleccionado
            cursor.execute("DELETE FROM REGISTROS WHERE ID = ?", (id_seleccionado,))
        
        # Confirmar los cambios en la base de datos
            conexion.commit()
            
        # Cerrar la conexión a la base de datos
            conexion.close()
            txtmensaje.configure(text="Registro eliminado correctamente",text_color="green")
        # Actualizar el Treeview para reflejar los cambios
        limpiar()
        vaciartabla()
        mostrar_datos()
       
def eliminarRegistroegreso():
    seleccion = tbpagos2.selection()
    if seleccion:
        id_seleccionado = tbpagos2.item(seleccion)["values"][0]
        
        # Conectarse a la base de datos
        conexion = sqlite3.connect("bdDatosFechas.db")
        cursor = conexion.cursor()
        
        # Eliminar el dato de la tabla "pagos" con el ID seleccionado
        cursor.execute("DELETE FROM REGISTROS WHERE ID = ?", (id_seleccionado,))
        
        # Confirmar los cambios en la base de datos
        conexion.commit()
            
        # Cerrar la conexión a la base de datos
        conexion.close()
        txtmensaje.configure(text="Registro eliminado correctamente",text_color="green")
        # Actualizar el Treeview para reflejar los cambios
        limpiar()
        vaciartablanega()
        mostrarnegativos()


def modificarFalse():
    global modificar
    modificar=False
    tbpagos.config(selectmode=NONE)
    tbpagos2.config(selectmode=NONE)
    btnnuevo.configure(text="guardar")
    btnmodificar.configure(text="seleccionar ingreso")
    btnmodificaregresos.configure(state=NORMAL)
    btnEliminar.configure(state=DISABLED)
    btnEliminaregreso.configure(state=DISABLED)
    
    
def modificarTrue():
    global modificar
    modificar=True
    tbpagos.config(selectmode=BROWSE)
    tbpagos2.config(selectmode=NONE)
    btnnuevo.configure(text="nuevo")
    btnmodificar.configure(text="modificar")
    btnEliminaregreso.configure(text="seleccionar egreso",state=DISABLED)
    btnmodificaregresos.configure(state=DISABLED)
    btnEliminar.configure(state=NORMAL)
    btnEliminaregreso.configure(state=DISABLED)

def modificarFalseegresos():
    global modificar
    modificar=False
    tbpagos.config(selectmode=NONE)
    tbpagos2.config(selectmode=NONE)
    btnnuevo.configure(text="guardar")
    btnmodificar.configure(text="seleccionar ingreso",state=NORMAL)
    btnEliminaregreso.configure(text="seleccionar egreso")
    btnEliminar.configure(state=DISABLED)
    btnEliminaregreso.configure(state=DISABLED)
    
def modificarTrueegresos():
    global modificar
    modificar=True
    tbpagos.config(selectmode=NONE)
    tbpagos2.config(selectmode=BROWSE)
    btnnuevo.configure(text="nuevo")
    btnmodificar.configure(state=DISABLED)
    btnEliminaregreso.configure(text="eliminar egreso")
    
    btnEliminar.configure(state=DISABLED)
    btnEliminaregreso.configure(state=NORMAL)

def actualizarPAGOS():
    if modificar==True:
        if validar():
           selected_item = tbpagos.focus()
           if selected_item:
               values = tbpagos.item(selected_item, "values")
               if values:
                   
                   record_id = values[0]  # Assuming the ID is stored in the first column
                   new_NOMBRE = nombre.get()
                   new_MOTIVO = motivo.get()
                   fecha=calendario.get_date()
                   new_MONTO = monto.get()
                   new_CATEGORIA = categoria.get()
                   # Update the record in the SQLite database
                   connection = sqlite3.connect("bdDatosFechas.db")  # Replace "database.db" with your database file
                   cursor = connection.cursor()
                   cursor.execute("UPDATE REGISTROS SET NOMBREPAGO=?, MOTIVO=?,FECHA=?,MONTO=?,CATEGORIA=? WHERE id=?", (new_NOMBRE, new_MOTIVO,fecha,new_MONTO,new_CATEGORIA, record_id))
                   connection.commit()
                   connection.close()
                   vaciartabla()
                   vaciartablanega()
                   mostrar_datos()
                   mostrarnegativos()
                   txtmensaje.configure(text="registro actualizado",text_color="green")
                   limpiar()
        else:
                
            txtmensaje.configure(text="los campos no deben estar vacios",text_color="red")
    else:
        modificarTrue()

def actualizarEGRESOS():
    if modificar==True:
        if validar():
           selected_item = tbpagos2.focus()
           if selected_item:
               values = tbpagos2.item(selected_item, "values")
               if values:
                   
                   record_id = values[0]  # Assuming the ID is stored in the first column
                   new_NOMBRE = nombre.get()
                   new_MOTIVO = motivo.get()
                   fecha=calendario.get_date()
                   new_MONTO = monto.get()
                   new_CATEGORIA = categoria.get()
                   # Update the record in the SQLite database
                   connection = sqlite3.connect("bdDatosFechas.db")  # Replace "database.db" with your database file
                   cursor = connection.cursor()
                   cursor.execute("UPDATE REGISTROS SET NOMBREPAGO=?, MOTIVO=?,FECHA=?,MONTO=?,CATEGORIA=? WHERE id=?", (new_NOMBRE, new_MOTIVO,fecha,new_MONTO,new_CATEGORIA, record_id))
                   connection.commit()
                   connection.close()
                   vaciartabla()
                   vaciartablanega()
                   mostrarnegativos()
                   mostrar_datos()
                   txtmensaje.configure(text="registro actualizado",text_color="green")
                   limpiar()
        else:
                
            txtmensaje.configure(text="los campos no deben estar vacios",text_color="red")
    else:
        modificarTrueegresos()
    
def mostrartotal():
    totalarray=[]
    totalpositivo=0
    connexion=sqlite3.connect("bdDatosFechas.db")
    cursor=connexion.cursor()
    cursor.execute("SELECT MONTO FROM REGISTROS")
    resultado = cursor.fetchall()
    for res in resultado:
        totalarray.append(res[0])
    
    for num in totalarray:
        if num>0:
            totalpositivo+=num
            
    txttotal.configure(text="Total de ingresos: " + str(totalpositivo),text_color="green")
    
def mostrartotalneagtivo():
    totalarray=[]
    totalpositivo=0
    connexion=sqlite3.connect("bdDatosFechas.db")
    cursor=connexion.cursor()
    cursor.execute("SELECT MONTO FROM REGISTROS")
    resultado = cursor.fetchall()
    for res in resultado:
        totalarray.append(res[0])
    
    for num in totalarray:
        if num<0:
            totalpositivo+=num
            
    txttotalegresos.configure(text="Total de ingresos: " + str(totalpositivo),text_color="red")
        
def mostrarbalancetotal():
    balancetotales=[]
    totalbalance=0
    conexion=sqlite3.connect("bdDatosFechas.db")
    cursor=conexion.cursor()
    cursor.execute("SELECT MONTO FROM REGISTROS")
    resultado=cursor.fetchall()
    for res in resultado:
        balancetotales.append(res[0])
    for mon in balancetotales:
        totalbalance+=mon
    if(totalbalance<0):
        txttotalbalance.configure(text="balance total:"+str(totalbalance),text_color="red")
    else:
        txttotalbalance.configure(text="balance total:"+str(totalbalance),text_color="green")

def crearExcel():
    conexion=sqlite3.connect("bdDatosFechas.db")
    query="SELECT*FROM REGISTROS"
    df=pd.read_sql_query(query,conexion)
    conexion.close()
    df.to_excel("RegistrosYtotales.xlsx",index=False)
    suma_total=df["MONTO"].sum()
    df_BalanceTotal=pd.DataFrame({"Total":[suma_total]})
    with pd.ExcelWriter("RegistrosYtotales.xlsx",mode="a",engine="openpyxl") as writer:
        df_BalanceTotal.to_excel(writer,sheet_name="resumenbalance",index=False)
    print("Archivo de Excel generado exitosamente.")
    txtmensaje.configure(text="Archivo Creado")
      
    
mostrarnegativos()
mostrar_datos()


ventana.mainloop()
