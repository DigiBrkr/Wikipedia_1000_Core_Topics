#Need to install wikipedia libary from: https://pypi.python.org/pypi/wikipedia
import wikipedia
import urllib.request, urllib.parse, urllib.error
import codecs
import ssl
#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

startingPoint = wikipedia.page("Wikipedia:1,000 core topics")
startingPoint = startingPoint.links

count = 0
baseURL = "https://en.wikipedia.org/wiki/Special:Export/"
for item in startingPoint:
    item = str(item)
    print(item)
    item = item.replace(" ", "_")
    item = item.replace("/", "_")
    url = baseURL + item
    try:
        data = urllib.request.urlopen(url, context=ctx)
        #work around for articles with funky characters in there title
    except:
        continue
    data = data.read().decode()
    name = item + ".xml"
    fileHandle = codecs.open(name, 'w', "utf-8")
    fileHandle.write(data)
    fileHandle.close()
