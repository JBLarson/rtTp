import matplotlib.pyplot as plt
import numpy as np

g = lambda r, o : r*(o-1)
ro = lambda x : round(x, ndigits=2)
rp = lambda n : round(n, ndigits=4)


#Forex: buy / Sports-Wager: over


#b1s,b1o,b1r = float(42), float(1.67), float(30)
b1s,b1o,b1r = float(44), float(1.87), float(145)
#b1s,b1o,b1r = float(46), float(1.952), float(20)



#Forex: sell / Sports-Wager: under


#b2s,b2o,b2r = float(45), float(1.952), float(45)
b2s,b2o,b2r = float(47), float(1.87), float(55)
#b2s,b2o,b2r = float(49), float(1.67), float(65)




b1w, b2w = ro(g(b1r,b1o)), ro(g(b2r,b2o))

pt_rng = np.arange(35, 55)


b1_rez = [b1w if n >= b1s else -b1r for n in pt_rng]
s1_rez = [b2w if pt < b2s else -b2r for pt in pt_rng]

net_rez = [ro(b1_rez[i]+s1_rez[i]) for i in range(len(b1_rez))]
all_rez = [b1_rez, s1_rez, net_rez]

#b1T, b2T = inp.b1T, inp.b2T




import sys

sys.stdout = open('rezults.txt', 'wt')


"""
for n in range(0,10):
	eval(f'print(pt_rng[{n}]), \',\', print(net_rez[{n}])')
"""


print(pt_rng[0], ',', net_rez[0])
print(pt_rng[1], ',', net_rez[1])
print(pt_rng[2], ',', net_rez[2])
print(pt_rng[3], ',', net_rez[3])
print(pt_rng[4], ',', net_rez[4])
print(pt_rng[5], ',', net_rez[5])
print(pt_rng[6], ',', net_rez[6])
print(pt_rng[7], ',', net_rez[7])
print(pt_rng[8], ',', net_rez[8])
print(pt_rng[9], ',', net_rez[9])
print(pt_rng[10], ',', net_rez[10])
print(pt_rng[11], ',', net_rez[11])
print(pt_rng[12], ',', net_rez[12])
print(pt_rng[13], ',', net_rez[13])
print(pt_rng[14], ',', net_rez[14])
print(pt_rng[15], ',', net_rez[15])
print(pt_rng[16], ',', net_rez[16])
print(pt_rng[17], ',', net_rez[17])
print(pt_rng[18], ',', net_rez[18])
print(pt_rng[19], ',', net_rez[19])




#print(pt_rng[10], ',', net_rez[10])
#print(pt_rng[11], ',', net_rez[11])
sys.stdout = open('b1s1.txt', 'wt')


"""
for n in range(0,10):
print(b1_rez[n]), ',', print(s1_rez[n])
"""

print(b1_rez[0], ',', s1_rez[0])
print(b1_rez[1], ',', s1_rez[1])
print(b1_rez[2], ',', s1_rez[2])
print(b1_rez[3], ',', s1_rez[3])
print(b1_rez[4], ',', s1_rez[4])
print(b1_rez[5], ',', s1_rez[5])
print(b1_rez[6], ',', s1_rez[6])
print(b1_rez[7], ',', s1_rez[7])
print(b1_rez[8], ',', s1_rez[8])
print(b1_rez[9], ',', s1_rez[9])
print(b1_rez[10], ',', s1_rez[10])
print(b1_rez[11], ',', s1_rez[11])
print(b1_rez[12], ',', s1_rez[12])
print(b1_rez[13], ',', s1_rez[13])
print(b1_rez[14], ',', s1_rez[14])
print(b1_rez[15], ',', s1_rez[15])
print(b1_rez[16], ',', s1_rez[16])
print(b1_rez[17], ',', s1_rez[17])
print(b1_rez[18], ',', s1_rez[18])
print(b1_rez[19], ',', s1_rez[19])
