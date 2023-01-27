# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 13:46:35 2020
@author: Ruby
"""
headline = input()  # news title file
ndict = input()  # keyword dictionary file
compcat = input()  # company industry file
crit = input().split(',')
target = crit[0]  # target industry stock
targetq = int(crit[1])  # target amount
rquant = crit[2].split(':')  # amount allocation
for r in range(len(rquant)):
    rquant[r] = int(rquant[r])
fh0 = open(headline, 'r', encoding='utf-8')
fh1 = open(ndict, 'r', encoding='utf-8')
fh2 = open(compcat, 'r', encoding='utf-8')

# save news title for querying
stringlist = []
for string in fh0:
    string = string.split(' ')
    string = ''.join(string)
    stringlist.append(string)

# make keyword weight into dictionary
newsdict = dict()
for d in fh1:
    d = d.strip('\n')
    d = d.split(' ')
    newsdict[d[0]] = int(d[1])
newsdict = sorted(newsdict.items(), reverse=True, key=lambda x: len(x[0]))

# make company stock and stock type into dictionary
stocktype = dict()
for s in fh2:
    s = s.strip('\n')
    s = s.split(' ')
    if s[1] not in stocktype:
        stocktype[s[1]] = [s[0]]
    else:
        stocktype[s[1]].append(s[0])

# calculate score for stock type
score = dict()
for t in stocktype[target]:
    for s in stringlist:
        # find company name
        comp = s.find(t)
        if comp == -1:
            continue
        else:
            # calculate keyword weight if company name exist
            for d in newsdict:
                kindex = s.find(d[0])
                # continue if keyword not in title
                if kindex == -1:
                    continue
                else:
                    # calculate company score
                    if t not in score:
                        score[t] = d[1]
                    else:
                        score[t] += d[1]

# rank companies by score
sorted_comp = sorted(score.items(), key=lambda x: (x[1], x[0]), reverse=True)
sorted_comp = sorted_comp[:len(rquant)]

# calculate final buying decision
finalbuy = dict()
for i in sorted_comp:
    finalbuy[i[0]] = 0
while targetq >= 0:
    for c in range(len(sorted_comp)):
        # if expected buy amount more than allocated stock amount
        if targetq >= rquant[c]:
            # buy allocated stock amount
            finalbuy[sorted_comp[c][0]] += rquant[c]
        else:
            # or else purchase rest of the expected buy amount
            finalbuy[sorted_comp[c][0]] += targetq
        targetq -= rquant[c]
        if targetq < 0:
            break

if target not in stocktype:
    print('NO_MATCH')
else:
    for i in sorted_comp:
        if finalbuy[i[0]] == 0:
            pass
        else:
            txt = '{}購買{}張'.format(i[0], finalbuy[i[0]])
            print(txt)
