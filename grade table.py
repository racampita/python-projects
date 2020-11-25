print("LAST GRADE","NEW GRADE","RAW GRADE")

def calculate(a,b):
	raw = (3 * b - a) / 2
	if raw > 100.0:
		raw = 'IMPOSIBLE'
	print(a,"       ",b,"      ",raw)

for x in range (80,100):
	for y in range (80,100):
		calculate(x,y)