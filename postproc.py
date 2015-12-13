import sys

test = open("test.dat", "r")
pred = open("test.pred", "r")
strvals = pred.readlines()
n = len(strvals)
w_bool = bool(sys.argv[1] and sys.argv[2])
if w_bool:
    w_pos = float(sys.argv[1])
    w_neg = float(sys.argv[2])
else:
    print "input weights"
    exit()

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
            tp += w_pos
        else:
            fn += w_pos
    else:
        if p > 0.5:
            fp += w_neg
        else:
            tn += w_neg

tot = tp + fp + tn + fn
err = (fp + fn)/tot
pre = tp/(tp + fp)
rec = tp/(tp + fn)

print "err: ", err
print "pre: ", pre
print "rec: ", rec



