import pyshorteners
# URL original #
url = 'https://github.com/Moviopudim?tab=repositories'
# Define a função #
x = pyshorteners.Shortener()
# Encurta a url #
shorturl = x.tinyurl.short(url)
# Printa a url encurtada #
print(f"A URL encurtada e: " + shorturl)