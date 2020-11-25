

def calculate(a,b):
	raw = (3 * b - a) / 2
	if raw > 100.0:
		raw = 'IMPOSIBLE'
	print(a,"       ",b,"      ",raw)

x = input('LAST GRADE: ' )
y = input('NEW GRADE: ' )
print("LAST GRADE","NEW GRADE","RAW GRADE")
calculate(int(x),int(y))