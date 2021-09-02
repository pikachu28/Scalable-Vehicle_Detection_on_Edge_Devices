import os

detect = {
    0: [240, 135, False],
    1: [480, 135,False],
    2: [720, 135, False],
    3: [960,135, False],
    4: [240, 270, False],
    5: [480, 270, False],
    6: [720, 270, False],
    7: [960, 270, False],
    8: [240, 405, False],
    9: [480, 405, False],
    10: [720, 405, False],
    11: [960, 405, False],
    12: [240, 540, False],
    13: [480, 540, False],
    14: [720, 540, False],
    15: [960, 540, False],
}
line = []

bbFile = os.listdir("/Users/anjalisingh/Desktop/edge_detection/Automation/BoundingBox")
bbFile.remove('.DS_Store')
print(bbFile)
# with open("/Users/anjalisingh/Desktop/edge_detection/yolov5-master/boundingBox.txt") as f:
for bb in bbFile:
	with open("/Users/anjalisingh/Desktop/edge_detection/Automation/BoundingBox/"+bb) as f:
	    line = f.readlines()
	# i=0
	print(bb)
	b = bb.split(".")[0].split("_")
	print(b)
	f = open("TileToKeep/toKeep_"+b[2]+".txt", 'a')
	# f = open("localVideos_1.txt", 'a')

	for x in line:
	    if x[0] == "V":
	        # f.write("Segment {}: ".format(str(i)))
	        for d in detect:
	            if(detect[d][2]==True):
	                f.write(str(d)+" ")
	                detect[d][2] = False
	        # i=i+1
	        f.write("\n")
	        continue
	    else:
	        x = x.split(' ')[1:5]
	        # print(x)
	        x[0], x[1], x[2], x[3] = float(x[0]), float(x[1]), float(x[2]), float(x[3])
	        points = [[x[0]-x[2]/2, x[1]+x[3]/2], [x[0]+x[2]/2, x[1]+x[3]/2], [x[0]-x[2]/2, x[1]-x[3]/2], [x[0]+x[2]/2, x[1]-x[3]/2]]
	        points = [[points[0][0]*1.1, points[0][1]*0.9], [points[1][0]*0.9, points[1][1]*0.9], [points[2][0]*1.1, points[2][1]*1.1], [points[3][0]*0.9, points[3][1]*1.1]]
	        for d in detect:
	            for p in points:
	                _x = p[0]*960
	                y = p[1]*540
	                if (_x<detect[d][0] and y<detect[d][1] and y>(detect[d][1]-135) and _x>(detect[d][0]-240)):
	                    detect[d][2] = True
	# f.write("Segment {}: ".format(str(i)))
	for d in detect:
	    if(detect[d][2]==True):
	        f.write(str(d)+" ")
	        detect[d][2] = False
	f.write("\n")

# [[0.0, 0.21111111156642437], [0.04791666567325592, 0.21111111156642437], [0.0, 0.16481481678783894], [0.04791666567325592, 0.16481481678783894]]
# [[0.0, 0.19000000040978193], [0.04312499910593033, 0.19000000040978193], [0.0, 0.18129629846662285], [0.04312499910593033, 0.18129629846662285]]






