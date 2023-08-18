from operator import itemgetter
records=[['hen',50],['cat',45],['aod',39],['edw',45]]
record =sorted(records,key=itemgetter(0))
#print(record)
def function(iterable):
	t=[]
	for y in iterable:
		p=y[1]
		t.append(p)
	r=list(set(t))
	return r
	#print(r)
marks=function(record)
#print(marks[1])
def runnerup(runnerup_score,sample_space):
	runnerup_list=[]
	for x in sample_space:
		if x[1]==runnerup_score:
			p=x[0]
			print(p)
		else:
			pass
	return runnerup_list
runnerup(marks[1],record)