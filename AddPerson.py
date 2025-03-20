import pygame
import tkinter as tk
import ctypes

from tkinter import simpledialog

class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long),
                ("top", ctypes.c_long),
                ("right", ctypes.c_long),
                ("bottom", ctypes.c_long)]

class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = text
        self.txt_surface = pygame.font.Font(None, 32).render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = pygame.font.Font(None, 32).render(self.text, True, self.color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))


class AddPersonWindow:
    def __init__(self, x, y):
        self.root = tk.Tk()
        self.root.title("Formularz")
        self.root.geometry(f"300x200+{x}+{y}")

        tk.Label(self.root, text="Imię:").pack()
        self.first_name_entry = tk.Entry(self.root)
        self.first_name_entry.pack()

        tk.Label(self.root, text="Nazwisko:").pack()
        self.last_name_entry = tk.Entry(self.root)
        self.last_name_entry.pack()

        tk.Label(self.root, text="ID rodzica:").pack()
        self.parent_id_entry = tk.Entry(self.root)
        self.parent_id_entry.pack()

        tk.Button(self.root, text="Commit", command=self.get_commit_values).pack()
        self.open_input_window()

    def get_commit_values(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        parent_id = self.parent_id_entry.get()
        print(f"Imię: {first_name}, Nazwisko: {last_name}, ID: {parent_id}")
        self.root.destroy()

    def open_input_window(self):
        self.root.mainloop()


class MainApp:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Główne Okno")
        self.clock = pygame.time.Clock()
        self.button_rect = pygame.Rect(150, 120, 100, 50)
        self.running = True

    def run(self):
        while self.running:
            self.screen.fill((30, 30, 30))
            pygame.draw.rect(self.screen, (0, 255, 0), self.button_rect)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.button_rect.collidepoint(event.pos):
                        self.open_add_person_window()
            self.clock.tick(30)
        pygame.quit()

    def get_pygame_window_position(self):
        hwnd = pygame.display.get_wm_info()['window']
        rect = RECT()
        ctypes.windll.user32.GetWindowRect(hwnd, ctypes.byref(rect))
        return rect.left, rect.top

    def open_add_person_window(self):
        x, y = self.get_pygame_window_position()
        add_person_window = AddPersonWindow(x + 50, y + 50)

if __name__ == "__main__":
    app = MainApp()
    app.run()
