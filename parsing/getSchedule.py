from bs4 import BeautifulSoup
import requests


def getDay(n):
    if (n == 1):
        return ("<b>Понедельник</b>")
    elif (n == 2):
        return ("<b>Вторник</b>")
    elif (n == 3):
        return ("<b>Среда</b>")
    elif (n == 4):
        return ("<b>Четверг</b>")
    elif (n == 5):
        return ("<b>Пятница</b>")
    elif (n == 6):
        return ("<b>Суббота</b>")
    elif (n == 7):
        return ("<b>Воскресенье</b>")


def lessonTime(para):
    if (para == 1):
        return ("8:20-9:50")
    elif (para == 2):
        return ("10:00-11:35")
    elif (para == 3):
        return ("12:05-13:40")
    elif (para == 4):
        return ("12:05-13:40")
    elif (para == 5):
        return ("13:50-15:25")
    elif (para == 6):
        return ("15:35-17:10")
    elif (para == 7):
        return ("17:20-18:40")
    elif (para == 8):
        return ("18:45-20:05")
    elif (para == 9):
        return ("20:10-21:30")


def pars(el, counter, para, soup):
    message = ''
    if (counter == 1):
        time = lessonTime(para)
        type = soup.find("td", id=el).find("div", class_="l-pr").text
        predm = soup.find("td", id=el).find_next("div", class_="l-dn").text
        prepod = soup.find("td", id=el).find("div", class_="l-tn").text
        kab = soup.find("td", id=el).find("div", class_="l-p").text
        return ("\n" + "<b>" + time + "</b>" + "\n" + type + "\n" + predm + "\n" + prepod + " \n" + kab + " \n")
    if (counter > 1):
        message = "<u>Несколько пар в одно время</u>\n\n"
        time = lessonTime(para)
        temp_type = soup.find("td", id=el).find_all("div", class_="l-pr")
        temp_predm = soup.find("td", id=el).find_all("div", class_="l-dn")
        temp_prepod = soup.find("td", id=el).find_all("div", class_="l-tn")
        temp_kab = soup.find("td", id=el).find_all("div", class_="l-p")
        itemsInOneLesson = len(temp_type)
        for i in range(itemsInOneLesson):
            type = temp_type[i].text
            predm = temp_predm[i].text
            prepod = temp_prepod[i].text
            kab = temp_kab[i].text
            message += (type + "\n" + predm + "\n" + prepod + " \n" + kab + " \n" + " \n")
        return ("\n" + "<b>" + time + "</b>" + "\n" + message)


def getSchedule(n, url):
    headers = {
        "accept": "*/*",
        "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Mobile Safari/537.36"
    }

    req = requests.get(url, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, "lxml")
    day = getDay(n)
    message = day + "\n"
    if (n == 1):
        tag = "_1"
        for para in range(1, 9):
            el = str(para) + tag
            counter = len(soup.find("td", id=el).find_all("div", class_="l-p"))
            if (counter > 0):
                message += pars(el, counter, para, soup)
            else:
                time = lessonTime(para)
                message += ("\n" + "<b>" + time + "</b>" + "\n Пар нет 😌 \n")

    elif (n == 2):
        tag = "_2"
        for para in range(1, 9):
            el = str(para) + tag
            counter = len(soup.find("td", id=el).find_all("div", class_="l-p"))
            if (counter > 0):
                message += pars(el, counter, para, soup)
            else:
                time = lessonTime(para)
                message += ("\n" + "<b>" + time + "</b>" + "\n Пар нет 😌 \n")
    elif (n == 3):
        tag = "_3"
        for para in range(1, 9):
            el = str(para) + tag
            counter = len(soup.find("td", id=el).find_all("div", class_="l-p"))
            if (counter > 0):
                message += pars(el, counter, para, soup)
            else:
                time = lessonTime(para)
                message += ("\n" + "<b>" + time + "</b>" + "\n Пар нет 😌 \n")
    elif (n == 4):
        tag = "_4"
        for para in range(1, 9):
            el = str(para) + tag
            counter = len(soup.find("td", id=el).find_all("div", class_="l-p"))
            if (counter > 0):
                message += pars(el, counter, para, soup)
            else:
                time = lessonTime(para)
                message += ("\n" + "<b>" + time + "</b>" + "\n Пар нет 😌 \n")
    elif (n == 5):
        tag = "_5"
        for para in range(1, 9):
            el = str(para) + tag
            counter = len(soup.find("td", id=el).find_all("div", class_="l-p"))
            if (counter > 0):
                message += pars(el, counter, para, soup)
            else:
                time = lessonTime(para)
                message += ("\n" + "<b>" + time + "</b>" + "\n Пар нет 😌 \n")
    elif (n == 6):
        tag = "_6"
        for para in range(1, 9):
            el = str(para) + tag
            counter = len(soup.find("td", id=el).find_all("div", class_="l-p"))
            if (counter > 0):
                message += pars(el, counter, para, soup)
            else:
                time = lessonTime(para)
                message += ("\n" + "<b>" + time + "</b>" + "\n Пар нет 😌 \n")
    elif (n == 7):
        message += ("\n Пар нет 😌 \n")

    return message
