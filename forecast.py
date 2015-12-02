""" Get a json wiht meteo forecast information for Saint Genis and print to the
    screen the current situation plus the forecast for the day. It uses yahoo APIs
"""

import json
import pprint
import urllib

ita_lookup = {
    "Fair" : "sereno (Fair)",
    "Clear" : "sereno (Clear)",
    "Sunny" : "soleggiato",
    "Mostly Sunny" : "prevalentemente soleggiato",
    "Partly Cloudy" : "parzialmente nuvoloso",
}

def f2c(ft):
    """ Convert farenight temperature to celsius
        ft: farenight temperature
        Return the floating point value for the temperature
    """
    return (int(ft)-32)/1.8

if __name__ == '__main__':
#
#    url = urllib.quote('https://query.yahooapis.com/v1/public/yql?q=select * from weather.forecast where woeid'
#                        '=624144&format=json&env=store://datatables.org/alltableswithkeys')
    url = ('https://query.yahooapis.com/v1/public/yql?q=select%20*%20'
           'from%20weather.forecast%20where%20woeid%20%3D624144&format'
           '=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys')
    page = urllib.urlopen(url).read()
    data = json.loads(page)

    now = data['query']['results']['channel']['item']['condition']
    ita_text = ita_lookup.get(now['text'], now['text'])
    print "Il tempo ora e' %s e ci sono %.1f gradi" % (ita_text, f2c(now['temp']))

    today = data['query']['results']['channel']['item']['forecast'][0]
    ita_text = ita_lookup.get(today['text'], today['text'])
    print "Il tempo oggi sara' %s con minima di %.1f gradi e massima di %.1f gradi" % (ita_text, f2c(today['low']), f2c(today['high']))
