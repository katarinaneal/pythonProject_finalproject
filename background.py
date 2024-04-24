import pygame
from pygame.locals import QUIT
from board import Board


class Scene:
    # Setup
    pygame.init()

    def __init__(self):
        self.scene = 'main_screen'
        self.screen = pygame.display.set_mode((800, 800))
        self.mouse = pygame.mouse.get_pos()
        self.title_font = pygame.font.SysFont('Arial', 50)
        self.box_font = pygame.font.SysFont('Arial', 35)

    def start(self):
        # Game Screen
        width = 800
        height = 800

        # Colors
        white = (255, 255, 255)
        black = (0, 0, 0)
        grey = (128, 128, 128)
        dark_grey = (169, 169, 169)

        # Text
        title = self.title_font.render('Welcome to Sudoku!', True, (0, 0, 0))
        easy_text = self.box_font.render('Easy', True, black)
        medium_text = self.box_font.render('Medium', True, black)
        hard_text = self.box_font.render('Hard', True, black)

        # Screen Rendering

        self.screen.fill((255, 255, 255))
        self.mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
        if width / 4 <= self.mouse[0] <= width / 4 + 200 and height / 4 <= self.mouse[1] <= height / 4 + 50:
            pygame.draw.rect(self.screen, grey, [width / 4, height / 4, 200, 50])
        else:
            pygame.draw.rect(self.screen, dark_grey, [width / 4, height / 4, 200, 50])

        if width / 4 <= self.mouse[0] <= width / 4 + 200 and height / 4 + 75 <= self.mouse[1] <= height / 3 + 50:
            pygame.draw.rect(self.screen, grey, [width / 4, height / 4 + 75, 200, 50])
        else:
            pygame.draw.rect(self.screen, dark_grey, [width / 4, height / 4 + 75, 200, 50])

        if width / 4 <= self.mouse[0] <= width / 4 + 200 and height / 4 + 75 <= self.mouse[1] <= height / 2 + 50:
            pygame.draw.rect(self.screen, grey, [width / 4, height / 4 + 150, 200, 50])
        else:
            pygame.draw.rect(self.screen, dark_grey, [width / 4, height / 4 + 150, 200, 50])

        self.screen.blit(title, (width / 6, height / 8))
        self.screen.blit(easy_text, (width / 4 + 25, height / 4))
        self.screen.blit(medium_text, (width / 4 + 25, height / 4 + 75))
        self.screen.blit(hard_text, (width / 4 + 25, height / 4 + 150))
        pygame.display.update()

    def game_in_progress(self):
        pass

    def game_win(self):
        self.screen.fill((255, 255, 255))
        self.mouse = pygame.mouse.get_pos()
        # Game Screen
        width = 800
        height = 800
        grey = (128, 128, 128)
        dark_grey = (169, 169, 169)
        title = self.title_font.render('You Win!', True, (0, 0, 0))
        exit_text = self.box_font.render('Exit', True, (0, 0, 0))
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if width / 4 + 100 <= self.mouse[0] <= width / 4 + 300 and height / 4 + 200 <= self.mouse[1] <= height / 4 + 250:
                    pygame.quit()

        if width / 4 + 100 <= self.mouse[0] <= width / 4 + 300 and height / 4 + 200 <= self.mouse[
            1] <= height / 4 + 250:
            pygame.draw.rect(self.screen, grey, [width / 4 + 100, height / 4 + 200, 200, 50])
        else:
            pygame.draw.rect(self.screen, dark_grey, [width / 4 + 100, height / 4 + 200, 200, 50])

        self.screen.blit(title, (width / 3, height / 3))
        self.screen.blit(exit_text, (width / 4 + 125, height / 4 + 200))
        pygame.display.update()

    def game_over(self):
        self.screen.fill((255, 255, 255))
        self.mouse = pygame.mouse.get_pos()
        # Game Screen
        width = 800
        height = 800
        grey = (128, 128, 128)
        dark_grey = (169, 169, 169)
        title = self.title_font.render('Sudoku Failed', True, (0, 0, 0))
        exit_text = self.box_font.render('Restart', True, (0, 0, 0))
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
        if width / 4 + 100 <= self.mouse[0] <= width / 4 + 300 and height / 4 + 200 <= self.mouse[
            1] <= height / 4 + 250:
            pygame.draw.rect(self.screen, grey, [width / 4 + 100, height / 4 + 200, 200, 50])
        else:
            pygame.draw.rect(self.screen, dark_grey, [width / 4 + 100, height / 4 + 200, 200, 50])

        self.screen.blit(title, (width / 3 - 50, height / 3))
        self.screen.blit(exit_text, (width / 4 + 125, height / 4 + 200))
        pygame.display.update()

