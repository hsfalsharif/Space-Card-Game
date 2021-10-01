import deck
import card
import random
import pygame
import sys
from pygame.locals import *

number_of_igniter_card = 1
number_of_fire_engine_card = 3
number_of_rocket_booster = 0
number_of_landing_gear_card = 1
number_of_RCS_thrusters_card = 0
number_of_electric_propulsion_card = 0

current_fuel = 100
current_mass = 10

pygame.init()

# Assign FPS a value
FPS = 60
main_clock = pygame.time.Clock()

# Setting up color objects
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
WHITE = (255, 255, 255)
DARKBLUE = (2, 3, 89)
REDDISH = (247, 58, 45)
# Setup a 1200x800 pixel display with caption
DISPLAYSURF = pygame.display.set_mode((1200,800))
pygame.display.set_caption("Decks To Orbit")

font = pygame.font.SysFont(None, 60)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def main_menu():
    click = False
    at_menu = True
    DISPLAYSURF.fill(BLACK)
    draw_text("Decks To Orbit!", font, WHITE, DISPLAYSURF, 420, 300)
    button_1 = pygame.Rect(475, 450, 200, 50)
    button_2 = pygame.Rect(475, 550, 200, 50)

    while at_menu:
        pygame.draw.rect(DISPLAYSURF, RED, button_1)
        draw_text("Play", font, WHITE, DISPLAYSURF, 530, 455)
        pygame.draw.rect(DISPLAYSURF, RED, button_2)
        draw_text("Quit", font, WHITE, DISPLAYSURF, 530, 555)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if button_1.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(DISPLAYSURF, BLUE, button_1)
            draw_text("Play", font, WHITE, DISPLAYSURF, 530, 455)
            if click:
                at_menu = False

        if button_2.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(DISPLAYSURF, BLUE, button_2)
            draw_text("Quit", font, WHITE, DISPLAYSURF, 530, 555)
            if click:
                pygame.quit()
                sys.exit()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        main_clock.tick(FPS)

def select_mission():
    click = False
    at_menu = True
    DISPLAYSURF.fill(GREY)
    draw_text("Select Mission", font, BLACK, DISPLAYSURF, 420, 300)
    button_1 = pygame.Rect(325, 500, 200, 50)
    button_2 = pygame.Rect(625, 500, 200, 50)

    while at_menu:
        pygame.draw.rect(DISPLAYSURF, WHITE, button_1)
        draw_text("Moon", font, BLACK, DISPLAYSURF, 370, 505)
        pygame.draw.rect(DISPLAYSURF, WHITE, button_2)
        draw_text("Mars", font, BLACK, DISPLAYSURF, 670, 505)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if button_1.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(DISPLAYSURF, BLUE, button_1)
            draw_text("Moon", font, WHITE, DISPLAYSURF, 370, 505)
            if click:
                at_menu = False

        if button_2.collidepoint((mouse_x, mouse_y)):
            pygame.draw.rect(DISPLAYSURF, BLUE, button_2)
            draw_text("Mars", font, WHITE, DISPLAYSURF, 670, 505)
            if click:
                pygame.quit()
                sys.exit()
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        main_clock.tick(FPS)

def deck_building():
    click = False
    DISPLAYSURF.fill(DARKBLUE)
    draw_text("Build Deck", font, REDDISH, DISPLAYSURF, 475, 200)
    deck_building = True
    card_1 = pygame.Rect(190, 300, 175, 300)
    card_2 = pygame.Rect(490, 300, 175, 300)
    card_3 = pygame.Rect(790, 300, 175, 300)
    number_hider = pygame.Rect(300, 50, 40, 40)
    pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_1)
    pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_2)
    pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_3)
    card_count = 0
    draw_text("Card Count: %d" % card_count, font, REDDISH, DISPLAYSURF, 50, 50)
    while deck_building:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if card_1.collidepoint((mouse_x, mouse_y)):
            if click:
                pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_1)
                pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_2)
                pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_3)
                card_count += 1
                if card_count >= 10:
                    deck_building = False
                else:
                    pygame.draw.rect(DISPLAYSURF, DARKBLUE, number_hider)
                    draw_text("Card Count: %d" % card_count, font, REDDISH, DISPLAYSURF, 50, 50)

        if card_2.collidepoint((mouse_x, mouse_y)):
            if click:
                pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_1)
                pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_2)
                pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_3)
                card_count += 1
                if card_count >= 10:
                    deck_building = False
                else:
                    pygame.draw.rect(DISPLAYSURF, DARKBLUE, number_hider)
                    draw_text("Card Count: %d" % card_count, font, REDDISH, DISPLAYSURF, 50, 50)
        if card_3.collidepoint((mouse_x, mouse_y)):
            if click:
                pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_1)
                pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_2)
                pygame.draw.rect(DISPLAYSURF, (random.randint(1,255), random.randint(1,255), random.randint(1,255)), card_3)
                card_count += 1
                if card_count >= 10:
                    deck_building = False
                else:
                    pygame.draw.rect(DISPLAYSURF, DARKBLUE, number_hider)
                    draw_text("Card Count: %d" % card_count, font, REDDISH, DISPLAYSURF, 50, 50)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        main_clock.tick(FPS)

def game_loop():
    click = False
    running = True
    DISPLAYSURF.fill(BLACK)
    card_deck = pygame.Rect(30, 475, 175, 300)
    for i in range(100):
        pygame.draw.circle(DISPLAYSURF, GREY, (random.randint(1,1200), random.randint(1,800)), 2)
    pygame.draw.circle(DISPLAYSURF, GREY, (600, 100), 50)
    pygame.draw.rect(DISPLAYSURF, DARKBLUE, card_deck)
    draw_text("Deck", font, REDDISH, DISPLAYSURF, 65, 600)

    while running:
        if click:
            DISPLAYSURF.fill(BLACK)
            for i in range(100):
                pygame.draw.circle(DISPLAYSURF, GREY, (random.randint(1,1200), random.randint(1,800)), 2)
            pygame.draw.circle(DISPLAYSURF, GREY, (600, 100), 50)
            pygame.draw.rect(DISPLAYSURF, DARKBLUE, card_deck)
            draw_text("Deck", font, REDDISH, DISPLAYSURF, 65, 600)
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        main_clock.tick(FPS)

main_menu()
select_mission()
deck_building()
game_loop()
pygame.quit()
sys.exit()
#igniter_card = card.Card('igniter', empty_func())
#fire_engine_card = card.Card('fire_engine', empty_func())
#solid_rocket_booster_card = card.Card('solid_rocket_booster', empty_func())
#landing_gear_card = card.Card('landing_gear', empty_func())
#rcs_thrusters = card.Card('rcs_thrusters', empty_func())
#thruster_gimbel_card = card.Card('thruster_gimbel', empty_func())
#electric_propulsion_card = card.Card('electric_propulsion', empty_func())


#list_of_cards = [
#    igniter_card,
#    fire_engine_card,
#    solid_rocket_booster_card,
#    landing_gear_card,
#    rcs_thrusters,
#    thruster_gimbel_card,
#    electric_propulsion_card,
#]

#new_object = random.choice(list_of_cards)
#print(new_object.name)