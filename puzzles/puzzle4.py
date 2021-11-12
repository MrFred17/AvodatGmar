from damka_assets.game_class import *

PUZZLE4 = [
    [0, 0, 0, 0, 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, SmallPiece(1, 2, RED), 0, SmallPiece(1, 4, WHITE), 0, SmallPiece(1, 6, WHITE), 0],
    [0, SmallPiece(2, 1, WHITE), 0, 0, 0, 0, 0, 0],
    [SmallPiece(3, 0, WHITE), 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, SmallPiece(4, 5, RED), 0, 0],
    [SmallPiece(5, 0, RED), 0, 0, 0, 0, 0, SmallPiece(5, 6, WHITE), 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, 0, 0, SmallPiece(6, 7, RED)],
    [0, 0, SmallPiece(7, 2, RED), 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE4_FIRST = [
    [0, 0, 0, 0, 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, SmallPiece(1, 2, RED), 0, SmallPiece(1, 4, WHITE), 0, SmallPiece(1, 6, WHITE), 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [SmallPiece(3, 0, WHITE), 0, SmallPiece(3, 2, WHITE), 0, 0, 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, SmallPiece(4, 5, RED), 0, 0],
    [SmallPiece(5, 0, RED), 0, 0, 0, 0, 0, SmallPiece(5, 6, WHITE), 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, 0, 0, SmallPiece(6, 7, RED)],
    [0, 0, SmallPiece(7, 2, RED), 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

queen = SmallPiece(0, 3, RED)
queen.make_queen()
PUZZLE4_CORRECT1 = [
    [0, 0, 0, queen, 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, 0, 0, SmallPiece(1, 4, WHITE), 0, SmallPiece(1, 6, WHITE), 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [SmallPiece(3, 0, WHITE), 0, SmallPiece(3, 2, WHITE), 0, 0, 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, SmallPiece(4, 5, RED), 0, 0],
    [SmallPiece(5, 0, RED), 0, 0, 0, 0, 0, SmallPiece(5, 6, WHITE), 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, 0, 0, SmallPiece(6, 7, RED)],
    [0, 0, SmallPiece(7, 2, RED), 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE4_SECOND = [
    [0, 0, 0, queen, 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, 0, 0, 0, 0, SmallPiece(1, 6, WHITE), 0],
    [0, 0, 0, 0, 0, SmallPiece(2, 5, WHITE), 0, 0],
    [SmallPiece(3, 0, WHITE), 0, SmallPiece(3, 2, WHITE), 0, 0, 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, SmallPiece(4, 5, RED), 0, 0],
    [SmallPiece(5, 0, RED), 0, 0, 0, 0, 0, SmallPiece(5, 6, WHITE), 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, 0, 0, SmallPiece(6, 7, RED)],
    [0, 0, SmallPiece(7, 2, RED), 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE4_CORRECT2 = [
    [0, 0, 0, queen, 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, 0, 0, 0, 0, SmallPiece(1, 6, WHITE), 0],
    [0, 0, 0, 0, 0, SmallPiece(2, 5, WHITE), 0, 0],
    [SmallPiece(3, 0, WHITE), 0, SmallPiece(3, 2, WHITE), 0, 0, 0, SmallPiece(3, 6, RED), 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, 0, 0, 0],
    [SmallPiece(5, 0, RED), 0, 0, 0, 0, 0, SmallPiece(5, 6, WHITE), 0],
    [0, SmallPiece(6, 1, RED), 0, 0, 0, 0, 0, SmallPiece(6, 7, RED)],
    [0, 0, SmallPiece(7, 2, RED), 0, 0, 0, SmallPiece(7, 6, RED), 0]
]

puzzle4_img = pygame.transform.scale(pygame.image.load("D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzle_4.png"), (800, 800))
puzzle4_before = pygame.transform.scale(pygame.image.load("D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzle_4_before.png"), (800, 800))


P4 = (PUZZLE4, PUZZLE4_FIRST, PUZZLE4_CORRECT1, puzzle4_img, puzzle4_before)
P4_SECOND = (PUZZLE4_SECOND, PUZZLE4_CORRECT2, puzzle4_before)
