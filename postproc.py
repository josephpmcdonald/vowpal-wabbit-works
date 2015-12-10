test = open("test.dat", "r")
pred = open("test.pred", "r")
strvals = pred.readlines()
n = len(strvals)

scores = [0]*n
for i, line in enumerate(strvals):
    scores[i] = float(line[:-1])

labels = [0]*n
for i, line in enumerate(test.readlines()):
    labels[i] = float(line[0])

tp = 0.
fp = 0.
fn = 0.
tn = 0.

for i in range(n):
    l = labels[i]
    p = scores[i]
    if l == 1 :
        if p > 0.5:
            tp += 1
        else:
            fn += 1
    else:
        if p > 0.5:
            fp += 1

err = (fp + fn)/n
pre = tp/(tp + fp)
rec = tp/(tp + fn)

print "error: ", err
print "pre: ", pre
print "rec: ", rec



