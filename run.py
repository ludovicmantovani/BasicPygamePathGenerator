import pygame
from pygame.locals import *
from pprint import pprint
import random

MULTIPLE = 2

HEIGHT = 200 * MULTIPLE
WIDTH = 200 * MULTIPLE

CEL_BY_LINE = 100 * MULTIPLE
CEL_BY_ROW = 100 * MULTIPLE

CEL_L_SIZE = WIDTH / CEL_BY_LINE
CEL_R_SIZE = HEIGHT / CEL_BY_ROW

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 205)


def count(map_data, pos):
    x, y = pos
    count = 0

    if map_data[y][x - 1]:
        count = count + 1
    if map_data[y - 1][x]:
        count = count + 1
    if map_data[y][x + 1]:
        count = count + 1
    if map_data[y + 1][x]:
        count = count + 1

    return count


def basic_generation(map_data):
    history = list()
    x = random.randint(0, len(map_data[0]) - 1)
    y = random.randint(0, len(map_data) - 1)
    nb_empty = 0
    fin = False
    while not fin:
        history.append((x, y))
        if map_data[y][x] is False:
            nb_empty = nb_empty + 1
        map_data[y][x] = True
        delta_x, delta_y = 0, 0
        delta_x = random.randint(-1, 1)
        delta_y = random.randint(-1, 1)

        if random.randint(1, 100) > 50:
            x = x + delta_x
        else:
            y = y + delta_y

        if x < 0 or x > len(map_data[0]) - 1 or y < 0 or y > len(map_data) - 1:
            fin = True
    print(nb_empty)
    return history


def vertical_generation(map_data):
    history = list()
    x = 0
    y = random.randint(0, len(map_data) - 1)
    nb_empty = 0
    fin = False
    while not fin:
        history.append((x, y))
        if map_data[y][x] is False:
            nb_empty = nb_empty + 1
        map_data[y][x] = True
        delta_x, delta_y = 0, 0
        delta_x = random.randint(0, 1)
        delta_y = random.randint(-1, 1)

        if random.randint(1, 100) > 50:
            x = x + delta_x
        else:
            y = y + delta_y

        if x < 0 or x > len(map_data[0]) - 1 or y < 0 or y > len(map_data) - 1:
            fin = True
    print(nb_empty)
    return history


def horizontal_generation(map_data):
    history = list()
    x = random.randint(0, len(map_data[0]) - 1)
    y = 0
    nb_empty = 0
    fin = False
    while not fin:
        history.append((x, y))
        if map_data[y][x] is False:
            nb_empty = nb_empty + 1
        map_data[y][x] = True
        delta_x, delta_y = 0, 0
        delta_x = random.randint(-1, 1)
        delta_y = random.randint(0, 1)

        if random.randint(1, 100) > 50:
            x = x + delta_x
        else:
            y = y + delta_y

        if x < 0 or x > len(map_data[0]) - 1 or y < 0 or y > len(map_data) - 1:
            fin = True
    print(nb_empty)
    return history


def generate_map(map_data):

    horizontal_generation(map_data)
    horizontal_generation(map_data)
    vertical_generation(map_data)
    vertical_generation(map_data)
    basic_generation(map_data)

    return


def initialise_map():
    map_data = list()
    for y in range(CEL_BY_ROW):
        line = list()
        for x in range(CEL_BY_LINE):
            line.append(False)
        map_data.append(line)
    return map_data


def display_map(surface, map_data):
    for y in range(0, len(map_data)):
        for x in range(0, len(map_data[y])):
            color = BLACK
            if map_data[y][x]:
                color = WHITE
            pygame.draw.rect(
                surface,
                color,
                (
                    y * CEL_R_SIZE,
                    x * CEL_L_SIZE,
                    CEL_R_SIZE,
                    CEL_L_SIZE
                )
            )
    pygame.display.flip()


def main():
    map_data = initialise_map()
    generate_map(map_data)
    # pprint(map_data)
    pygame.init()
    pygame.display.set_caption("Générateur")
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    running = True

    while running:
        display_map(screen, map_data)
        # genereMap(map_data)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    map_data = initialise_map()
                    generate_map(map_data)


if __name__ == '__main__':
    main()
