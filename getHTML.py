import urllib.request, urllib.error, urllib.parse
website = input("Enter Website:")
fhand = urllib.request.urlopen(website)
for line in fhand:
    print(line.decode().strip())