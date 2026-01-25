import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import mysql.connector

# =========================
# CONFIG DB (cámbialo)
# =========================
DB_CONFIG = {
    "host": "localhost",
    "user": "root",          # <-- tu usuario MySQL
    "password": "",          # <-- tu contraseña MySQL
    "database": "biblioteca_crud",
    "port": 3306
}
# =========================
# UTILIDADES
# =========================
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
# =========================
# APP
# =========================
class BibliotecaCRUD(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CRUD Biblioteca - Python + MySQL")
        self.geometry("980x560")
        self.resizable(False, False)

        self.editoriales_map = {}  # nombre -> id
        self.selected_book_id = None

        self._build_ui()
        self._load_editoriales()
        self._load_books(activos=True)

    def db(self):
        return mysql.connector.connect(**DB_CONFIG)
