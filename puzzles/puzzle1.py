from damka_assets.game_class import *


PUZZLE1 = [
    [0, 0, 0, 0, 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, SmallPiece(1, 2, WHITE), 0, 0, 0, SmallPiece(1, 6, RED), 0],
    [0, SmallPiece(2, 1, WHITE), 0, 0, 0, 0, 0, SmallPiece(2, 7, RED)],
    [0, 0, SmallPiece(3, 2, WHITE), 0, 0, 0, 0, 0],
    [0, 0, 0, SmallPiece(4, 3, WHITE), 0, 0, 0, SmallPiece(4, 7, WHITE)],
    [0, 0, SmallPiece(5, 2, WHITE), 0, SmallPiece(5, 4, RED), 0, 0, 0],
    [0, 0, 0, SmallPiece(6, 3, RED), 0, 0, 0, SmallPiece(6, 7, WHITE)],
    [0, 0, 0, 0, SmallPiece(7, 4, RED), 0, SmallPiece(7, 6, RED), 0]
]

PUZZLE1_FIRST = [
    [0, 0, 0, 0, 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, SmallPiece(1, 2, WHITE), 0, 0, 0, SmallPiece(1, 6, RED), 0],
    [0, SmallPiece(2, 1, WHITE), 0, 0, 0, 0, 0, SmallPiece(2, 7, RED)],
    [0, 0, SmallPiece(3, 2, WHITE), 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, SmallPiece(4, 7, WHITE)],
    [0, 0, SmallPiece(5, 2, WHITE), 0, 0, 0, 0, 0],
    [0, 0, 0, SmallPiece(6, 3, RED), 0, SmallPiece(6, 5, WHITE), 0, SmallPiece(6, 7, WHITE)],
    [0, 0, 0, 0, SmallPiece(7, 4, RED), 0, SmallPiece(7, 6, RED), 0]
]

queen = SmallPiece(0, 1, RED)
queen.make_queen()
PUZZLE1_CORRECT = [
    [0, queen, 0, 0, 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, 0, 0, 0, 0, SmallPiece(1, 6, RED), 0],
    [0, SmallPiece(2, 1, WHITE), 0, 0, 0, 0, 0, SmallPiece(2, 7, RED)],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, SmallPiece(4, 7, WHITE)],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, SmallPiece(6, 5, WHITE), 0, SmallPiece(6, 7, WHITE)],
    [0, 0, 0, 0, SmallPiece(7, 4, RED), 0, SmallPiece(7, 6, RED), 0]
]

puzzle1_img = pygame.transform.scale(pygame.image.load("D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzle_1_OKOK.png"), (800, 800))
puzzle1_before = pygame.transform.scale(pygame.image.load("D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzle_1_OK.png"), (800, 800))


P1 = (PUZZLE1, PUZZLE1_FIRST, PUZZLE1_CORRECT, puzzle1_img, puzzle1_before)


# def puzzle1_play(user_id=None):
#     pygame.display.set_caption("Puzzle 1")
#     screen = pygame.display.set_mode((800, 800))
#
#     puzzle = Puzzle(screen, PUZZLE1, RED, PUZZLE1_CORRECT, PUZZLE1_FIRST)
#     game = puzzle.game
#     screen.blit(puzzle1_img, (-10, 0))
#     started_puzzle = False
#     game.started_puzzle = started_puzzle
#     clock = pygame.time.Clock()
#
#     while True:
#         clock.tick(FPS)
#
#         for event in pygame.event.get():
#
#             # user wishes to quit the application
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if is_mouse_on_button(675, 66, 100, 26):
#                     puzzles_page(user_id)
#
#                 # start puzzle
#                 if is_mouse_on_button(296, 666, 149, 42) and not started_puzzle:
#                     started_puzzle = True
#                     game.started_puzzle = started_puzzle
#                     game.board.board = deepcopy(PUZZLE1_FIRST)
#                     time.sleep(0.5)
#                     screen.blit(puzzle1_img_before, (-10, 0))
#
#                 if is_mouse_on_button(655, 260, 130, 50) and game.board.is_game_over:
#                     puzzle = Puzzle(screen, PUZZLE1, RED, PUZZLE1_CORRECT, deepcopy(PUZZLE1_FIRST))
#                     game = puzzle.game
#                     screen.blit(puzzle1_img, (-10, 0))
#                     started_puzzle = False
#                     game.started_puzzle = started_puzzle
#
#                 position = pygame.mouse.get_pos()
#                 row, col = small_get_mouse_row_col(position)
#                 game.select_piece(row, col)
#
#         # if a move was played
#         if game.board.is_game_over:
#             if game.check_move():
#                 screen.blit(big_font.render("Correct!", True, GREEN), (653, 190))
#             else:
#                 screen.blit(big_font.render("Wrong.", True, RED), (660, 190))
#                 pygame.draw.rect(screen, WHITE, (655, 260, 130, 50))
#                 screen.blit(font.render("Try Again", True, BLACK), (667, 263))
#
#         game.update_game()

