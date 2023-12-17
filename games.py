import sqlite3

game = input("Введіть назву гри\n").lower()

connection = sqlite3.connect("games.db")
cursor = connection.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS games
                  (id INTEGER PRIMARY KEY,
                  title TEXT,
                  description TEXT,
                  rating TEXT,
                  codes TEXT)''')

connection.commit()

cursor.execute("SELECT * FROM games")

cursor.execute("SELECT * FROM games WHERE title LIKE ?", (f"%{game}%",))
check = cursor.fetchone()

if check:
    cursor.execute("SELECT * FROM games WHERE title LIKE ?", (f"%{game}%",))

    info = cursor.fetchone()

    print(f"Гра знайдена - {info[1].capitalize()}")
    action = input("1) Короткий опис гри\n2) Загальний рейтинг\n3) Доступні чит-коди\n")

    if action == "1":
        print(f"Опис гри: \n{info[2]}")

    if action == "2":
        print(f"Рейтинг гри: \n{info[3]}")

    if action == "3":
        print(f"Доступні коди: \n{info[4]}")

else:
    new_game = input("Ви помилилися в назві гри або вона не існує в базі даних\nБажаєте додати її? (y/n)\n").lower()

    if new_game == "y":
        title = input("Введіть назву нової гри\n")
        description = input("Введіть опис гри\n")
        rating = input("Введіть рейтинг гри (якщо він є)\n")
        codes = input("Якщо є коди читів для гри, перерахуйте їх\n")

        cursor.execute("INSERT INTO games (title, description, rating, codes) VALUES (?, ?, ?, ?)",
                        (title, description, rating, codes))

        print("Нова гра додана!\n")
    else:
        exit()

connection.commit()
cursor.close()
connection.close()