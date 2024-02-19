import pygame

import settings
import tools


def draw_game_over_button(window, icon: pygame.surface.Surface):
    final_icon = pygame.transform.scale(icon, (250, 150))

    mx = pygame.mouse.get_pos()[0]
    my = pygame.mouse.get_pos()[1]

    x = settings.WIDTH / 2 - 125
    y = settings.HEIGHT / 2 - 75

    if x < mx < x + final_icon.get_rect()[2] and y < my < y + final_icon.get_rect()[3]:
        final_icon.fill((20, 20, 20), special_flags=pygame.BLEND_RGB_ADD)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
    else:
        final_icon.fill((0, 0, 0), special_flags=pygame.BLEND_RGB_ADD)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    window.blit(final_icon, (x, y))

    if x < mx < x + final_icon.get_rect()[2] and y < my < y + final_icon.get_rect()[3]:
        return tools.is_clicked

    return False
