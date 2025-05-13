import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from person import Person

class WindowEditPerson:
    def __init__(self, master, person : 'Person'):
        self.person = person
        self.top = tk.Toplevel(master)
        self.top.title("Edytuj kwadrat")
        self.top.geometry("200x200")

        self.entries = {}
        self.entries["Name"] = self.create_input("Imie:", person.get_name_and_surname()[0])
        self.entries["Surname"] = self.create_input("Nazwisko:", person.get_name_and_surname()[1])
        # self.entries["Birthday_date"] = self.create_input("Miejsce urodzenia:", person.)


        button_frame = tk.Frame(self.top)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Potwierdź", command=self.on_confirm).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Anuluj", command=self.on_cancel).pack(side=tk.LEFT, padx=5)

    def create_input(self, txt_label: str, txt_input: str) -> tk.Entry:
        tk.Label(self.top, text=txt_label).pack()
        entry = tk.Entry(self.top)
        entry.pack()
        entry.insert(0, txt_input)
        return entry

    def on_confirm(self):
        self.person.edit_name(self.entries["Name"].get()[:15])
        self.person.edit_surname(self.entries["Surname"].get()[:15])

        self.top.destroy()

    def on_cancel(self):
        self.top.destroy()