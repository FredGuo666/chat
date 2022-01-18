
lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5]  # str 可以当作list来看
	name = s[0][5:]
	print(time) 
	print(name)
