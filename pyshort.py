import pyshorteners

url = input("Enter your URL")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Your URL is ready: ", s)
