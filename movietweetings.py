#convert MovieTweetings format to vw format
from sys import platform
from random import random

p = 0.1

if platform == "darwin":
    prepath = "/Users/josephpmcdonald/Documents/"
elif platform == "linux2":
    prepath = "/scratch/"
else:
    exit("Provide input location")

r_file = open(prepath+"MovieTweetings-master/latest/ratings.dat","r")
w_file = open(prepath+"MovieTweetings-master/latest/ratings.vw","w")
t_file = open(prepath+"MovieTweetings-master/latest/test.vw","w")

for line in r_file:
    l = line.rstrip().split("::")
    if random() > p:
        w_file.writelines("%s |u %s |i %s\n"%(l[2], l[0], l[1]))
    else:
        t_file.writelines("%s |u %s |i %s\n"%(l[2], l[0], l[1]))

r_file.close()
w_file.close()
t_file.close()



