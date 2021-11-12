from damka_assets.game_class import *

PUZZLE6 = [
    [0, 0, 0, SmallPiece(0, 3, WHITE), 0, SmallPiece(0, 5, WHITE), 0, 0],
    [SmallPiece(1, 0, WHITE), 0, 0, 0, 0, 0, SmallPiece(1, 6, WHITE), 0],
    [0, SmallPiece(2, 1, WHITE), 0, SmallPiece(2, 3, RED), 0, SmallPiece(2, 5, WHITE), 0, SmallPiece(2, 7, WHITE)],
    [0, 0, 0, 0, SmallPiece(3, 4, RED), 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, SmallPiece(4, 5, RED), 0, SmallPiece(4, 7, WHITE)],
    [SmallPiece(5, 0, RED), 0, 0, 0, 0, 0, 0, 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, SmallPiece(6, 5, RED), 0, 0],
    [0, 0, SmallPiece(7, 2, RED), 0, SmallPiece(7, 4, RED), 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE6_FIRST = [
    [0, 0, 0, SmallPiece(0, 3, WHITE), 0, SmallPiece(0, 5, WHITE), 0, 0],
    [SmallPiece(1, 0, WHITE), 0, 0, 0, 0, 0, SmallPiece(1, 6, WHITE), 0],
    [0, 0, 0, SmallPiece(2, 3, RED), 0, SmallPiece(2, 5, WHITE), 0, SmallPiece(2, 7, WHITE)],
    [SmallPiece(3, 0, WHITE), 0, 0, 0, SmallPiece(3, 4, RED), 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, SmallPiece(4, 5, RED), 0, SmallPiece(4, 7, WHITE)],
    [SmallPiece(5, 0, RED), 0, 0, 0, 0, 0, 0, 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, SmallPiece(6, 5, RED), 0, 0],
    [0, 0, SmallPiece(7, 2, RED), 0, SmallPiece(7, 4, RED), 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE6_CORRECT1 = [
    [0, 0, 0, SmallPiece(0, 3, WHITE), 0, SmallPiece(0, 5, WHITE), 0, 0],
    [SmallPiece(1, 0, WHITE), 0, 0, 0, 0, 0, SmallPiece(1, 6, WHITE), 0],
    [0, 0, 0, SmallPiece(2, 3, RED), 0, SmallPiece(2, 5, WHITE), 0, SmallPiece(2, 7, WHITE)],
    [SmallPiece(3, 0, WHITE), 0, 0, 0, SmallPiece(3, 4, RED), 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, SmallPiece(4, 5, RED), 0, SmallPiece(4, 7, WHITE)],
    [SmallPiece(5, 0, RED), 0, 0, 0, 0, 0, 0, 0],
    [0, SmallPiece(6, 1, RED), 0, SmallPiece(6, 3, RED), 0, SmallPiece(6, 5, RED), 0, 0],
    [0, 0, SmallPiece(7, 2, RED), 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE6_SECOND = [
    [0, 0, 0, SmallPiece(0, 3, WHITE), 0, SmallPiece(0, 5, WHITE), 0, 0],
    [SmallPiece(1, 0, WHITE), 0, 0, 0, 0, 0, SmallPiece(1, 6, WHITE), 0],
    [0, 0, 0, SmallPiece(2, 3, RED), 0, SmallPiece(2, 5, WHITE), 0, SmallPiece(2, 7, WHITE)],
    [SmallPiece(3, 0, WHITE), 0, 0, 0, SmallPiece(3, 4, RED), 0, 0, 0],
    [0, 0, 0, 0, 0, SmallPiece(4, 5, RED), 0, SmallPiece(4, 7, WHITE)],
    [SmallPiece(5, 0, RED), 0, 0, 0, SmallPiece(5, 4, WHITE), 0, 0, 0],
    [0, SmallPiece(6, 1, RED), 0, SmallPiece(6, 3, RED), 0, SmallPiece(6, 5, RED), 0, 0],
    [0, 0, SmallPiece(7, 2, RED), 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE6_CORRECT2 = [
    [0, 0, 0, SmallPiece(0, 3, WHITE), 0, SmallPiece(0, 5, WHITE), 0, 0],
    [SmallPiece(1, 0, WHITE), 0, 0, 0, 0, 0, SmallPiece(1, 6, WHITE), 0],
    [0, 0, 0, SmallPiece(2, 3, RED), 0, SmallPiece(2, 5, WHITE), 0, SmallPiece(2, 7, WHITE)],
    [SmallPiece(3, 0, WHITE), 0, 0, 0, SmallPiece(3, 4, RED), 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, RED), 0, SmallPiece(4, 5, RED), 0, SmallPiece(4, 7, WHITE)],
    [SmallPiece(5, 0, RED), 0, 0, 0, 0, 0, 0, 0],
    [0, SmallPiece(6, 1, RED), 0, SmallPiece(6, 3, RED), 0, 0, 0, 0],
    [0, 0, SmallPiece(7, 2, RED), 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

puzzle6_img = pygame.transform.scale(pygame.image.load("D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzle_6.png"), (800, 800))
puzzle6_before = pygame.transform.scale(pygame.image.load("D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzle_6_before.png"), (800, 800))

P6 = (PUZZLE6, PUZZLE6_FIRST, PUZZLE6_CORRECT1, puzzle6_img, puzzle6_before)
P6_SECOND = (PUZZLE6_SECOND, PUZZLE6_CORRECT2, puzzle6_before)

