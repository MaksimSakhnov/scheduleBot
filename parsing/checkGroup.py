from bs4 import BeautifulSoup
import requests

headers = {
    "accept": "*/*",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Mobile Safari/537.36"
}


def fac(var):
    if (var == 1):
        return ("https://www.sgu.ru/schedule/bf")
    elif (var == 2):
        return ("https://www.sgu.ru/schedule/gf")
    elif (var == 3):
        return ("https://www.sgu.ru/schedule/gl")
    elif (var == 4):
        return ("https://www.sgu.ru/schedule/ii")
    elif (var == 5):
        return ("https://www.sgu.ru/schedule/imo")
    elif (var == 6):
        return ("https://www.sgu.ru/schedule/ff")
    elif (var == 7):
        return ("https://www.sgu.ru/schedule/ifk")
    elif (var == 8):
        return ("https://www.sgu.ru/schedule/ifg")
    elif (var == 9):
        return ("https://www.sgu.ru/schedule/ih")
    elif (var == 10):
        return ("https://www.sgu.ru/schedule/mm")
    elif (var == 11):
        return ("https://www.sgu.ru/schedule/sf")
    elif (var == 12):
        return ("https://www.sgu.ru/schedule/fi")
    elif (var == 13):
        return ("https://www.sgu.ru/schedule/knt")
    elif (var == 14):
        return ("https://www.sgu.ru/schedule/fps")
    elif (var == 15):
        return ("https://www.sgu.ru/schedule/fppso")
    elif (var == 16):
        return ("https://www.sgu.ru/schedule/fmimt")
    elif (var == 17):
        return ("https://www.sgu.ru/schedule/fp")
    elif (var == 18):
        return ("https://www.sgu.ru/schedule/ef")
    elif (var == 19):
        return ("https://www.sgu.ru/schedule/uf")


def getUrl(var, answer):
    url = fac(var)
    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    rez = soup.find("fieldset", class_="do").find_all("a")
    groups = []
    for el in rez:
        groups.append(el.text)
    group = answer
    if group in groups:
        for el in rez:
            if (el.text == group):
                url = "https://www.sgu.ru" + el["href"]
                return (url)
                break
    else:
        return -1
