import tkinter as tk
from tkinter import ttk, messagebox
from validators import validar_producto, validar_cantidad, validar_precio
from venta_service import registrar_venta, obtener_ventas, eliminar_venta, calcular_total, actualizar_venta


class App:
    def __init__(self, root):
        self.id_seleccionado = None
        self.root = root
        self.root.title("Sistema de Ventas Diarias")
        self.root.geometry("900x500")
        self.root.resizable(False, False)

        self.crear_interfaz()
        self.cargar()

    def crear_interfaz(self):
        frame_form = tk.LabelFrame(self.root, text="Registro de venta", padx=10, pady=10)
        frame_form.pack(fill="x", padx=10, pady=10)

        tk.Label(frame_form, text="Producto").grid(row=0, column=0, padx=5, pady=5)
        self.producto = tk.Entry(frame_form, width=25)
        self.producto.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame_form, text="Cantidad").grid(row=0, column=2, padx=5, pady=5)
        self.cantidad = tk.Entry(frame_form, width=15)
        self.cantidad.grid(row=0, column=3, padx=5, pady=5)

        tk.Label(frame_form, text="Precio").grid(row=0, column=4, padx=5, pady=5)
        self.precio = tk.Entry(frame_form, width=15)
        self.precio.grid(row=0, column=5, padx=5, pady=5)

        tk.Button(frame_form, text="Registrar venta", command=self.guardar, width=18).grid(
            row=0, column=6, padx=10, pady=5
        )

        frame_tabla = tk.Frame(self.root)
        frame_tabla.pack(fill="both", expand=True, padx=10, pady=10)

        self.tabla = ttk.Treeview(
            frame_tabla,
            columns=("ID", "Producto", "Cantidad", "Precio", "Total", "Fecha"),
            show="headings",
            height=15
        )

        self.tabla.heading("ID", text="ID")
        self.tabla.heading("Producto", text="Producto")
        self.tabla.heading("Cantidad", text="Cantidad")
        self.tabla.heading("Precio", text="Precio")
        self.tabla.heading("Total", text="Total")
        self.tabla.heading("Fecha", text="Fecha")

        self.tabla.column("ID", width=60, anchor="center")
        self.tabla.column("Producto", width=220, anchor="center")
        self.tabla.column("Cantidad", width=100, anchor="center")
        self.tabla.column("Precio", width=100, anchor="center")
        self.tabla.column("Total", width=100, anchor="center")
        self.tabla.column("Fecha", width=250, anchor="center")

        scrollbar = ttk.Scrollbar(frame_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscrollcommand=scrollbar.set)

        self.tabla.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        frame_acciones = tk.Frame(self.root)
        frame_acciones.pack(fill="x", padx=10, pady=10)

        tk.Button(
            frame_acciones,
            text="Eliminar venta seleccionada",
            command=self.eliminar,
            width=25
        ).pack(side="left")

        tk.Button(
            frame_acciones,
            text="Seleccionar",
            command=self.seleccionar,
            width=15
        ).pack(side="left", padx=5)

        tk.Button(
            frame_acciones,
            text="Actualizar venta",
            command=self.actualizar,
            width=20
        ).pack(side="left", padx=5)

        self.total_label = tk.Label(
            frame_acciones,
            text="Total vendido: S/ 0.00",
            font=("Arial", 12, "bold")
        )
        self.total_label.pack(side="right")

    def guardar(self):
        p = self.producto.get()
        c = self.cantidad.get()
        pr = self.precio.get()

        if not validar_producto(p):
            messagebox.showerror("Error", "Ingrese un producto válido")
            return

        if not validar_cantidad(c):
            messagebox.showerror("Error", "Ingrese una cantidad válida")
            return

        if not validar_precio(pr):
            messagebox.showerror("Error", "Ingrese un precio válido")
            return

        exito = registrar_venta(p, int(c), float(pr))

        if exito:
            messagebox.showinfo("Éxito", "Venta registrada correctamente")
            self.limpiar_campos()
            self.cargar()
        else:
            messagebox.showerror("Error", "No se pudo registrar la venta")

    def cargar(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)

        for v in obtener_ventas():
            self.tabla.insert("", tk.END, values=v)

        total = calcular_total()
        self.total_label.config(text=f"Total vendido: S/ {total:.2f}")

    def eliminar(self):
        item = self.tabla.selection()

        if not item:
            messagebox.showwarning("Advertencia", "Seleccione una venta para eliminar")
            return

        id_venta = self.tabla.item(item[0])["values"][0]
        eliminar_venta(id_venta)
        self.cargar()

    def limpiar_campos(self):
        self.producto.delete(0, tk.END)
        self.cantidad.delete(0, tk.END)
        self.precio.delete(0, tk.END)

    def seleccionar(self):
        item = self.tabla.selection()

        if not item:
            messagebox.showwarning("Advertencia", "Seleccione una venta")
            return

        datos = self.tabla.item(item[0])["values"]

        self.id_seleccionado = datos[0]

        self.producto.delete(0, tk.END)
        self.producto.insert(0, datos[1])

        self.cantidad.delete(0, tk.END)
        self.cantidad.insert(0, datos[2])

        self.precio.delete(0, tk.END)
        self.precio.insert(0, datos[3])

    def actualizar(self):
        if self.id_seleccionado is None:
            messagebox.showwarning("Advertencia", "Seleccione una venta primero")
            return

        p = self.producto.get()
        c = self.cantidad.get()
        pr = self.precio.get()

        if not validar_producto(p):
            messagebox.showerror("Error", "Producto inválido")
            return

        if not validar_cantidad(c):
            messagebox.showerror("Error", "Cantidad inválida")
            return

        if not validar_precio(pr):
            messagebox.showerror("Error", "Precio inválido")
            return

        exito = actualizar_venta(self.id_seleccionado, p, int(c), float(pr))

        if exito:
            messagebox.showinfo("Éxito", "Venta actualizada")
            self.id_seleccionado = None
            self.limpiar_campos()
            self.cargar()
        else:
            messagebox.showerror("Error", "No se pudo actualizar")