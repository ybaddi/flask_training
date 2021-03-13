import feedparser
from flask import Flask, render_template,  request
import requests
import json
# from urllib2 import urlopen
# import urllib.request
app = Flask(__name__)


DEFAULTS={'publication': 'bbc',
                'city': 'London,uk'
           }

RSS_FEEDS={'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
                'cnn': 'http://rss.cnn.com/rss/edition.rss',
                'fox': 'http://feeds.foxnews.com/foxnews/latest',
                'iol': 'http://www.iol.co.za/cmlink/1.640'
           }



def get_news(publication):
    print(publication)
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed['entries']

def get_wather(city):
    print(city)

    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":city,"lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\""}

    headers = {
        'x-rapidapi-key': "596e8021cdmshb5fe200daf4530dp18897djsn630183f7de18",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.get(url, headers=headers, params=querystring)

    return json.loads(response.text[5:-1])


@app.route("/", methods=['GET', 'POST'])
def get_post():
    publication = request.args.get('publication')
    if not publication:
        publication = DEFAULTS['publication']
    
    articles = get_news(publication)
  
    city = request.args.get('city')
    if not city:
        city = DEFAULTS['city']
    wather = get_wather(city)
    
    return render_template("template.html",
                           articles=articles,
                           wather=wather)

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')


