import tkinter as tk
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from person import Person  # tylko do podpowiedzi typu, nie aktywny przy uruchamianiu
    from window_main import WindowMain


class WindowAddPerson:
    def __init__(self, master: tk.Tk, window_main: 'WindowMain'):
        self.window_main = window_main
        self.top = tk.Toplevel(master)
        self.top.title("Dodaj nowy kwadrat")

        tk.Label(self.top, text="Kliknij na osobę żeby zrobić połącznie").pack(pady=5)

        self.coords_label = tk.Label(self.top, text="Nie wybrano osoby")
        self.coords_label.pack(pady=5)

        tk.Label(self.top, text="Imie").pack()
        self.name_entry = tk.Entry(self.top)
        self.name_entry.pack()
        tk.Label(self.top, text="Nazwisko").pack()
        self.surname_entry = tk.Entry(self.top)
        self.surname_entry.pack()
        tk.Label(self.top, text="Data urodzenia").pack()
        self.birthday_entry = tk.Entry(self.top)
        self.birthday_entry.pack()
        tk.Label(self.top, text="Miejsce urodzenia").pack()
        self.birthday_place_entry = tk.Entry(self.top)
        self.birthday_place_entry.pack()

        tk.Label(self.top, text="Kolor linii (np. black, blue):").pack()
        self.color_entry = tk.Entry(self.top)
        self.color_entry.insert(0, "black")
        self.color_entry.pack()

        self.selected_person = None

        button_frame = tk.Frame(self.top)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Dodaj", command=self.on_confirm).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Anuluj", command=self.on_cancel).pack(side=tk.LEFT, padx=5)


    def show_selection(self, label):
        self.coords_label.config(text=f"Wybrano osobe: {label}")

    def on_confirm(self):
        label = self.name_entry.get()[:10]
        color = self.color_entry.get()
        self.confirm_add_personangle(label, color)
        self.top.destroy()

    def on_cancel(self):
        self.cancel_add_personangle()
        self.top.destroy()

    def selected(self, person: 'Person'):
        self.selected_person = person
        self.show_selection(person.get_name_and_surname()[0] + " " + person.get_name_and_surname()[1])

    def confirm_add_personangle(self, label: str, color: str):
        if self.selected_person:
            x, y = self.selected_person.get_center()
            new_person = self.window_main.create_person(x + 150, y, label)
            self.window_main.connect_persons(self.selected_person, new_person, color=color)
        self.selected_person = None
        self.window_main.pending_new_window = None

    def cancel_add_personangle(self):
        self.selected_person = None
        self.window_main.pending_new_window = None