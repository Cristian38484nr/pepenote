import tkinter as tk
from tkinter import messagebox
from notes import pNotes
import json

notas = {}
try:
    with open('notas.json', 'r', encoding='utf-8') as f:
        notas = json.load(f)
except FileNotFoundError:
    with open('notas.json', 'w', encoding='utf-8') as f:
        json.dump({}, f)

many = tk.Tk()
many.title("Notas")
many.geometry("800x600")

titulo1 = tk.Label(many, text = "Inicio")
titulo1.pack()

text = tk.Text(many)
text.pack()


def vernotas(many, notas):
    pNotes(many, notas)
    many.withdraw()

def guardaN():
    nota = text.get("1.0", tk.END)
    nota = nota.strip()
    if len(nota) < 1:
        messagebox.showerror("Error", "Debes escribir algo.")
    else:
        messagebox.showinfo("Exito", "Nota guardada")
        if notas:
            nuevo_id = max(map(int, notas.keys())) + 1
        else:
            nuevo_id = 1

        notas[nuevo_id] = {
            "nota": nota
        }
        with open('notas.json', 'w', encoding='utf-8') as f:
            json.dump(notas, f, indent=4)
    

boton = tk.Button(many, text="Ver notas", command=lambda: vernotas(many, notas))
boton.pack(pady=20)

boton = tk.Button(many, text="Guardar nota", command=lambda: guardaN())
boton.pack(pady=20)

many.mainloop()