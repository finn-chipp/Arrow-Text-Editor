def quicksave(feed,filename):
	with open(filename, "r") as origfile:
		readfile = list(origfile.read())
		rawfile = origfile.read()
	readfeed = list(feed)
	if readfile == readfeed:
		pass
	elif rawfile in readfeed and len(readfile) < len(readfeed):
		p = readfile[-1]
		end = readfile.index(p)
		del readfeed[0:end]
		x = -1
		for i in range(len(readfeed)):
			x+=1
			f = open(filename, "a")
			f.write(readfeed[x])
			f.close()
	else:
		f = open(filename, "w")
		f.write(feed)
		f.close()
#qsave(input("feed: "), input("filename: "))#<-- this is just for testing by itself
def loadfile(filename):
	try:
		f = open(filename, "r")
		return (f.read())
	except:
		return ("File is presumed not to exist. If you have entered the name correctly then try using a file suffix (such as .py or .txt)")

