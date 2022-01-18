#读取档案
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:         
		for line in f:
			lines.append(line.strip())  # strip()去掉换行符
	return(lines )

# 文件转换
def convert(lines):
	person = None
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0 
	for line in lines:
		s = line.split(' ')  # split() 切割
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '贴图':
				allen_sticker_count += 1
			elif s[2] == '图片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '贴图':
				viki_sticker_count += 1
			elif s[2] == '图片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen说了', allen_word_count, '个字')
	print('Allen上传了', allen_sticker_count, '张贴图')
	print('Allen上传了', allen_image_count, '张图片')
	print('Viki说了', viki_word_count, '个字')
	print('Viki上传了', viki_sticker_count, '张贴图')
	print('Viki上传了', viki_image_count, '张图片')
	

# 写入档案
def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines) 
	# write_file('output.txt', lines)

main()
