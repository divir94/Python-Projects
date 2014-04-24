import urllib
import json as m_json
import requests, random, re, string, random
from bs4 import BeautifulSoup


def genThesis():
    #query = raw_input ( '\nTopic: ' )
    # keyword = raw_input ( '\nkeyword: ' )
    query = 'education'
    websites = {'businessinsider.com': 'h1', 'cnn.com': 'h1'}
    web = random.choice(websites.keys())
    queryText = 'reason why'
    query = queryText + query + ' is important site:' + web
    query = urllib.urlencode ( { 'q' : query } )
    response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query ).read()
    json = m_json.loads ( response )
    results = json [ 'responseData' ] [ 'results' ]
    print 'length of results: ', len(results)

    thesisURL = results[random.randint(0, (len(results) - 1))]['url']
    r = requests.get(thesisURL)
    data = r.text
    soup = BeautifulSoup(data)

    print 'querty: ', query
    print 'site: ', web
    print 'url: ', thesisURL
        
    #print thesisURL
    if websites[web] == 'h1':
        thesisRaw = str(soup.h1)
    else:
        print('other token')

    #print thesisRaw
    print '\nThesis: ', re.sub(r'<|>|\/|h1', r'', thesisRaw), '\n'

    # to open the document and read the text


    #print thesis
    # print(soup.get_text())

def main():
    genThesis()

if __name__ == "__main__":
    main()
