import csv
import random

import requests
from bs4 import BeautifulSoup
from flask import Flask, escape, request, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/lotto')
def lotto():
    return render_template('lotto.html', numbers=random.sample(range(1, 46), 6))


@app.route('/lunch')
def lunch():
    menu = {
        'Black-bean-sauce noodles': 'http://static.hubzum.zumst.com/hubzum/2019/07/01/10/967a67742c244ebe9ac7c85048c591c3.jpg',
        'Jjambbong': 'https://i.ytimg.com/vi/M04aOUyPIDg/maxresdefault.jpg',
        'steak': 'https://fresheasy.speedgabia.com/contents/p.images/S1932390/750x750.jpg',
        'Kalguksu': 'https://homecuisine.co.kr/files/attach/images/140/824/012/7ece1535875d6ce18990de309b9dbcfb.JPG',
        'Naju gomtang': 'http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1201/IE002061721_STD.JPG',
    }
    menu, img = random.choice(list(menu.items()))
    return render_template('lunch.html', menu=menu, img=img)


if __name__ == '__main__':
    app.run(debug=True)
