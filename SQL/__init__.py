import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='nadavnoa123',
    database='checkers'
)

mycursor = mydb.cursor()
# print(mycursor.fetchall())

# mycursor.execute("CREATE TABLE users (ID INTEGER PRIMARY KEY AUTO_INCREMENT, username TEXT, password TEXT);")

# users_insert_formula = "INSERT INTO users (username, password) VALUES (%s, %s);"
# user = ("idog", "1234567")
# mycursor.execute(users_insert_formula, user)

# insert_formula = "INSERT INTO games (userID, won, difficulty, gtime, total_moves) VALUES (%s, %s, %s, %s, %s);"
# game = (1, 0, 3, "00:07:48", 36)
# mycursor.execute(games_insert_formula, game)

# mycursor.execute("ALTER TABLE users ADD COLUMN puzzle_level INT DEFAULT 0;")
# mycursor.execute("ALTER TABLE users DROP COLUMN puzzle_level;")
# mycursor.execute("ALTER TABLE users ALTER puzzle_level SET DEFAULT 0;")
# mycursor.execute("SELECT puzzle_level FROM users WHERE ID=1;")
# my_result = mycursor.fetchall()[0][0]  # from  last executed command, fetches all. else - fetchone()
# print(my_result)
# mycursor.execute("UPDATE users SET puzzle_level = 0 WHERE puzzle_level IS NULL;")
mydb.commit()  # this will actually save the changes in the table
