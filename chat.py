#读取档案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:         
		for line in f:
			lines.append(line.strip())  # strip()去掉换行符
	return(lines )

# 文件转换
def convert(lines):
	new = []
	person = None
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue     #跳到下一个回圈
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:		
			new.append(person + ': ' + line)
	return new  

# 写入档案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines) 
	write_file('output.txt', lines)

main()
