
import requests

formating = exec(requests.get("https://raw.githubusercontent.com/ProfKrzys/test/main/utils/formating.py").text)

color = formating.color

class Logger:
    def plus(text):
        print(f"{color.bright_black('[')}{color.green('+')}{color.bright_black(']')} {color.white(text)}")

    def minus(text):
        print(f"{color.bright_black('[')}{color.red('-')}{color.bright_black(']')} {color.white(text)}")

    def slash(text):
        print(f"{color.bright_black('[')}{color.dark_yellow('/')}{color.bright_black(']')} {color.white(text)}")
