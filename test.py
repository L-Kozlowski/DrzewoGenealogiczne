import tkinter as tk
from collections import defaultdict

class FamilyTreeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dynamiczne drzewo genealogiczne")

        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack()

        self.nodes = {}  # name -> {"parents": [], "children": []}
        self.positions = {}  # name -> (x, y)
        self.levels = defaultdict(list)

        # Przycisk dodawania osoby
        add_button = tk.Button(root, text="Dodaj osobę", command=self.open_add_person_window)
        add_button.pack(pady=10)

        # Dodajemy początkowych członków
        self.add_person("Dziecko")
        self.add_person("Ojciec", children = 'Dziecko')
        self.add_person("Matka",  children = 'Dziecko', marriage=["Ojciec"])
        self.add_person("Babcia", children = 'Ojciec')
        self.add_person("Dziadek", children = 'Ojciec', marriage=["Babcia"])

        self.level = 0

        # self.add_person("Ojciec", parents=["Dziadek", "Babcia"])
        # self.add_person("Dziecko", parents=["Ojciec", "Matka"])
        self.draw_tree()
        # print(self.nodes)

    def add_person(self, name, parents=None, marriage=None, children=None):
        if name in self.nodes:
            return

        self.nodes[name] = {"parents": [], "children": [],  "marriage" : []}
        if parents:
            self.nodes[name]["parents"] = parents
            for p in parents:
                if p in self.nodes:
                    self.nodes[p]["children"].append(name)
        if children:
            self.nodes[name]["children"] = children

        if marriage:
            self.nodes[name]["marriage"] = marriage
            for m in marriage:
                if m in self.nodes:
                    self.nodes[m]["marriage"].append(name)

    def layout_tree(self):
        self.levels.clear()
        visited = set()
        depth = {}

        def dfs(name, level):
            if name in visited:
                return
            visited.add(name)
            depth[name] = self.level
            if self.level == 0:
                self.levels[level].append(name)
                self.level += 1
            for l in self.levels:
                # print("l", l, " self.levels[l] ", self.levels[l], 'children',self.nodes[name]["children"] )
                if self.nodes[name]["children"] in  self.levels[l]:
                    self.levels[l+1].append(name)
                    break
            if max(self.levels) > self.level:
                self.level +=1
            # print("Levels",self.levels)


        # Start from roots (no parents)
        roots = [n for n, v in self.nodes.items() if not v["parents"]]
        # print("Roots", roots)
        for r in roots:
            # print("r", r)
            dfs(r, 0)

        # Assign X/Y positions
        self.positions.clear()
        max_width = 800
        level_height = 100

        for level, names in self.levels.items():
            print("level",level, "names", names)
            count = len(names)
            spacing = max_width // (count + 1)
            for i, name in enumerate(names):
                print("i", i, "name", name)
                x = spacing * (i + 1)
                y = level_height * (level + 1)
                self.positions[name] = (x, y)
            print(self.positions)

    def draw_line_90_deg(self, x1, y1, x2, y2):
        mid_y = (y1 + y2) // 2
        self.canvas.create_line(x1, y1, x1, mid_y)
        self.canvas.create_line(x1, mid_y, x2, mid_y)
        self.canvas.create_line(x2, mid_y, x2, y2)

    def draw_tree(self):
        self.canvas.delete("all")
        self.layout_tree()

        # Rysowanie osób
        for name, (x, y) in self.positions.items():
            self.canvas.create_rectangle(x - 40, y - 20, x + 40, y + 20, fill="lightblue")
            self.canvas.create_text(x, y, text=name)

        # Rysowanie linii
        for child, data in self.nodes.items():
            for parent in data["parents"]:
                if parent in self.positions and child in self.positions:
                    self.draw_line_90_deg(*self.positions[parent], *self.positions[child])

    def open_add_person_window(self):
        add_window = tk.Toplevel(self.root)
        add_window.title("Dodaj osobę")

        tk.Label(add_window, text="Imię:").grid(row=0, column=0)
        name_entry = tk.Entry(add_window)
        name_entry.grid(row=0, column=1)

        tk.Label(add_window, text="Rodzic 1 (opcjonalnie):").grid(row=1, column=0)
        parent1_entry = tk.Entry(add_window)
        parent1_entry.grid(row=1, column=1)

        tk.Label(add_window, text="Rodzic 2 (opcjonalnie):").grid(row=2, column=0)
        parent2_entry = tk.Entry(add_window)
        parent2_entry.grid(row=2, column=1)

        def confirm():
            name = name_entry.get().strip()
            p1 = parent1_entry.get().strip()
            p2 = parent2_entry.get().strip()
            parents = []
            if p1:
                parents.append(p1)
            if p2:
                parents.append(p2)
            if name:
                self.add_person(name, parents=parents)
                self.draw_tree()
                add_window.destroy()

        tk.Button(add_window, text="Dodaj", command=confirm).grid(row=3, columnspan=2, pady=10)

def main():
    root = tk.Tk()
    app = FamilyTreeApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
