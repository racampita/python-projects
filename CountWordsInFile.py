file = input('OPEN FILE: ')
opnFile = open(file,'r')
txt = opnFile.read().split()
print(len(txt))