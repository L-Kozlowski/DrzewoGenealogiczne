import tkinter as tk
from typing import Optional

from person import Person
from connection_line import ConnectionLine
from window_add_person import WindowAddPerson
from window_edit_person import WindowEditPerson
from person_list import PersonList

class WindowMain:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Drzewo Genealogiczne")
        self.canvas = tk.Canvas(self.root, width=1000, height=800, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.person_list = PersonList(self.canvas)
        # self.persons: list[Person] = []
        # self.lines: list[ConnectionLine] = []

        self.dragging = None
        self.last_x = 0
        self.last_y = 0
        self.scroll_speed = 0.5

        self.selected_person = None
        self.pending_new_window = None

        self.setup_ui()
        self.bind_events()

        self.person_list.add_to_persons(Person(self.canvas, 300, 300, "Adam", "Kowalski"))
        self.person_list.add_to_persons(Person(self.canvas, 500, 400, "Ania", "Nowak"))
        self.person_list.connect_persons(self.person_list.get_persons()[0],
                                         self.person_list.get_persons()[1], color="black")
        # self.connect_persons(self.persons[0], self.persons[1], color="black")
        self.view_offset = [0, 0]  # [x, y]
        self.view_cords= [0, 0]  # [x, y]
        self.canvas.tag_lower("line")


        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Dodaj nowa osone", command=self.add_connected_person)
        self.context_menu.add_command(label="Usun osobe", command=self.person_list.delete_person)
        self.context_menu.add_command(label="Edytuj osobe", command=self.edit_person)

        self.right_click_target = None  # prostokąt kliknięty prawym przyciskiem

        self.root.mainloop()

    def edit_person(self):
        WindowEditPerson(self.canvas, self.selected_person)

    def setup_ui(self):
        frame = tk.Frame(self.root)
        frame.place(x=10, y=10)

        add_btn = tk.Button(frame, text="Dodaj kwadrat", command=self.start_add_person)
        add_btn.pack(side=tk.LEFT, padx=0)

        reset_btn = tk.Button(frame, text="Reset widoku", command=self.reset_view)
        reset_btn.pack(side=tk.LEFT, padx=0)

        self.coord_label = tk.Label(self.root, text="x: 0, y: 0", bg="white")
        self.coord_label.place(relx=1.0, y=0, anchor="ne")

    def bind_events(self):
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.canvas.bind("<Motion>", self.update_coordinates)
        self.canvas.bind("<Button-3>", self.on_right_click)


    def on_right_click(self, event):
        person = self.get_clicked_person(event)

        if person is None:
            self.selected_person = None  # kliknięto poza prostokątami
            return

        self.selected_person = person
        self.person_list.set_selected_person(person)
        self.context_menu.tk_popup(event.x_root, event.y_root)

    def on_mouse_down(self, event):
        person = self.get_clicked_person(event)

        if person: # move person or select person
            if self.pending_new_window:
                self.selected_person = person
                # coords = person.get_center()
                # self.pending_new_window.show_selection(coords)
                self.pending_new_window.selected(person)
                self.person_list.set_selected_person(self.selected_person)
            else:
                self.dragging = person
                self.last_x = event.x
                self.last_y = event.y
        else:  # move background
            self.dragging = "canvas"
            self.last_x = event.x
            self.last_y = event.y

    def on_mouse_drag(self, event):
        if self.dragging == "canvas":
            dx = event.x - self.last_x
            dy = event.y - self.last_y

            self.view_offset[0] = dx * self.scroll_speed
            self.view_offset[1] = dy * self.scroll_speed
            self.view_cords[0] -= self.view_offset[0]
            self.view_cords[1] -= self.view_offset[1]

            for person in self.person_list.get_persons(): #self.persons
                person.move_display(self.view_offset[0],self.view_offset[1])
                for conn in person.connections:
                    conn.update()

            self.last_x = event.x
            self.last_y = event.y


        elif isinstance(self.dragging, Person):
            dx = event.x - self.last_x
            dy = event.y - self.last_y

            person = self.dragging
            person.move(dx, dy)

            self.last_x = event.x
            self.last_y = event.y
            for connection in person.connections:
                connection.update()

    def on_mouse_up(self, event):
        self.dragging = None

    def reset_view(self):
        for person in self.person_list.get_persons(): #self.persons:
            person.reset_display()
        self.person_list.update_all_lines()
        self.view_cords = [0,0]

    # def update_all_lines(self):
    #     for line in self.lines:
    #         line.update()

    def update_coordinates(self, event):
        x, y = self.view_cords
        self.coord_label.config(text=f"Widok: x={int(x)}, y={int(y)}")

    def start_add_person(self):
        self.pending_new_window = WindowAddPerson(self.root, self, self.canvas, self.person_list)

    def add_connected_person(self):
        if self.selected_person:
            self.pending_new_window = WindowAddPerson(self.root, self, self.canvas, self.person_list)
            self.pending_new_window.selected(self.selected_person)
            self.person_list.set_selected_person(self.selected_person)

    def get_clicked_person(self, event) -> Optional[Person]:
        clicked = self.canvas.find_overlapping(event.x, event.y, event.x, event.y)
        clicked_ids = set(clicked)

        for person in self.person_list.get_persons(): #self.persons:
            if person.check_if_clicked(clicked_ids):
                return person
        return None

    # def add_to_persons(self, person: Person):
    #     self.persons.append(person)
    #

    # def connect_persons(self, r1: Person, r2: Person, color="black"):
    #     line = ConnectionLine(self.canvas, r1, r2, color=color)
    #     self.canvas.tag_lower("line")
    #     self.lines.append(line)

    # def delete_person(self):
    #
    #     # validation
    #     if len(self.selected_person.connections) > 1:
    #         print("To many connections")
    #     elif len(self.persons) == 1:
    #         print("You cannot delete last one")
    #     else:
    #         # delete person
    #         selected_person = self.selected_person
    #         selected_person.delete_canvas()
    #         self.persons.remove(selected_person)
    #
    #         # delete connected lines
    #         for line in selected_person.connections:
    #              line.delete()
        



if __name__ == "__main__":
    WindowMain()