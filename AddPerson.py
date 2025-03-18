import pygame

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
            if event.key == pygame.K_RETURN:
                print(self.text)
                self.text = ''
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode
            self.txt_surface = pygame.font.Font(None, 32).render(self.text, True, self.color)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 2)
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))

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
                        self.open_input_window()
            self.clock.tick(30)
        pygame.quit()

    def open_input_window(self):
        input_screen = pygame.display.set_mode((400, 300))
        pygame.display.set_caption("Formularz")
        font = pygame.font.Font(None, 32)
        labels = ["Imię:", "Nazwisko:", "ID rodzica:"]
        input_boxes = [
            InputBox(150, 50, 200, 32),
            InputBox(150, 100, 200, 32),
            InputBox(150, 150, 200, 32)
        ]
        commit_button = pygame.Rect(150, 200, 100, 40)
        running = True
        while running:
            input_screen.fill((50, 50, 50))
            for i, box in enumerate(input_boxes):
                label_surface = font.render(labels[i], True, pygame.Color('white'))
                input_screen.blit(label_surface, (50, 55 + i * 50))
                box.draw(input_screen)
            pygame.draw.rect(input_screen, (0, 255, 0), commit_button)
            commit_text = font.render("Commit", True, pygame.Color('black'))
            input_screen.blit(commit_text, (commit_button.x + 15, commit_button.y + 10))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if commit_button.collidepoint(event.pos):
                        print(f"Imię: {input_boxes[0].text}, Nazwisko: {input_boxes[1].text}, ID: {input_boxes[2].text}")
                for box in input_boxes:
                    box.handle_event(event)
            pygame.time.Clock().tick(30)
        pygame.display.set_mode((400, 300))  # Przywrócenie głównego okna


if __name__ == "__main__":
    app = MainApp()
    app.run()
