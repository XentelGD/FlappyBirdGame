import pygame

is_clicked_before = False
is_clicked = False


def update_tools(event):
    global is_clicked, is_clicked_before


    is_clicked = False
    if event.type == pygame.MOUSEBUTTONDOWN and not is_clicked_before:
        is_clicked_before = True
        is_clicked = True

    if event.type == pygame.MOUSEBUTTONUP:
        is_clicked_before = False


def is_mouse_clicked_now():
    return is_clicked
