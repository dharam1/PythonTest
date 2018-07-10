f = open('input.txt', 'r')
o = open('output.txt','w')
try:
    count = {}
    for i in f:
    	s = i.split()
    	for j in s:
    		if(j in count):
    			count[j] +=1
    		else:
    			count[j] = 1
    result = sorted(count.keys())
    for i in result:
    	s= str(i+ " -> " + str(count[i]))
    	o.write(s)
    	o.write('\n')
finally:
    f.close()
    o.close()