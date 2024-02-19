import random

import pygame

import ui
from bird import *
from object import *
from settings import *
from tools import *
from column import *

# pygame initializing

pygame.init()

# variables
running = True
event = None
bird = Bird(BIRD_START_X, BIRD_START_Y, 80, 80, pygame.image.load("res/img/bird.png"))
background = Object(0, 0, WIDTH, HEIGHT, pygame.image.load("res/img/bg.png"))
clock = pygame.time.Clock()
columns = []
tick = 0
is_game_over = False
score_font = pygame.font.Font("res/fonts/score.ttf", 50)
score = 0
score_text = score_font.render(str(score), 1, (255, 255, 255), )

# window creating
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(TITLE)
pygame.display.set_icon(pygame.image.load("res/img/bird.png"))


def draw():

    score_text = score_font.render(str(score), 1, (255, 255, 255))


    background.draw(window, clock)
    bird.draw(window, clock)
    for column in columns:
        if column is not None:
            column.draw(window, clock)

    if is_game_over:
        if ui.draw_game_over_button(window, pygame.image.load("res/img/restart.png")):
            restart()

    pygame.draw.rect(window, (0, 0, 0), (WIDTH / 2 - score_text.get_rect()[2] / 2 - 3, 100, score_text.get_rect()[2] + 3, score_text.get_rect()[3]), 0, 3)
    window.blit(score_text, (WIDTH / 2 - score_text.get_rect()[2] / 2, 100))
    ...


def restart():
    global bird, background, clock, columns, is_game_over, score

    is_game_over = False
    score = 0

    bird = Bird(BIRD_START_X, BIRD_START_Y, 80, 80, pygame.image.load("res/img/bird.png"))
    background = Object(0, 0, WIDTH, HEIGHT, pygame.image.load("res/img/bg.png"))
    clock = pygame.time.Clock()
    columns = []


def logic_update():
    global is_game_over, score
    if is_mouse_clicked_now():
        bird.jump(BIRD_JUMP_SIZE)
    i = 0
    for column in columns:
        if column is not None:
            if column.collide_rect(bird.hitbox):
                is_game_over = True
            if column.x < -100:
                columns[i] = None
            if column.x < BIRD_START_X and column.can_give_score:
                score += 1
                column.can_give_score = False
        i += 1
    background.update(window, clock)
    bird.update(window, clock)
    for column in columns:
        if column is not None:
            column.update(window, clock)
    ...


while running:

    clock.tick(FPS)

    for current_event in pygame.event.get():
        if current_event.type == pygame.QUIT:
            running = False
        else:
            event = current_event

    window.fill(clear_color)

    delta_time = 0
    try:
        delta_time = 120 / clock.get_fps()
    except:
        ...

    if not is_game_over:
        tick += TICK_SPEED * delta_time

        if tick > 10:
            tick = 0
            columns.append(
                Column(WIDTH + 5, random.randint(-200, 200), 100, HEIGHT, pygame.image.load("res/img/column_up.png"),
                       pygame.image.load("res/img/column_down.png")))


        logic_update()
    update_tools(event)
    draw()

    pygame.display.flip()

exit()
