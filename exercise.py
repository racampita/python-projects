cnt = 0
tot = 0.0
while True:
	sval = input('Enter a number: ')
	if sval == 'done':
		break
	try:
		fval = float(sval)
	except:
		print('Invalid Input')
		continue
	cnt += 1
	tot += fval
#print('ALL DONE')
print(tot,cnt,tot/cnt)