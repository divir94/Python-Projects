import urllib2
from bs4 import BeautifulSoup

def get_html(url):
   hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',}
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
     
url = "http://www.bbc.com/sport/0/football/27679577"
print_text(url)

