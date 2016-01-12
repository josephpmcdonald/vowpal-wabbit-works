from random import random
import sys

p = 0.1

prepath = "/scratch/ml-20m/"
r_file = open(prepath+"ratings.vw","r")
tr_file = open(prepath+"train.vw","w")
te_file = open(prepath+"test.vw","w")

for line in r_file:
    if random() > p:
        tr_file.writelines(line)
    else:
        te_file.writelines(line)

r_file.close()
tr_file.close()
te_file.close()


