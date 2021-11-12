from damka_assets.game_class import *

PUZZLE5 = [
    [0, SmallPiece(0, 1, WHITE), 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, SmallPiece(1, 4, WHITE), 0, 0, 0],
    [0, SmallPiece(2, 1, RED), 0, 0, 0, 0, 0, 0],
    [0, 0, SmallPiece(3, 2, WHITE), 0, SmallPiece(3, 4, WHITE), 0, SmallPiece(3, 6, WHITE), 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, 0, 0, 0],
    [SmallPiece(5, 0, RED), 0, SmallPiece(5, 2, RED), 0, 0, 0, 0, 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, SmallPiece(6, 5, RED), 0, 0],
    [0, 0, 0, 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE5_FIRST = [
    [0, SmallPiece(0, 1, WHITE), 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, SmallPiece(1, 4, WHITE), 0, 0, 0],
    [0, SmallPiece(2, 1, RED), 0, 0, 0, 0, 0, 0],
    [0, 0, SmallPiece(3, 2, WHITE), 0, SmallPiece(3, 4, WHITE), 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, 0, 0, SmallPiece(4, 7, WHITE)],
    [SmallPiece(5, 0, RED), 0, SmallPiece(5, 2, RED), 0, 0, 0, 0, 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, SmallPiece(6, 5, RED), 0, 0],
    [0, 0, 0, 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE5_CORRECT1 = [
    [0, SmallPiece(0, 1, WHITE), 0, 0, 0, 0, 0, 0],
    [SmallPiece(1, 0, RED), 0, 0, 0, SmallPiece(1, 4, WHITE), 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, SmallPiece(3, 2, WHITE), 0, SmallPiece(3, 4, WHITE), 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, 0, 0, SmallPiece(4, 7, WHITE)],
    [SmallPiece(5, 0, RED), 0, SmallPiece(5, 2, RED), 0, 0, 0, 0, 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, SmallPiece(6, 5, RED), 0, 0],
    [0, 0, 0, 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE5_SECOND = [
    [0, SmallPiece(0, 1, WHITE), 0, 0, 0, 0, 0, 0],
    [SmallPiece(1, 0, RED), 0, 0, 0, SmallPiece(1, 4, WHITE), 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, SmallPiece(3, 2, WHITE), 0, SmallPiece(3, 4, WHITE), 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, 0, 0, 0],
    [SmallPiece(5, 0, RED), 0, SmallPiece(5, 2, RED), 0, 0, 0, SmallPiece(5, 6, WHITE), 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, SmallPiece(6, 5, RED), 0, 0],
    [0, 0, 0, 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE5_CORRECT2 = [
    [0, SmallPiece(0, 1, WHITE), 0, 0, 0, 0, 0, 0],
    [SmallPiece(1, 0, RED), 0, 0, 0, SmallPiece(1, 4, WHITE), 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, SmallPiece(3, 2, WHITE), 0, SmallPiece(3, 4, WHITE), 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, 0, 0, SmallPiece(4, 7, RED)],
    [SmallPiece(5, 0, RED), 0, SmallPiece(5, 2, RED), 0, 0, 0, 0, 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, SmallPiece(7, 6, RED), 0]
]


puzzle5_img = pygame.transform.scale(pygame.image.load("D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzle_5.png"), (800, 800))
puzzle5_before = pygame.transform.scale(pygame.image.load("D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzle_5_before.png"), (800, 800))


P5 = (PUZZLE5, PUZZLE5_FIRST, PUZZLE5_CORRECT1, puzzle5_img, puzzle5_before)
P5_SECOND = (PUZZLE5_SECOND, PUZZLE5_CORRECT2, puzzle5_before)
