from typing import TYPE_CHECKING
from window_person import WindowPerson
if TYPE_CHECKING:
    from person import Person

class WindowEditPerson(WindowPerson):
    def __init__(self, master, person : 'Person'):
        super().__init__(master)
        self.person = person
        self.top.title("Edytuj kwadrat")
        self.add_input_entries()
        self.insert_input()
        self.add_buttons()

    def insert_input(self):
        for key, value in self.person.personalities.items():
            self.entries[key].insert(0, value)

    def on_confirm(self):
        self.person.set_personalities(self.get_entry_value())
        self.top.destroy()

    def on_cancel(self):
        self.top.destroy()