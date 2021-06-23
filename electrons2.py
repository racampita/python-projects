print("======================================================");
print("Enter the quantum number separated by commas:\t");
q_number = readline();
result = q_number.split(",");

n = int(result[0]);
l = int(result[1]);
ml = float(result[2]);
ms = float(result[3]);

if (ms == -0.5):
	e = ml + (3*l) + 2;
elif (ms == 0.5):
	e = ml + l + 1;
else:
	print("Invalid quantum number. Please try again.");

print("number of valent electrons: " + str(int(e)));