import tkinter as tk



class WindowPerson():
    def __init__(self, master):
        self.top = tk.Toplevel(master)
        self.entries = {}

    def add_buttons(self):
        button_frame = tk.Frame(self.top)
        button_frame.pack(pady=10)
        tk.Button(button_frame, text="Dodaj", command=self.on_confirm).pack(side=tk.LEFT, padx=5)
        tk.Button(button_frame, text="Anuluj", command=self.on_cancel).pack(side=tk.LEFT, padx=5)

    def add_input_entries(self):

        self.entries = {
            "Name": self.create_input("Imie"),
            "Surname": self.create_input("Nazwisko"),
            "Birthday_date": self.create_input("Data urodzenia"),
            "Birthday_place": self.create_input("Miejsce urodzenia"),
            "Line_color": self.create_input("Kolor linii (np. black, blue)", "black"),
        }
    def create_input(self, txt_label: str, txt_input = "") -> tk.Entry:
        """
        create a new input
        :param txt_input: text to be inserted in the entries
        :param txt_label: label text
        :return: new input box with label
        """
        tk.Label(self.top, text=txt_label+":").pack()
        entry = tk.Entry(self.top)
        entry.insert(0, txt_input)
        entry.pack()
        return entry

    def get_entry_value(self) -> dict[str,str]:
        entry_values = {}
        for key, entry in self.entries.items():
            entry_values[key] = entry.get()
        return entry_values

    def on_confirm(self):
        pass
    def on_cancel(self):
        pass