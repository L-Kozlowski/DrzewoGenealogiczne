import pygame

# Inicjalizacja Pygame
pygame.init()

# Tworzenie okna
screen = pygame.display.set_mode((800, 600))  # Okno 800x600 pikseli
pygame.display.set_caption('Przykładowa gra')

# Główna pętla programu
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Zamknięcie okna
            running = False

    # Wypełnianie ekranu białym kolorem
    screen.fill((255, 255, 255))

    # Odświeżanie ekranu
    pygame.display.flip()

# Zakończenie programu
pygame.quit()
