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
