import tkinter as tk
import json

def pNotes(many, notas):
    pNotes = tk.Toplevel()
    pNotes.title("Notas guardadas")
    pNotes.geometry("800x600")


    titulo = tk.Label(pNotes, text = "Estas son tus notas guardadas.")
    titulo.pack()

    listbox = tk.Listbox(pNotes, selectmode=tk.MULTIPLE)  # MULTIPLE o SINGLE
    listbox.pack(pady=10, fill=tk.BOTH, expand=True)

    for id_nota, contenido in notas.items():
        listbox.insert(tk.END, f"{id_nota}: {contenido['nota']}")

    def delatenotes():
        ide = id.get()
        if ide in notas:
            del notas[ide]
            print(f"Borraste la nota numero {ide}")
            pNotes.update()
            with open('notas.json', 'w', encoding='utf-8') as f:
                json.dump(notas, f, indent=4)
        else:
            print("Pvto bruto jaja")

    boton = tk.Button(pNotes, text="Ver notas", command=lambda: delatenotes())
    boton.pack(pady=20)

    titulo = tk.Label(pNotes, text = "Pon el id de la nota que deseas eliminar:")
    titulo.pack()

    id = tk.Entry(pNotes)
    id.pack()

    boton = tk.Button(pNotes, text="Borrar nota", command=lambda: delatenotes())
    boton.pack(pady=20)
