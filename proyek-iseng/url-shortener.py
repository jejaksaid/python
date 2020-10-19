from pyshorteners import Shortener

url = input("Shorten")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Result: ", s)