# import feedparser
from flask import Flask, render_template
import requests
import json
# from urllib2 import urlopen
# import urllib.request
app = Flask(__name__)


RSS_FEEDS={'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
                'cnn': 'http://rss.cnn.com/rss/edition.rss',
                'fox': 'http://feeds.foxnews.com/foxnews/latest',
                'iol': 'http://www.iol.co.za/cmlink/1.640'
           }



@app.route("/", methods=['GET', 'POST'])
def get_post():
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"q":"London,uk","lat":"0","lon":"0","callback":"test","id":"2172797","lang":"null","units":"\"metric\" or \"imperial\""}

    headers = {
        'x-rapidapi-key': "596e8021cdmshb5fe200daf4530dp18897djsn630183f7de18",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
        }

    response = requests.get(url, headers=headers, params=querystring)

    print(response)
    # print(response.json)
    text1=response.text[5:]
    text2=text1[:-1]
    print(text2)
    # print(response.text)
    # data = text2.json()
    #

    # print(data)
    # 
    # 
    parsed = json.loads(text2)
    print(parsed)
    main = parsed['main']
    print(main['temp'])
    return render_template("template.html",
                           main=main)

if __name__ == "__main__":
    app.run(port=5000, debug=True, host='0.0.0.0')


