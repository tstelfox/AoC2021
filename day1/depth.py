file = open('inputfile', mode = 'r')
line1 = int(file.readline())
line2 = int(file.readline())
line3 = int(file.readline())

cnt = 3
increments = 0
print('fuck')

while True:
	cnt+=1
	try:
		line4 = int(file.readline())
	except:
		break
	if cnt == 4:	
		sum1 = line1 + line2 + line3
	sum2 = line2 + line3 + line4

	if sum2 > sum1:
		increments += 1
	sum1 = sum2
	line1 = line2
	line2 = line3
	line3 = line4
	if not line1 or not line2:
		break

file.close()

print("The amount of increments is:", increments)