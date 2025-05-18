import tkinter as tk
from typing import TYPE_CHECKING
from person import Person
from window_person import WindowPerson
if TYPE_CHECKING:
    from person import Person  # tylko do podpowiedzi typu, nie aktywny przy uruchamianiu
    from window_main import WindowMain
    from person_list import PersonList

class WindowAddPerson(WindowPerson):
    def __init__(self, master: tk.Tk, window_main: 'WindowMain', canvas: tk.Canvas, person_list: 'PersonList'):
        super().__init__(master)
        self.window_main = window_main
        self.canvas = canvas
        self.top.title("Dodaj nowy kwadrat")
        self.person_list = person_list

        tk.Label(self.top, text="Kliknij na osobę żeby zrobić połącznie").pack(pady=5)
        self.coords_label = tk.Label(self.top, text="Nie wybrano osoby")
        self.coords_label.pack(pady=5)

        self.add_input_entries()
        self.add_buttons()
        self.selected_person = None

    def show_selection(self, label):
        self.coords_label.config(text=f"Wybrano osobe: {label}")

    def on_confirm(self):
        if self.selected_person:
            x, y = self.selected_person.get_center()
            entry_values = self.get_entry_value()
            new_person = Person(self.canvas, x + 150, y)
            new_person.set_personalities(entry_values)
            self.person_list.add_to_persons(new_person)
            self.person_list.connect_persons(self.selected_person, new_person, color=entry_values["Line_color"])
        self.selected_person = None
        self.window_main.pending_new_window = None
        self.top.destroy()

    def on_cancel(self):
        self.selected_person = None
        self.window_main.pending_new_window = None
        self.top.destroy()

    def selected(self, person: 'Person'):
        self.selected_person = person
        self.show_selection(person.get_name_and_surname()[0] + " " + person.get_name_and_surname()[1])
