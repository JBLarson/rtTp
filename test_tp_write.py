import matplotlib.pyplot as plt
import numpy as np
import sys

g = lambda r, o : round(r*(o-1), ndigits=2)

pt_rng = np.arange(35, 56) #upper and lower parameters for visual
contract = 'NE/KC ' #name of event

b1a, s1a = True, False #Alternate Wager choice

if b1a == True: b1s,b1o,b1r = float(42), float(1.67), float(30)
elif b1a == False: b1s,b1o,b1r = float(44), float(1.87), float(145)
if s1a == True: s1s,s1o,s1r = float(46), float(1.87), float(55)
elif s1a == False: s1s,s1o,s1r = float(49), float(1.67), float(65)

b1w, b2w = g(b1r,b1o), g(s1r,s1o)

b1_rez = [b1w if n >= b1s else -b1r for n in pt_rng]
s1_rez = [b2w if pt < s1s else -s1r for pt in pt_rng]
net_rez = [round((b1_rez[i]+s1_rez[i]),ndigits=2) for i in range(len(b1_rez))]

b1T, s1T = "Over "+contract+str(b1s), "Under "+contract+str(s1s)

def test_tp_write():
	sys.stdout = open('rezults.txt', 'wt')
	for n in range(0,len(pt_rng)):
		print(pt_rng[n], ',', net_rez[n])

	sys.stdout = open('b1s1.txt', 'wt')
	for n in range(0,len(pt_rng)): print(b1_rez[n], ',', s1_rez[n])

	sys.stdout = open('positions.txt', 'wt')
	print(b1T)
	print(s1T)

test_tp_write()

