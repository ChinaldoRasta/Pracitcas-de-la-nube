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
