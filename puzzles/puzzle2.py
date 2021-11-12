from damka_assets.game_class import *

PUZZLE2 = [
    [0, 0, 0, SmallPiece(0, 3, WHITE), 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, 0, 0, SmallPiece(1, 4, WHITE), 0, 0, 0],
    [0, SmallPiece(2, 1, RED), 0, SmallPiece(2, 3, WHITE), 0, 0, 0, SmallPiece(2, 7, WHITE)],
    [0, 0, SmallPiece(3, 2, RED), 0, 0, 0, SmallPiece(3, 6, RED), 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, SmallPiece(5, 4, RED), 0, SmallPiece(5, 6, WHITE), 0],
    [0, 0, 0, 0, 0, SmallPiece(6, 5, RED), 0, 0],
    [0, 0, SmallPiece(7, 2, RED), 0, SmallPiece(7, 4, RED), 0, 0, 0]
]

PUZZLE2_FIRST = [
    [0, 0, 0, SmallPiece(0, 3, WHITE), 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, 0, 0, SmallPiece(1, 4, WHITE), 0, 0, 0],
    [0, SmallPiece(2, 1, RED), 0, SmallPiece(2, 3, WHITE), 0, 0, 0, 0],
    [0, 0, SmallPiece(3, 2, RED), 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, SmallPiece(5, 6, WHITE), 0],
    [0, 0, 0, SmallPiece(6, 3, WHITE), 0, SmallPiece(6, 5, RED), 0, 0],
    [0, 0, SmallPiece(7, 2, RED), 0, SmallPiece(7, 4, RED), 0, 0, 0]
]

PUZZLE2_CORRECT = [
    [0, 0, 0, SmallPiece(0, 3, WHITE), 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, 0, 0, SmallPiece(1, 4, WHITE), 0, 0, 0],
    [0, SmallPiece(2, 1, RED), 0, SmallPiece(2, 3, WHITE), 0, 0, 0, 0],
    [0, 0, SmallPiece(3, 2, RED), 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, SmallPiece(4, 7, RED)],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, SmallPiece(6, 3, WHITE), 0, 0, 0, 0],
    [0, 0, SmallPiece(7, 2, RED), 0, SmallPiece(7, 4, RED), 0, 0, 0]
]

PUZZLE2_SECOND = [
    [0, 0, 0, SmallPiece(0, 3, WHITE), 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, 0, 0, SmallPiece(1, 4, WHITE), 0, 0, 0],
    [0, SmallPiece(2, 1, RED), 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, SmallPiece(4, 1, WHITE), 0, 0, 0, 0, 0, SmallPiece(4, 7, RED)],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, SmallPiece(6, 3, WHITE), 0, 0, 0, 0],
    [0, 0, SmallPiece(7, 2, RED), 0, SmallPiece(7, 4, RED), 0, 0, 0]
]

PUZZLE2_CORRECT2 = [
    [0, 0, 0, SmallPiece(0, 3, WHITE), 0, SmallPiece(0, 5, WHITE), 0, 0],
    [0, 0, 0, 0, SmallPiece(1, 4, WHITE), 0, 0, 0],
    [0, SmallPiece(2, 1, RED), 0, 0, 0, 0, 0, 0],
    [SmallPiece(3, 0, RED), 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, SmallPiece(4, 7, RED)],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, SmallPiece(7, 2, RED), 0, 0, 0, 0, 0]
]


puzzle2_img = pygame.transform.scale(pygame.image.load("D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzle_1.png"), (800, 800))
puzzle2_before = pygame.transform.scale(pygame.image.load("D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzle_2_OK.png"), (800, 800))


P2 = (PUZZLE2, PUZZLE2_FIRST, PUZZLE2_CORRECT, puzzle2_img, puzzle2_before)
P2_SECOND = (PUZZLE2_SECOND, PUZZLE2_CORRECT2, puzzle2_before)


# def puzzle2_play(user_id=None):
#     pygame.display.set_caption("Puzzle 2")
#     screen = pygame.display.set_mode((800, 800))
#
#     puzzle = Puzzle(screen, PUZZLE2, RED, PUZZLE2_CORRECT, PUZZLE2_FIRST)
#     game = puzzle.game
#     screen.blit(puzzle2_img, (-10, 0))
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
#                     game.board.board = deepcopy(PUZZLE2_FIRST)
#                     time.sleep(0.5)
#                     screen.blit(puzzle2_before, (-10, 0))
#
#                 if is_mouse_on_button(655, 260, 130, 50) and game.board.is_game_over:
#                     puzzle = Puzzle(screen, PUZZLE2, RED, PUZZLE2_CORRECT, deepcopy(PUZZLE2_FIRST))
#                     game = puzzle.game
#                     screen.blit(puzzle2_img, (-10, 0))
#                     started_puzzle = False
#                     game.started_puzzle = started_puzzle
#
#                 position = pygame.mouse.get_pos()
#                 row, col = small_get_mouse_row_col(position)
#                 game.select_piece(row, col)
#
#         # if a move was played
#         if game.board.is_game_over:
#             if isinstance(game.board.board[0][1], Piece):
#                 if game.board.board[0][1].queen:
#                     game.board.board = PUZZLE2_CORRECT
#                     screen.blit(big_font.render("Correct!", True, GREEN), (653, 190))
#             else:
#                 screen.blit(big_font.render("Wrong.", True, RED), (660, 190))
#                 pygame.draw.rect(screen, WHITE, (655, 260, 130, 50))
#                 screen.blit(font.render("Try Again", True, BLACK), (667, 263))
#
#         game.update_game()


