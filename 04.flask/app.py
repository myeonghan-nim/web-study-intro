from flask import Flask, escape, request, render_template
from bs4 import BeautifulSoup

import requests
import random
import csv

app = Flask(__name__)


@app.route('/')
def hello():

    return render_template('index.html')


@app.route('/lotto')
def lotto():

    numbers = random.sample(range(1, 46), 6)

    return render_template('lotto.html', numbers=numbers)


@app.route('/lunch')
def lunch():

    lst = {
        'Black-bean-sauce noodles': 'http://static.hubzum.zumst.com/hubzum/2019/07/01/10/967a67742c244ebe9ac7c85048c591c3.jpg',
        'Jjambbong': 'https://i.ytimg.com/vi/M04aOUyPIDg/maxresdefault.jpg',
        'steak': 'https://fresheasy.speedgabia.com/contents/p.images/S1932390/750x750.jpg',
        'Kalguksu': 'https://homecuisine.co.kr/files/attach/images/140/824/012/7ece1535875d6ce18990de309b9dbcfb.JPG',
        'Naju gomtang': 'http://ojsfile.ohmynews.com/STD_IMG_FILE/2016/1201/IE002061721_STD.JPG'
    }

    menu, img = random.choice(list(lst.items()))

    return render_template('lunch.html', menu=menu, img=img)


@app.route('/opgg')
def opgg():

    return render_template('opgg.html')


@app.route('/search')
def search():

    opgg_url = 'https://www.op.gg/summoner/userName='
    summoner = request.args.get('summoner')

    url = opgg_url + summoner
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    tier = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierRank').text

    return render_template('search.html', tier=tier, summoner=summoner)


@app.route('/nono')
def nono():

    with open('data.csv', 'r', encoding='utf-8', newline='') as f:
        reader = list(csv.reader(f))

    return render_template('nono.html', products=reader)


@app.route('/new')
def new():

    return render_template('new.html')


@app.route('/create')
def create():

    product = request.args.get('product')
    category = request.args.get('category')
    replace = request.args.get('replace')

    with open('data.csv', 'a+', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        product_info = [product, category, replace]
        writer.writerow(product_info)

    return render_template('create.html')


@app.route('/card')
def card():
    
    with open('data.csv', 'r', encoding='utf-8', newline='') as f:
        reader = list(csv.reader(f))

    return render_template('card.html', products=reader)


if __name__== '__main__':
    app.run(debug=True)
    