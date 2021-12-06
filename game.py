import SQL
from damka_assets.game_class import *
from AI import *
from copy import deepcopy
from damka_assets.functions import lock_puzzles
from puzzles import Puzzle
from puzzles.puzzle1 import P1
from puzzles.puzzle2 import P2, P2_SECOND
from puzzles.puzzle3 import P3, P3_SECOND
from puzzles.puzzle4 import P4, P4_SECOND
from puzzles.puzzle5 import P5, P5_SECOND
from puzzles.puzzle6 import P6, P6_SECOND

pygame.init()


def select_difficulty():
    pygame.display.set_caption("Select Difficulty")
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    window.blit(select_diff, (218, 181))

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_on_button(220, 186, 359, 126):
                    return 2
                if is_mouse_on_button(220, 337, 359, 126):
                    return 3
                if is_mouse_on_button(221, 488, 359, 126):
                    return 4

        pygame.display.update()
    pygame.quit()


def main_menu(user_id=None):
    user = " - Hello, Guest"
    if user_id:
        SQL.mycursor.execute("SELECT username FROM users WHERE ID = "+str(user_id))
        username = SQL.mycursor.fetchone()[0]
        user = " - Welcome Back, " + username
    pygame.display.set_caption("Main Menu"+user)
    menu = pygame.display.set_mode((WIDTH, HEIGHT))
    menu.blit(bg, (12, 0))

    run = True
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                # print(pygame.mouse.get_pos())

                # login button
                if is_mouse_on_button(503, 712, 80, 70):
                    if not user_id:
                        login_page()
                    else:
                        are_you_sure_logout(user_id)

                # puzzles
                if is_mouse_on_button(609, 714, 61, 68):
                    if user_id:
                        puzzles_page(user_id)
                    else:
                        log_in_first_puzzles()

                # stats
                if is_mouse_on_button(325, 718, 60, 60):
                    if user_id:
                        stats_page(user_id)
                    else:
                        log_in_first_stats()
                # profile
                if is_mouse_on_button(412, 708, 58, 71):
                    if user_id:
                        profile_page(user_id)
                    else:
                        log_in_first_profile()
                # help
                if is_mouse_on_button(227, 709, 59, 69):
                    help_page(user_id)
                # single player
                if is_mouse_on_button(x_from1, y_from, width, height):
                    depth = select_difficulty()
                    start_game(True, depth, user_id)
                    run = False
                # 2 players
                if is_mouse_on_button(x_from2, y_from, width, height):
                    start_game()
                    run = False
                # leaderboard
                if is_mouse_on_button(145, 711, 57, 65):
                    leaderboard_page(user_id, back_to_mm=True)

        pygame.display.update()

    pygame.quit()


def start_game(with_ai=False, ai_depth=2, user_id=None):
    pygame.display.set_caption("Checkers - TwoPlayer Mode")  # window caption
    if with_ai:
        pygame.display.set_caption("Checkers - SinglePlayer Mode")
    game = Game(WIN, ai_depth, user_id)
    clock = pygame.time.Clock()
    start = start_square = 0
    arrows_info = []
    run = True
    game_finished, arrow, count_stats, toggled = False, False, False, False
    if user_id:
        count_stats = True

    moves = 0
    draw_accepted, draw_offered, viewing_board = False, False, False

    while run:
        clock.tick(FPS)

        # # make it play against itself
        # if with_ai and not game_finished:
        #     search_object = SearchTree(ai_depth, WHITE)
        #     if game.turn == RED:
        #         search_object.player_color = RED
        #
        #     move = search_object.find_optimal_move(game.board)
        #     game.ai_move(move)

        # AI
        if with_ai and game.turn == WHITE and not game.board.check_win():
            search_object = SearchTree(ai_depth, WHITE)
            ai_move = search_object.find_optimal_move(game.board)
            game.ai_move(ai_move)
            moves += 2

        for event in pygame.event.get():

            # user wishes to quit the application
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT_CLICK:
                # print(pygame.mouse.get_pos())
                arrow = False
                arrows_info = []
                position = pygame.mouse.get_pos()
                row, col = get_mouse_row_col(position)
                game.select_piece(row, col)

                # for draw offer
                if game.board.is_draw_offer_visible:
                    # accept
                    if is_mouse_on_button(205, 370, 100, 70):
                        draw_accepted = True
                        game.board.is_draw = True
                        game.board.is_draw_offer_visible = False
                        game.board.toggle_game_over_msg()

                    # decline
                    if is_mouse_on_button(495, 370, 100, 70):
                        game.board.toggle_draw_offer()

                    # view board
                    if is_mouse_on_button(350, 420, 105, 40):
                        viewing_board = True
                        game.board.toggle_draw_offer()
                        game.board.is_draw = True

                # while viewing board, user clicks "back"
                if viewing_board and is_mouse_on_button(37, 227, 125, 40):
                    viewing_board = False
                    game.board.is_draw = False
                    game.board.toggle_draw_offer()

                # user clicked on "quit game" icon
                if is_mouse_on_button(0, 0, 30, 30) and not game.board.is_error_msg_visible and not game_finished:
                    game.board.toggle_error_visibility()

                # user wished to quit
                if is_mouse_on_button(205, 370, 95, 65) and game.board.is_error_msg_visible:
                    main_menu(user_id)

                # user canceled and won't quit
                if is_mouse_on_button(495, 370, 95, 65) and game.board.is_error_msg_visible:
                    game.board.toggle_error_visibility()

                # after the game is over, play again or back to main menu?
                if game.board.is_win_msg_visible:
                    moves = 0
                    game_finished = True
                    # play again:
                    if is_mouse_on_button(169, 467, 178, 47):
                        game.reset_game(ai_depth, user_id)
                        game_finished = False
                        draw_offered, draw_accepted = False, False
                        toggled = False
                        game.board.is_draw_offer_visible = False
                    # back to main menu:
                    if is_mouse_on_button(450, 468, 178, 47):
                        main_menu(user_id)
                # show board:
                if is_mouse_on_button(27, 230, 135, 40) and game_finished:
                    game.board.toggle_game_over_msg()

            # arrows
            if not game.board.is_win_msg_visible:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == RIGHT_CLICK:
                    start = pygame.mouse.get_pos()
                    start_square = get_mouse_row_col(start)
                if event.type == pygame.MOUSEBUTTONUP and event.button == RIGHT_CLICK:
                    arrow = True
                    end = pygame.mouse.get_pos()

                    this_arrow = draw_arrow(start, end, start_square)
                    arrows_info.append(this_arrow)

        # draw offer
        red, white = game.board.red_left, game.board.white_left
        red_qu, white_qu = game.board.red_queens, game.board.white_queens
        if moves > 130 or ((red == red_qu and white == white_qu) and (abs(red_qu - white_qu < 2))):
            if not draw_accepted and not draw_offered:
                game.board.is_draw_offer_visible = True
                draw_offered = True

        winner = game.board.check_win()
        if winner:
            if not game_finished and count_stats:
                game.stats.end_timer()
                game.stats.assign_winner(winner)
                if not draw_accepted:
                    game.stats.insert_stats_to_database()
            if not toggled:
                game.board.toggle_game_over_msg()
                toggled = True
            game_finished = True

        if arrow:
            game.update_game(arrows_info)
        else:
            game.update_game()

    pygame.quit()


def are_you_sure_logout(user_id, back_to_profile=False):
    pygame.display.set_caption("Log Out")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.blit(logout_msg, (85, 220))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # log out
                if is_mouse_on_button(286, 324, 232, 59):
                    main_menu()
                # cancel
                if is_mouse_on_button(362, 419, 83, 13):
                    if not back_to_profile:
                        main_menu(user_id)
                    else:
                        profile_page(user_id)

        pygame.display.update()
        clock.tick(60)


def log_in_first_stats():
    pygame.display.set_caption("Statistics")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.blit(login_first_img, (85, 220))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # log in
                if is_mouse_on_button(286, 324, 232, 59):
                    login_page(True)
                # cancel
                if is_mouse_on_button(362, 419, 83, 13):
                    main_menu()

        pygame.display.update()
        clock.tick(60)


def log_in_first_profile():
    pygame.display.set_caption("Statistics")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.blit(log_in_for_profile, (85, 220))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # log in
                if is_mouse_on_button(286, 324, 232, 59):
                    login_page(back_to_profile=True)
                # cancel
                if is_mouse_on_button(362, 419, 83, 13):
                    main_menu()

        pygame.display.update()
        clock.tick(60)


def help_page(user_id=None):
    pygame.display.set_caption("Help")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.blit(help_page_img, (-10, -17))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # back to mm
                if is_mouse_on_button(27, 36, 73, 20):
                    main_menu(user_id)

        pygame.display.update()
        clock.tick(60)


def choose_profile_photo_page(user_id=None):
    pygame.display.set_caption("Choose Profile Photo")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.blit(choose_profile_photo, (-20, -20))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # back to profile
                if is_mouse_on_button(25, 50, 56, 22):
                    profile_page(user_id)

                # 1-meg
                if is_mouse_on_button(80, 211, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 0 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 2-jerry
                if is_mouse_on_button(260, 211, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 1 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 3-stewie
                if is_mouse_on_button(438, 211, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 2 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 4-bart
                if is_mouse_on_button(614, 211, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 3 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 5-homer
                if is_mouse_on_button(80, 407, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 4 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 6-patrick
                if is_mouse_on_button(253, 407, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 5 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 7-brian
                if is_mouse_on_button(433, 407, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 6 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 8-isabelle
                if is_mouse_on_button(612, 407, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 7 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 9-perry
                if is_mouse_on_button(80, 588, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 8 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 10-peter
                if is_mouse_on_button(253, 588, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 9 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 11-rick
                if is_mouse_on_button(433, 588, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 10 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)
                # 12-spongebob
                if is_mouse_on_button(612, 588, 105, 100):
                    SQL.mycursor.execute("UPDATE users SET profile_photo = 11 WHERE ID = " + str(user_id) + ";")
                    SQL.mydb.commit()
                    profile_page(user_id)

        pygame.display.update()
        clock.tick(60)


def leaderboard_page(user_id=None, back_to_mm=False):
    pygame.display.set_caption("Leaderboard")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.blit(leaderboard_img, (-11.5, -11))

    # [(user_id, username, photo), ...]
    SQL.mycursor.execute("SELECT ID, username, profile_photo FROM users;")
    users_data = SQL.mycursor.fetchall()

    # # [(user_id, wins)]
    SQL.mycursor.execute("SELECT ID from USERS;")
    num_users = len(SQL.mycursor.fetchall())
    wins_data = []
    for x in range(1, num_users + 1):
        SQL.mycursor.execute("SELECT SUM(won) FROM games WHERE userID = " + str(x) + ";")
        wins_data.append([SQL.mycursor.fetchall()[0][0]])
        if wins_data[x - 1][0] is None:
            wins_data[x - 1][0] = 0

    # combine data - [user_id, username, profile_photo, #wins]
    all_data = []
    for x in range(num_users):
        all_data.append([users_data[x][0], users_data[x][1], users_data[x][2], wins_data[x][0]])

    # now sort all data and select only top 10 users
    all_data = sorted(all_data, key=lambda data: data[3], reverse=True)[:10]

    # display data
    prev = 110
    for x in range(len(all_data)):
        user_data = all_data[x]

        color = WHITE
        if user_data[0] == user_id:
            color = PURPLE

        username_surface = font.render(user_data[1], True, color)
        wins_surface = font.render(str(user_data[3]), True, color)
        try:
            profile_photo = profile_photos[user_data[2]]
            scale = (62, 60)
        except TypeError:
            profile_photo = default_profile_photo
            scale = (57, 54)

        screen.blit(pygame.transform.scale(profile_photo, scale), (176, prev-10))
        screen.blit(username_surface, (380, prev))
        screen.blit(wins_surface, (638, prev))

        if x < 2:
            prev += 78
        elif x == 2:
            prev += 70
        elif x < 5:
            prev += 62
        elif x == 5:
            prev += 66
        else:
            prev += 64

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_on_button(37, 58, 48, 19):
                    if back_to_mm:
                        main_menu(user_id)
                    else:
                        stats_page(user_id)

        pygame.display.update()
        clock.tick(60)


def login_page(back_to_stats=False, back_to_profile=False, back_to_puzzles=False):
    pygame.display.set_caption("Login")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.fill((30, 129, 228))
    screen.blit(login_page_img, (25, 25))

    username_typing = password_typing = False
    username_input = password_input = ""
    username_color = password_color = WHITE

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # sign up button
                if is_mouse_on_button(490, 730, 77, 16):
                    signup_page()
                # main menu
                if is_mouse_on_button(534, 55, 160, 170) or is_mouse_on_button(70, 90, 51, 23):
                    main_menu()
                # login
                if is_mouse_on_button(549, 540, 180, 73):
                    user_info = (username_input, password_input)
                    found_id = check_if_exists(user_info, False)
                    if found_id != -1:
                        if back_to_stats:
                            stats_page(found_id)
                        elif back_to_profile:
                            profile_page(found_id)
                        elif back_to_puzzles:
                            puzzles_page(found_id)
                        else:
                            main_menu(found_id)
                    # invalid msg
                    invalid_msg_surface = small_font.render("Invalid username or password.", True, RED)
                    screen.blit(invalid_msg_surface, (178, 520))

                # username typing
                if is_mouse_on_button(88, 381, 460, 29):
                    username_typing = True
                    password_typing = False
                    username_color = PURPLE
                    password_color = WHITE

                # password typing
                elif is_mouse_on_button(88, 466, 460, 29):
                    username_typing = False
                    password_typing = True
                    username_color = WHITE
                    password_color = PURPLE

                else:
                    username_typing = False
                    password_typing = False
                    username_color = password_color = WHITE

            # user text input
            if event.type == pygame.KEYDOWN:

                if username_typing:
                    if event.key == pygame.K_BACKSPACE:
                        username_input = username_input[:-1]
                    elif len(username_input) < 20 and event.key != pygame.K_RETURN:
                        username_input += event.unicode

                elif password_typing:
                    if event.key == pygame.K_BACKSPACE:
                        password_input = password_input[:-1]
                    elif len(password_input) < 20 and event.key != pygame.K_RETURN:
                        password_input += event.unicode

                # if "enter" is pressed
                if event.key == pygame.K_RETURN:
                    user_info = (username_input, password_input)
                    found_id = check_if_exists(user_info, False)
                    if found_id != -1:
                        if back_to_stats:
                            stats_page(found_id)
                        elif back_to_profile:
                            profile_page(found_id)
                        elif back_to_puzzles:
                            puzzles_page(found_id)
                        else:
                            main_menu(found_id)

                    # invalid msg
                    invalid_msg_surface = small_font.render("Invalid username or password.", True, RED)
                    screen.blit(invalid_msg_surface, (178, 520))

        # username text
        pygame.draw.rect(screen, WHITE, (217, 351, 460, 60))
        username_surface = font.render(username_input, True, BLACK)
        screen.blit(username_surface, (225, 374))
        # outline
        pygame.draw.rect(screen, username_color, (213, 373, 351, 40), 3)

        # password text
        pygame.draw.rect(screen, WHITE, (218, 421, 460, 60))
        password_surface = font.render("*"*len(password_input), True, BLACK)
        screen.blit(password_surface, (225, 459))
        # outline
        pygame.draw.rect(screen, password_color, (213, 450, 351, 40), 3)

        pygame.display.update()
        clock.tick(60)


def profile_page(user_id):
    SQL.mycursor.execute("SELECT * FROM users WHERE ID = "+str(user_id))
    data = SQL.mycursor.fetchone()

    username, password, since = data[1], data[2], str(data[3])
    total_played = str(get_all_stats(user_id)[1][0])

    pygame.display.set_caption("Profile")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.blit(profile_page_img, (-10, -17))

    SQL.mycursor.execute("SELECT profile_photo FROM users WHERE ID = " + str(user_id) + ";")
    try:
        user_profile_photo = profile_photos[SQL.mycursor.fetchall()[0][0]]
        screen.blit(user_profile_photo, (294.7, 28))
    except TypeError:
        pass

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # back to mm
                if is_mouse_on_button(49, 53, 49, 17):
                    main_menu(user_id)
                # sign out
                if is_mouse_on_button(673, 41, 76, 30):
                    are_you_sure_logout(user_id, True)
                # full stats
                if is_mouse_on_button(637, 702, 100, 45):
                    stats_page(user_id, True)
                # choose profile photo
                if is_mouse_on_button(290, 25, 196, 185) or is_mouse_on_button(491, 33, 59, 23):
                    choose_profile_photo_page(user_id)

        # username
        start = 395 - (9 * len(username))
        username_surface_big = big_font.render(username, True, BLACK)
        screen.blit(username_surface_big, (start, 220))
        username_surface_small = font.render(username, True, BLACK)
        screen.blit(username_surface_small, (236, 333))
        # password
        password_surface = font.render(password, True, BLACK)
        screen.blit(password_surface, (227, 448))
        # since
        since_surface = font.render(since, True, BLACK)
        screen.blit(since_surface, (433, 573))
        # total played
        total_played_surface = font.render(total_played, True, BLACK)
        screen.blit(total_played_surface, (395, 698))

        pygame.display.update()
        clock.tick(60)


def signup_page():
    pygame.display.set_caption("Sign Up")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.fill((10, 110, 225))
    screen.blit(signup_page_img, (12, 12))

    username_typing = password_typing = False
    username_input = password_input = ""
    username_color = password_color = WHITE

    invalid_msg = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # sign in buttons
                if is_mouse_on_button(516, 743, 71, 15) or is_mouse_on_button(61, 83, 53, 20):
                    login_page()
                # main menu
                if is_mouse_on_button(546, 61, 160, 170):
                    main_menu()
                # sign up
                if is_mouse_on_button(555, 539, 182, 72):
                    # check if username is valid
                    if len(username_input) < 3:
                        invalid_msg = "Username length must be 3 or longer."
                    # check if password is valid
                    elif len(password_input) < 6:
                        invalid_msg = "Password length must be 6 or longer."
                    else:
                        user_info = (username_input, password_input)
                        # already exists
                        if check_if_exists(user_info, True) != -1:
                            invalid_msg = "username already exists"
                        else:
                            clause = "INSERT INTO users (username, password, since) VALUES (%s, %s, %s);"
                            today = str(datetime.date.today()).replace('-', ':')
                            user_info = (user_info[0], user_info[1], today)
                            SQL.mycursor.execute(clause, user_info)
                            SQL.mydb.commit()
                            login_page()

                # username typing
                if is_mouse_on_button(59, 359, 583, 14):
                    username_typing = True
                    password_typing = False
                    username_color = PURPLE
                    password_color = WHITE

                # password typing
                elif is_mouse_on_button(62, 444, 583, 14):
                    username_typing = False
                    password_typing = True
                    username_color = WHITE
                    password_color = PURPLE

                else:
                    username_typing = False
                    password_typing = False
                    username_color = password_color = WHITE

            # user text input
            if event.type == pygame.KEYDOWN:

                if username_typing:
                    if event.key == pygame.K_BACKSPACE:
                        username_input = username_input[:-1]
                    elif len(username_input) < 20 and event.key != pygame.K_RETURN:
                        username_input += event.unicode

                elif password_typing:
                    if event.key == pygame.K_BACKSPACE:
                        password_input = password_input[:-1]
                    elif len(username_input) < 20 and event.key != pygame.K_RETURN:
                        password_input += event.unicode

                # if enter is pressed
                if event.key == pygame.K_RETURN:
                    if len(username_input) < 3:
                        invalid_msg = "Username length must be 3 or longer."
                    # check if password is valid
                    elif len(password_input) < 6:
                        invalid_msg = "Password length must be 6 or longer."
                    else:
                        user_info = (username_input, password_input)
                        # already exists
                        if check_if_exists(user_info, True) != -1:
                            invalid_msg = "username already exists"
                        else:
                            clause = "INSERT INTO users (username, password, since) VALUES (%s, %s, %s);"
                            today = str(datetime.date.today()).replace('-', ':')
                            user_info = (user_info[0], user_info[1], today)
                            SQL.mycursor.execute(clause, user_info)
                            SQL.mydb.commit()
                            print("inserted to db")
                            login_page()

        # username text
        pygame.draw.rect(screen, WHITE, (175, 322, 460, 60))
        username_surface = font.render(username_input, True, BLACK)
        screen.blit(username_surface, (193, 345))
        # outline
        pygame.draw.rect(screen, username_color, (178, 343, 351, 40), 3)

        # password text
        pygame.draw.rect(screen, WHITE, (175, 402, 460, 60))
        password_surface = font.render("*"*len(password_input), True, BLACK)
        screen.blit(password_surface, (193, 430))
        # outline
        pygame.draw.rect(screen, password_color, (176, 422, 351, 40), 3)

        # invalid msg
        pygame.draw.rect(screen, WHITE, (130, 480, 370, 60))
        invalid_msg_surface = small_font.render(invalid_msg, True, RED)
        screen.blit(invalid_msg_surface, (140, 490))

        pygame.display.update()
        clock.tick(60)


def stats_page(user_id, back_to_profile=False):
    SQL.mycursor.execute("SELECT username FROM users WHERE ID = " + str(user_id))
    username = SQL.mycursor.fetchone()[0]
    pygame.display.set_caption("Statistics - "+username)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.blit(stats_page_img, (-20, -30))

    games, totals, win_p, times, avg_moves = get_all_stats(user_id)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # main menu
                if is_mouse_on_button(26, 39, 51, 19):
                    if not back_to_profile:
                        main_menu(user_id)
                    else:
                        profile_page(user_id)
                # leaderboard
                if is_mouse_on_button(534, 685, 223, 58):
                    leaderboard_page(user_id)

        total = totals[0]
        pos = (590, 465)
        if total > 0:
            wins = totals[2]
            end_angle = (wins / total) * 360
            draw_arc(screen, 0, end_angle, 100, pos, GREEN, 10)
            draw_arc(screen, end_angle, 360, 100, pos, RED, 10)
        else:
            draw_arc(screen, 0, 360, 100, pos, BLUE, 10)

        # username
        username_surface = big_font.render(username, True, WHITE)
        # win%
        win_p_surface = big_font.render(win_p, True, BLACK)

        # easy won
        easy_won_surface = small_font.render(str(games[0][1]), True, WHITE)
        # easy lost
        easy_lost_surface = small_font.render(str(games[0][0]), True, WHITE)
        # medium won
        medium_won_surface = small_font.render(str(games[1][1]), True, WHITE)
        # medium lost
        medium_lost_surface = small_font.render(str(games[1][0]), True, WHITE)
        # hard won
        hard_won_surface = small_font.render(str(games[2][1]), True, WHITE)
        # hard lost
        hard_lost_surface = small_font.render(str(games[2][0]), True, WHITE)

        # total games
        total_games_surface = big_font.render(str(totals[0]), True, WHITE)
        # total won
        won_surface = font.render(str(totals[2]), True, GREEN)
        # total lost
        lost_surface = font.render(str(totals[1]), True, RED)

        # longest & shortest
        if times:
            longest_surface = font.render(str(times[0]), True, WHITE)
            shortest_surface = font.render(str(times[1]), True, WHITE)
        else:
            longest_surface = font.render("-Play Games-", True, WHITE)
            shortest_surface = font.render("-Play Games-", True, WHITE)

        # avg moves
        avg_moves_surface = font.render(str(avg_moves), True, WHITE)

        screen.blit(username_surface, (300, 100))
        screen.blit(win_p_surface, (655, 70))

        screen.blit(easy_won_surface, (242, 270))
        screen.blit(easy_lost_surface, (237, 312))

        screen.blit(medium_won_surface, (357, 270))
        screen.blit(medium_lost_surface, (357, 312))

        screen.blit(hard_won_surface, (500, 270))
        screen.blit(hard_lost_surface, (500, 312))

        screen.blit(total_games_surface, (567, 443))
        screen.blit(won_surface, (450, 447))
        screen.blit(lost_surface, (445, 485))

        screen.blit(longest_surface, (225, 577))
        screen.blit(shortest_surface, (225, 637))
        screen.blit(avg_moves_surface, (328, 693))

        pygame.display.update()
        clock.tick(60)


def puzzles_page(user_id):
    pygame.display.set_caption("Checkers Puzzles")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.blit(puzzles_img, (-10, -17))

    SQL.mycursor.execute("SELECT puzzle_level FROM users WHERE ID = " + str(user_id) + ";")
    puzzle_level = SQL.mycursor.fetchall()[0][0]  # 0 = no puzzles, 1 = completed 1...
    lock_puzzles(puzzle_level, screen)

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # print(pygame.mouse.get_pos())
                # main menu
                if is_mouse_on_button(40, 49, 54, 20):
                    main_menu(user_id)
                # puzzle 1
                if is_mouse_on_button(90, 280, 117, 144):
                    play_puzzle(P1, 1, user_id)
                # puzzle 2
                if is_mouse_on_button(336, 280, 117, 144) and puzzle_level >= 1:
                    play_puzzle(P2, 2, user_id, P2_SECOND)
                # puzzle 3
                if is_mouse_on_button(578, 280, 117, 144) and puzzle_level >= 2:
                    play_puzzle(P3, 3, user_id, P3_SECOND)
                # puzzle 4
                if is_mouse_on_button(90, 508, 117, 144) and puzzle_level >= 3:
                    play_puzzle(P4, 4, user_id, P4_SECOND)
                # puzzle 5
                if is_mouse_on_button(336, 507, 117, 144) and puzzle_level >= 4:
                    play_puzzle(P5, 5, user_id, P5_SECOND)
                # puzzle 6
                if is_mouse_on_button(578, 507, 117, 144) and puzzle_level >= 5:
                    play_puzzle(P6, 6, user_id, P6_SECOND)

        pygame.display.update()


def play_puzzle(puzzle_info, p_id, user_id, second_phase_info=None):
    # puzzle_info = (PUZZLE_BASE, PUZZLE_FIRST, PUZZLE_CORRECT, puzzle_base_img, puzzle_started_img)
    PUZZLE_BASE, PUZZLE_FIRST, PUZZLE_CORRECT = deepcopy(puzzle_info[:3])
    puzzle_base_img, puzzle_started_img = puzzle_info[3:]

    pygame.display.set_caption("Puzzle #" + str(p_id))
    screen = pygame.display.set_mode((800, 800))

    puzzle = Puzzle(screen, PUZZLE_BASE, RED, PUZZLE_CORRECT, PUZZLE_FIRST)
    game = puzzle.game
    screen.blit(puzzle_base_img, (-10, 0))
    started_puzzle = False
    game.started_puzzle = started_puzzle
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)

        for event in pygame.event.get():

            # user wishes to quit the application
            if event.type == pygame.QUIT:
                pygame.quit()

            # menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_mouse_on_button(675, 66, 100, 26):
                    puzzles_page(user_id)

                # start puzzle
                if is_mouse_on_button(296, 666, 149, 42) and not started_puzzle:
                    started_puzzle = True
                    game.started_puzzle = started_puzzle
                    game.board.board = deepcopy(PUZZLE_FIRST)
                    time.sleep(0.5)
                    screen.blit(puzzle_started_img, (-10, 0))

                # try again
                if is_mouse_on_button(655, 260, 130, 50) and game.board.is_game_over:
                    puzzle = Puzzle(screen, PUZZLE_BASE, RED, PUZZLE_CORRECT, deepcopy(PUZZLE_FIRST))
                    game = puzzle.game
                    screen.blit(puzzle_base_img, (-10, 0))
                    started_puzzle = False
                    game.started_puzzle = started_puzzle

                position = pygame.mouse.get_pos()
                row, col = small_get_mouse_row_col(position)
                game.select_piece(row, col)

        # if a move was played
        if game.board.is_game_over:

            if p_id == 1:
                if type(game.board.board[0][1]) == SmallPiece:
                    if game.board.board[0][1].queen:
                        game.board.board = PUZZLE_CORRECT
                        screen.blit(big_font.render("Correct!", True, GREEN), (653, 190))
                        SQL.mycursor.execute("SELECT puzzle_level FROM users WHERE ID = " + str(user_id))
                        puzzle_level = SQL.mycursor.fetchall()[0][0]
                        if puzzle_level == 0:
                            SQL.mycursor.execute(
                                "UPDATE users SET puzzle_level = " + str(p_id) + " WHERE ID = " + str(user_id))
                            SQL.mydb.commit()
                else:
                    screen.blit(big_font.render("Wrong.", True, RED), (660, 190))
                    pygame.draw.rect(screen, WHITE, (655, 260, 130, 50))
                    screen.blit(font.render("Try Again", True, BLACK), (667, 263))

            else:
                if game.check_move():
                    if second_phase_info:
                        second_phase(second_phase_info, puzzle_info, p_id, user_id)
                    else:
                        screen.blit(big_font.render("Correct!", True, GREEN), (653, 190))
                        SQL.mycursor.execute(
                            "UPDATE users SET puzzle_level = " + str(p_id) + " WHERE ID = " + str(user_id))
                        SQL.mydb.commit()
                else:
                    screen.blit(big_font.render("Wrong.", True, RED), (660, 190))
                    pygame.draw.rect(screen, WHITE, (655, 260, 130, 50))
                    screen.blit(font.render("Try Again", True, BLACK), (667, 263))

        game.update_game()


def second_phase(second_phase_info, puzzle_info, p_id, user_id):
    # second_phase_info = (PUZZLE_START, PUZZLE_CORRECT, puzzle_img)
    PUZZLE_START, PUZZLE_CORRECT = deepcopy(second_phase_info[0]), deepcopy(second_phase_info[1])
    puzzle_img = second_phase_info[2]

    pygame.display.set_caption("Puzzle #" + str(p_id))
    screen = pygame.display.set_mode((800, 800))
    game = SmallGame(screen, correct_board=PUZZLE_CORRECT)
    game.board.board = PUZZLE_START
    screen.blit(puzzle_img, (-10, 0))
    started_puzzle = True
    game.started_puzzle = started_puzzle
    clock = pygame.time.Clock()

    while True:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # menu
                if is_mouse_on_button(675, 66, 100, 26):
                    puzzles_page(user_id)

                # try again
                if is_mouse_on_button(655, 260, 130, 50) and game.board.is_game_over:
                    if p_id == 2:
                        play_puzzle(puzzle_info, p_id, user_id, second_phase_info=P2_SECOND)
                    if p_id == 3:
                        play_puzzle(puzzle_info, p_id, user_id, second_phase_info=P3_SECOND)
                    if p_id == 4:
                        play_puzzle(puzzle_info, p_id, user_id, second_phase_info=P4_SECOND)
                    if p_id == 5:
                        play_puzzle(puzzle_info, p_id, user_id, second_phase_info=P5_SECOND)
                    if p_id == 6:
                        play_puzzle(puzzle_info, p_id, user_id, second_phase_info=P6_SECOND)

                position = pygame.mouse.get_pos()
                row, col = small_get_mouse_row_col(position)
                game.select_piece(row, col)

        # if a move was played
        if game.board.is_game_over:
            if game.check_move():
                screen.blit(big_font.render("Correct!", True, GREEN), (653, 190))
                SQL.mycursor.execute("SELECT puzzle_level FROM users WHERE ID = " + str(user_id))
                puzzle_level = SQL.mycursor.fetchall()[0][0]
                if p_id > puzzle_level:
                    SQL.mycursor.execute("UPDATE users SET puzzle_level = " + str(p_id) + " WHERE ID = " + str(user_id))
                    SQL.mydb.commit()
            else:
                screen.blit(big_font.render("Wrong.", True, RED), (660, 190))
                pygame.draw.rect(screen, WHITE, (655, 260, 130, 50))
                screen.blit(font.render("Try Again", True, BLACK), (667, 263))

        game.update_game()


def log_in_first_puzzles():
    pygame.display.set_caption("Checkers Puzzles")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 800))
    screen.blit(log_in_for_puzzles, (85, 220))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # log in
                if is_mouse_on_button(286, 324, 232, 59):
                    login_page(back_to_puzzles=True)
                # cancel
                if is_mouse_on_button(362, 419, 83, 13):
                    main_menu()

        pygame.display.update()
        clock.tick(60)


main_menu()
