
import time
start_time = time.time()

file = open('siddhartha.txt', 'r')

# make list of lines of text
text = []
for line in file:
	text.append(line)

#make list of chariters in book
l = [item for sublist in text for item in sublist]
chars = [item.lower() for item in l]

# make list of unique charicters in book
syms = list(set(chars))

# find probability of each symbol in syms
le = len(chars)
plist = []
i=0
for j in syms:
	p = float(chars.count(j))/le
	plist.append([p,syms[i]])
	i += 1

#*********** sum of probs -> should equal 1 ***********
i = 0
t = 0
for j in plist:
	t = t + j[0]
	i += 1
print t
#*********** sum of probs -> should equal 1 ***********

#sort list of syms based on probability
sortedlist = sorted(plist)
print len(syms)

#assign code based on probability of syms
def mktree(slist):

	if len(slist) <= 1:
		return
	
	half = 0
	sub1 = []
	sub0 = []
	j = 0
	for ele in slist:
		half += ele[0]
		if half >= sum([g[0] for g in slist])/2:
			sub1.append(ele)
			slist[j].append('1')
		else:
			sub0.append(ele)
			slist[j].append('0')
		j += 1
	mktree(sub1)
	mktree(sub0)
	return slist

#run code to make codes and join into strings
codedsyms = mktree(sortedlist)
for ele in codedsyms:
	ele[2] = ''.join(ele[2::])#[::-1] - to reverse string
	del ele[3:]

#print list of symbols with code
import pprint
#pprint.pprint(codedsyms)

#make dictionary with symbols and codes
keys = []
values = []
for item in codedsyms:
	keys.append(item[1])
	values.append(item[2])

dictionary = dict(zip(keys, values))
pprint.pprint(dictionary)

codedbooklist = []
for item in chars:
	codedbooklist.append(dictionary[item])

codedbook = ''.join(codedbooklist[::])
print len(codedbook)
print 6*len(chars)
print float(6*len(chars))/len(codedbook)

#reverse dictionary
res = dict((v,k) for k,v in dictionary.iteritems())

uncodedbook = []
uncodedsym = []
for item in codedbook:
	uncodedsym.append(item)
	sym = ''.join(uncodedsym[::])
	if sym in res:
		uncodedbook.append(res[sym])
		uncodedsym = []
print chars[::] == uncodedbook[::]
