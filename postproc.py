import sys

test = open("test.dat", "r")
pred = open("test.pred", "r")
strvals = pred.readlines()
n = len(strvals)

#scores = [0]*n
#for i, line in enumerate(strvals):
#    scores[i] = float(line)
#
#labels = [0]*n
#for i, line in enumerate(test.readlines()):
#    labels[i] = float(line[0])

tp = 0.
fp = 0.
fn = 0.
tn = 0.

for i in range(n):
    p = float(strvals[i])
    line = test.readline().split()
    l = int(line[0])
    w = float(line[1])

    #l = labels[i]
    #p = scores[i]

    if l == 1:
        if p > 0.5:
            tp += w
        else:
            fn += w
    else:
        if p > 0.5:
            fp += w
        else:
            tn += w

tot = tp + fp + tn + fn
err = (fp + fn)/tot
pre = tp/(tp + fp)
rec = tp/(tp + fn)

print "err: ", err
print "pre: ", pre
print "rec: ", rec

test.close()
pred.close()

