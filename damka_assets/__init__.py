import pygame
pygame.init()

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HAKI = (255, 206, 158)
RED = (180, 0, 3)
BROWN = (209, 139, 71)
BLUE = (26, 136, 233)
PURPLE = (145, 0, 255)
GREEN = (0, 195, 0)

# application constants
ROWS, COLS = 8, 8
WIDTH, HEIGHT = 800, 800
FPS = 60
SQUARE_SIZE = WIDTH // COLS  # 100 X 100 square
SMALL_SQUARE_SIZE = SQUARE_SIZE * 0.8
SQUARE_MIDDLE = SQUARE_SIZE // 2
SMALL_SQUARE_MIDDLE = SQUARE_MIDDLE * 0.8
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # setting the app window

# single player button
x_from1 = 124
y_from = 492
width = 230
height = 111
# 2 player button
x_from2 = 450

# queen stuff
QUEEN_WIDTH = 60
SMALL_QUEEN_WIDTH = int(QUEEN_WIDTH * 0.8)
QUEEN_HEIGHT = 43
SMALL_QUEEN_HEIGHT = int(QUEEN_HEIGHT * 0.8)
white_q = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/WHITE_Q.png')
black_q = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/BLACK_Q.png')
WHITE_QUEEN = pygame.transform.scale(white_q, (QUEEN_WIDTH, QUEEN_HEIGHT))
SMALL_WHITE_QUEEN = pygame.transform.scale(white_q, (SMALL_QUEEN_WIDTH, SMALL_QUEEN_HEIGHT))
BLACK_QUEEN = pygame.transform.scale(black_q, (QUEEN_WIDTH, QUEEN_HEIGHT))
SMALL_BLACK_QUEEN = pygame.transform.scale(black_q, (SMALL_QUEEN_WIDTH, SMALL_QUEEN_HEIGHT))


# images
bg = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/bg1.png'), (HEIGHT, WIDTH))
quit_button = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/back_to_mm.png'), (30, 30))
game_over_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/game_over.png'), (779, 363))
select_diff = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/diff.png'), (364, 437))
login_page_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/test_login_page.png'), (750, 750))
signup_page_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/signup_page.png'), (775, 775))
logout_msg = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/logout_msg.png'), (635, 241))
stats_page_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/stats.png'), (800, 800))
login_first_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/log_in_first.png'), (635, 241))
profile_page_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile.png'), (820, 820))
log_in_for_profile = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/log_in_for_profile.png'), (635, 241))
help_page_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/help_page.png'), (800, 800))
back_show_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/back_show.png'), (180, 50))
choose_profile_photo = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile_selection.png'), (800, 800))
leaderboard_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/leaderboard.png'), (800, 800))
puzzles_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/puzzles_page.png'), (800, 800))
log_in_for_puzzles = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/log_in_puzzles.png'), (635, 241))
lock_puzzle_img = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/lock_puzzle_img.png'), (117, 117))

# profile images
default_profile_photo = pygame.transform.scale(pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/default_profile_photo.png'), (90, 85))

meg = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/1-meg.png')
jerry = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/2-jerry.png')
stewie = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/3-stewie.png')
bart = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/4-bart.png')
homer = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/5-homer.png')
patrick = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/6-patrick.png')
brian = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/7-brian.png')
isabelle = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/8-isabelle.png')
perry = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/9-perry.png')
peter = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/10-peter.png')
rick = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/11-rick.png')
spongebob = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/profile pictures/12-spongebob.png')
profile_photos = [meg, jerry, stewie, bart, homer, patrick, brian, isabelle, perry, peter, rick, spongebob]
for i in range(len(profile_photos)):
    profile_photos[i] = pygame.transform.scale(profile_photos[i], (196, 185))

# mouse stuff
LEFT_CLICK = 1
RIGHT_CLICK = 3

# arrow stuff
arrow_right = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/blue_arrow.png')
arrow_left = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/blue_arrow1.png')
arrow_down_right = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/blue_arrow2.png')
arrow_down_left = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/blue_arrow3.png')
big_arrow_right = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/bigarrow_right.png')
big_arrow_left = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/bigarrow_left.png')
big_arrow_down_right = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/bigarrow_down_right.png')
big_arrow_down_left = pygame.image.load('D:/Users/nadav/PycharmProjects/AVODAT_GMAR/media/bigarrow_down_left.png')


# font
font = pygame.font.SysFont("Arial", 30)
small_font = pygame.font.SysFont("Arial", 22)
big_font = pygame.font.SysFont("Arial", 45)

