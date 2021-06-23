file = input("Enter filename of file to open: ")
data = open(file)
# counting all words in the file
count = dict()
for line in data:
   for word in line.split():
       count[word] = count.get(word,0) + 1

reverselist = sorted([ (v,k) for k,v in count.items()],reverse=True)
for k,v in reverselist[:10]:
    print(v,k)

