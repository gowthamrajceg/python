with open("file1.txt") as f:
	with open("file2.txt") as f1:
		for line in f:
			f1.write(line)
