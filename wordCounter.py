<<<<<<< HEAD
#open text file
text = open("file.txt", "r")
#split all words in text file
words = text.read().split()
#count all words in text file
count = dict((i,words.count(i)) for i in words)
#put all values in an array
repetitions = []
for key in count.keys():
	repetitions.append(count[key])


def getKeysByValue():
    listOfKeys = list()
    listOfItems = count.items()
    for item  in listOfItems:
        if item[1] == max(repetitions):
            listOfKeys.append(item[0])
    return  listOfKeys

=======
#open text file
text = open("file.txt", "r")
#split all words in text file
words = text.read().split()
#count all words in text file
count = dict((i,words.count(i)) for i in words)
#put all values in an array
repetitions = []
for key in count.keys():
	repetitions.append(count[key])


def getKeysByValue():
    listOfKeys = list()
    listOfItems = count.items()
    for item  in listOfItems:
        if item[1] == max(repetitions):
            listOfKeys.append(item[0])
    return  listOfKeys

>>>>>>> 330c7678249051ff2714787ec9ac56a35b8b4c9a
print(getKeysByValue())