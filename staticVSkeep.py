s = open("Static_MVI_20011.txt", 'r')
Sline = s.readlines()

k = open("toKeep_20011.txt", 'r')
Kline = k.readlines()


f = open("static_20011.txt", 'a')
i = 0

for K in Kline:
	static = K.split(" ")
	try:
		print(Sline[i])
		for x in static:
			if " "+x+" " not in Sline[i]:
				f.write(x+ " ")
		i = i+1
	except:
		break
