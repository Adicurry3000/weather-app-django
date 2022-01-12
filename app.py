from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
from bs4 import BeautifulSoup

page = requests.get('https://weather.com/en-IN/weather/today/l/12.89,77.55?par=google&temp=c')
soup = BeautifulSoup(page.content, 'html.parser')
week = soup.find(class_='looking-ahead')
items = week.find_all(class_='today-daypart-content')
period_names = [item.find(class_='today-daypart-title').get_text() for item in items]
short_disc = [item.find(class_='today-daypart-wxphrase').get_text() for item in items]
temp = [item.find(class_='today-daypart-temp').get_text() for item in items]
precip = [item.find(class_='precip-val').get_text() for item in items]

d1 = [period_names[0], short_disc[0], temp[0], precip[0]]
d2 = [period_names[1], short_disc[1], temp[1], precip[1]]
d3 = [period_names[2], short_disc[2], temp[2], precip[2]]
d4 = [period_names[3], short_disc[3], temp[3], precip[3]]
d5 = [period_names[4], short_disc[4], temp[4], precip[4]]

app = Flask(__name__)


@app.route('/')
def weather():

    return render_template('main.html', d1=d1, d2=d2, d3=d3, d4=d4, d5=d5)

@app.route('/today')
def today():
    pass

if __name__ == '__main__':
    app.run(debug=True)
