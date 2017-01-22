puncList = [".", ",", "!", "?", ":", ";", "\"", "\'", "(", ")"]
dict = {}
file = open("sample.txt", "rU")
for line in file:
	for punc in puncList:
		line = line.replace(punc, "")
	line = line.lower()
	for word in line.split():
		if word not in dict:
			dict[word] = 1
		else:
			dict[word] += 1