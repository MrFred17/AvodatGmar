from damka_assets import *
import pygame
import SQL
import time
import datetime
from math import radians, sin, cos


class GameStats:

    def __init__(self, ai_diff, user_id):
        self.user_id = user_id
        self.won = 0  # In MySQL: 0 = False, 1 = True  ("TinyInt")
        self.ai_diff = ai_diff
        self.start_time = 0
        self.total_time = ''
        self.total_moves = 0

    def start_timer(self):
        self.start_time = time.time()

    def end_timer(self):
        # returns total game time - "hh:mm:ss"
        self.total_time = str(datetime.timedelta(seconds=time.time() - self.start_time))

    def assign_winner(self, winner):
        if winner == RED:
            self.won = 1

    def insert_stats_to_database(self):
        insert_formula = "INSERT INTO games (userID, won, difficulty, gtime, total_moves) VALUES (%s, %s, %s, %s, %s);"
        SQL.mycursor.execute(insert_formula, (self.user_id, self.won, self.ai_diff, self.total_time, self.total_moves))
        SQL.mydb.commit()


def get_arrow_pos(start_square):
    row, col = start_square
    x = int(str(col)+str("45"))
    y = int(str(row-1)+str("45"))
    return x, y


def draw_arrow(start, end, start_square):
    big_arrow = False
    xf, yf = start
    xt, yt = end
    x, y = get_arrow_pos(start_square)
    if abs(yf - yt) > 175:  # check if it's a big arrow
        big_arrow = True
        this_arrow = [big_arrow_right, (x + 10, y - 100)]
    else:
        this_arrow = [arrow_right, (x, y)]

    if yf > yt:  # arrow up (as red)
        if xt < xf:  # arrow to the left
            this_arrow[0] = arrow_left
            this_arrow[1] = (x - 100, y)
            if big_arrow:
                this_arrow[0] = big_arrow_left
                this_arrow[1] = (x - 200, y - 100)

    else:  # arrow down (as white)
        if xt > xf:  # down right
            this_arrow[0] = arrow_down_right
            if big_arrow:
                this_arrow[0] = big_arrow_down_right
            this_arrow[1] = (x, y + 100)
        else:  # down left
            this_arrow[0] = arrow_down_left
            this_arrow[1] = (x - 100, y + 100)
            if big_arrow:
                this_arrow[0] = big_arrow_down_left
                this_arrow[1] = (x - 200, y + 100)

    return this_arrow


def is_mouse_on_button(xfrom, yfrom, width1, height1):
    x, y = pygame.mouse.get_pos()
    if (xfrom < x < xfrom + width1) and (yfrom < y < yfrom + height1):
        return True
    return False


def get_mouse_row_col(position):
    # get the (row, col) values based on mouse position
    x, y = position
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE

    return row, col


def small_get_mouse_row_col(position):
    # get the (row, col) values based on mouse position
    x, y = position
    row = y // SMALL_SQUARE_SIZE
    col = x // SMALL_SQUARE_SIZE

    return round(row), round(col)


def opposite_color(color):
    if color == RED:
        return WHITE
    return RED


def check_if_exists(user_info, username_only):
    # checks if user exists in the database
    # user_info = (username, password)
    # username_only = bool: will check only if the username exists
    # if exists: the user id
    # if not: -1
    SQL.mycursor.execute("SELECT * FROM users")
    for row in SQL.mycursor.fetchall():
        if (row[1], row[2]) == user_info:
            return row[0]
        if username_only and row[1] == user_info[0]:
            return row[0]

    return -1


def get_all_stats(user_id):
    # (games, totals, win%, times, avg_moves)
    SQL.mycursor.execute("SELECT * FROM games WHERE userID = " + str(user_id))
    data = SQL.mycursor.fetchall()

    # games: [(easy_lost, easy_won), (medium_lost,...) ... ()]
    games = [[0, 0], [0, 0], [0, 0]]
    totals = [0, 0, 0]  # total, total lost, total won
    for game in data:
        # easy: 2, medium: 3, hard: 4
        games[game[2]-2][game[1]] += 1   # games[difficulty - 3][lost / won]
        totals[0] += 1
        totals[game[1]+1] += 1

    if len(data) < 1:
        return games, totals, None, None, None

    try:
        p = totals[2] / totals[0]
        win_p = str(round(100 * p, 1))
    except ZeroDivisionError:
        win_p = "0"

    # times: [longest, shortest]
    total_moves = 0
    longest = shortest = data[0][3]
    for game in data:
        total_moves += game[4]
        if game[3] > longest:
            longest = game[3]
        elif game[3] < shortest:
            shortest = game[3]

    times = (longest, shortest)

    return games, totals, win_p, times, round(total_moves / len(data), 1)


def draw_arc(display, start_angle, end_angle, distance, pos, color, thickness=1):
    if start_angle > end_angle:
        theta = end_angle
        bigger = start_angle
    else:
        theta = start_angle
        bigger = end_angle

    while theta < bigger:
        for t in range(thickness):
            x = round((cos(radians(theta)) * (distance - t)) + pos[0])
            y = round((-sin(radians(theta)) * (distance - t)) + pos[1])
            display.set_at((x, y), color)
            theta += 0.01


def blank():
    d = pygame.display.set_mode((800, 800))
    d.fill(BLACK)
    d.blit(back_show_img, (27, 230))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        total = 30
        wins = 10
        losses = total - wins

        end_angle = (wins / total) * 360

        # draw_arc(d, 0, end_angle, 100, (200, 200), RED, 8)
        # draw_arc(d, end_angle, 360, 100, (200, 200), GREEN, 8)

        pygame.display.update()


def lock_puzzles(puzzle_level, screen):
    if puzzle_level < 1:
        screen.blit(lock_puzzle_img, (337, 280))
    if puzzle_level < 2:
        screen.blit(lock_puzzle_img, (578, 280))
    if puzzle_level < 3:
        screen.blit(lock_puzzle_img, (92, 508))
    if puzzle_level < 4:
        screen.blit(lock_puzzle_img, (336, 507))
    if puzzle_level < 5:
        screen.blit(lock_puzzle_img, (578, 507))
    if puzzle_level == 6:
        screen.blit(big_font.render(
            "Congratulations, You Finished All Puzzles!", True, WHITE), (42, 675))

