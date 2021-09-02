import os
from collections import OrderedDict

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
# bbFile.remove('.DS_Store')
print(bbFile)


for bb in bbFile:
	with open("/Users/anjalisingh/Desktop/edge_detection/Automation/BoundingBox/"+str(bb)) as f:
	    line = f.readlines()
	    location = dict()
	    f = open("static/"+bb, 'a')
	    for x in line:
	        if x[0] == "V":
	            # print("Segment changed")
	            location = OrderedDict(sorted(location.items()))

	            for l in location:
	                al, bl, cl, dl = l[0], l[1], l[2], l[3]
	                for k in location:
	                    if k!=l:
	                        ak, bk, ck, dk = k[0], k[1], k[2], k[3]
	                        x1, y1 = abs(al[0]-ak[0]), abs(al[1]-ak[1])
	                        x2, y2 = abs(bl[0]-bk[0]), abs(bl[1]-bk[1])
	                        x3, y3 = abs(cl[0]-ck[0]), abs(cl[1]-ck[1])
	                        x4, y4 = abs(dl[0]-dk[0]), abs(dl[1]-dk[1])
	                        if x1<=5 and y1<=5 and x2<=5 and y2<=5 and x3<=5 and y3<=5 and x4<=5 and y4<=5:
	                            location[l] = location[l] + 1
	            for l in location:
	                if location[l]>2:
	                    for (x, y) in l:
	                        for d in detect:
	                            if (x<detect[d][0] and y<detect[d][1] and y>(detect[d][1]-135) and x>(detect[d][0]-240) and detect[d][2]==False):
	                                f.write(str(d)+" ")
	                                detect[d][2] = True
	                    print(l,location[l])
	            location = dict()
	            f.write("\n")
	            continue
	        else:
	            x = x.split(' ')[1:5]
	            x[0], x[1], x[2], x[3] = float(x[0]), float(x[1]), float(x[2]), float(x[3])
	            points = [[x[0]-x[2]/2, x[1]+x[3]/2], [x[0]+x[2]/2, x[1]+x[3]/2], [x[0]-x[2]/2, x[1]-x[3]/2], [x[0]+x[2]/2, x[1]-x[3]/2]]
	            points = [tuple([round(points[0][0]*960),round(points[0][1]*540)]), tuple([round(points[1][0]*960), round(points[1][1]*540)]), tuple([round(points[2][0]*960), round(points[2][1]*540)]), tuple([round(points[3][0]*960), round(points[3][1]*540)])]
	            points = tuple(points)
	            # print(points)
	            if points not in location.items():
	                location[points] = 1
	            else:
	                location[points] = location[points] + 1
	# for l in location:
	#         print(l, location[l])
	location = OrderedDict(sorted(location.items()))

	for l in location:
	    # print(l)
	    al, bl, cl, dl = l[0], l[1], l[2], l[3]
	    for k in location:
	        if k!=l:
	            ak, bk, ck, dk = k[0], k[1], k[2], k[3]
	            x1, y1 = abs(al[0]-ak[0]), abs(al[1]-ak[1])
	            x2, y2 = abs(bl[0]-bk[0]), abs(bl[1]-bk[1])
	            x3, y3 = abs(cl[0]-ck[0]), abs(cl[1]-ck[1])
	            x4, y4 = abs(dl[0]-dk[0]), abs(dl[1]-dk[1])
	            if x1<=4 and y1<=4 and x2<=4 and y2<=4 and x3<=4 and y3<=4 and x4<=4 and y4<=4:
	                 location[l] = location[l] + 1






