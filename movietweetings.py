
r_file = open("/scratch/MovieTweetings-master/latest/ratings.dat","r")
w_file = open("/scratch/MovieTweetings-master/latest/ratings.vw","w")
for line in r_file:
    l = line.rstrip().split("::")
    w_file.writelines("%s |u %s |i %s\n"%(l[2], l[0], l[1]))

r_file.close()
w_file.close()


