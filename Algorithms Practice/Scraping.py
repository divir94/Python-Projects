import urllib2
from bs4 import BeautifulSoup

def striphtml(data):
    p = re.compile(r'<.*?>')
    return p.sub('', data)

def get_html(url):
   hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
          "X-Parse-Application-Id": "5DZi1FrdZcwBKXIxMplWsqYu3cEEumlmFDB1kKnC",
            "X-Parse-REST-API-Key": "pMT9AefpMkJfbcJ5fTA2uOGxwpitMII7hpCt8x4O"}
   req = urllib2.Request(url, headers=hdr)
   html = None
   try:
       html = urllib2.urlopen(req).read()
   except urllib2.HTTPError, e:
       print "URL broke: %s" % url
   return html

def find_tags(html, tag_name, class_name=False):
   soup = BeautifulSoup(html)
   if class_name: tags = soup.findAll(tag_name, { "class" : class_name })
   else: tags = soup.findAll(tag_name)
   return tags

def print_text(url):
     html = get_html(url)
     tags = find_tags(html, 'p')
     for tag in tags:
          print tag.text.replace('\n','').replace('\r','').replace('  ','')
          print
     
url = "https://parse.com/apps/barlift--3/push_notifications?page=1&type=all"
html = get_html(url)
print html

#tags = find_tags(html,'span', 'endorse-item-name-text')

#print(tags)
