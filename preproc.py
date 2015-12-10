import re
import sys
import random


p = float(sys.argv[1])
if p < 0 or p > 1:
    print "input valid p, 0<=p<=1"
    exit()

w_bool = bool(sys.argv[2] and sys.argv[3])
if w_bool:
    w_pos = float(sys.argv[2])
    w_neg = float(sys.argv[3])

train = open("train.dat","w")
test = open("test.dat","w")

for i in range(1):
    with open("/scratch/url_svmlight/Day"+str(i)+".svm","r") as f:
        for line in f:
            if w_bool:
                newline = re.sub(r"^-1", "0 %f |f"%w_neg, line)
                newline = re.sub(r"^\+1", "1 %f |f"%w_pos, newline)
                newline = re.sub(r"$\s", " const:.01\n", newline)
            else:
                newline = re.sub(r"^-1", "0 |f", line)
                newline = re.sub(r"^\+1", "1 |f", newline)
                newline = re.sub(r"$\s", " const:.01\n", newline)

            rand = random.random()
            if rand < p:
                test.write(newline)
            else:
                train.write(newline)

            #exit()

train.close()
test.close()



