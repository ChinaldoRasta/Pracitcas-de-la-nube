import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import mysql.connector


DB_CONFIG = {
    "host": "localhost",
    "user": "root",         
    "password": "",         
    "database": "biblioteca_crud",
    "port": 3306
}

def parse_date(date_str: str):
    """Acepta YYYY-MM-DD"""
    try:
        return datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
    except ValueError:
        return None

def parse_decimal(value: str):
    try:
        v = float(value.strip())
        if v < 0:
            return None
        return round(v, 2)
    except ValueError:
        return None

class BibliotecaCRUD(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRUD Biblioteca - Python + MySQL")
        self.geometry("980x560")
        self.resizable(False, False)

        self.editoriales_map = {}  
        self.selected_book_id = None

        self._build_ui()
        self._load_editoriales()
        self._load_books(activos=True)

    def db(self):
        return mysql.connector.connect(**DB_CONFIG)
    
    def _build_ui(self):
       
        frm = ttk.LabelFrame(self, text="Datos del libro")
        frm.place(x=15, y=15, width=950, height=170)

        ttk.Label(frm, text="Nombre del libro:").place(x=12, y=15)
        self.ent_nombre = ttk.Entry(frm, width=40)
        self.ent_nombre.place(x=130, y=15)

        ttk.Label(frm, text="Autor:").place(x=450, y=15)
        self.ent_autor = ttk.Entry(frm, width=35)
        self.ent_autor.place(x=505, y=15)

        ttk.Label(frm, text="Fecha lanzamiento (YYYY-MM-DD):").place(x=12, y=55)
        self.ent_fecha = ttk.Entry(frm, width=20)
        self.ent_fecha.place(x=230, y=55)

        ttk.Label(frm, text="Editorial:").place(x=450, y=55)
        self.cmb_editorial = ttk.Combobox(frm, state="readonly", width=32)
        self.cmb_editorial.place(x=520, y=55)

        ttk.Label(frm, text="Costo:").place(x=12, y=95)
        self.ent_costo = ttk.Entry(frm, width=20)
        self.ent_costo.place(x=130, y=95)
    # ---------- CRUD ----------
    def registrar(self):
        data, err = self._get_form_data()
        if err:
            messagebox.showwarning("Validación", err)
            return

        try:
            with self.db() as conn:
                cur = conn.cursor()
                cur.execute(
                    """
                    INSERT INTO libros (nombre_libro, autor, fecha_lanzamiento, editorial_id, costo, activo)
                    VALUES (%s, %s, %s, %s, %s, 1);
                    """,
                    data
                )
                conn.commit()
            messagebox.showinfo("OK", "Libro registrado.")
            self._load_books(activos=self.var_activos.get())
            self.limpiar_form()
        except Exception as e:
            messagebox.showerror("DB Error", f"No se pudo registrar:\n{e}")
    def _load_books(self, activos=True):
        self.tree.delete(*self.tree.get_children())
        self.selected_book_id = None

        try:
            with self.db() as conn:
                cur = conn.cursor()
                sql = """
                    SELECT l.id, l.nombre_libro, l.autor, l.fecha_lanzamiento, e.nombre, l.costo, l.activo
                    FROM libros l
                    JOIN editoriales e ON e.id = l.editorial_id
                """
                if activos:
                    sql += " WHERE l.activo=1 "
                sql += " ORDER BY l.id DESC;"

                cur.execute(sql)
                for row in cur.fetchall():
                    self.tree.insert("", "end", values=row)
        except Exception as e:
            messagebox.showerror("DB Error", f"No se pudo cargar libros:\n{e}")
