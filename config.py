
# DO NOT EDIT

# Assignment for 18xz85

from lib204 import wff
P, Q, R, S, T = map(wff.Variable, 'PQRST')
s1 = (~P|(R|S))
s2 = ((~R|S)&(~S|~R))
s3 = (P|(~S|~R))
s4 = ((P|~R)&(~R|~P))

s5 = ((S>>P)>>((P&~S)|R))
s6 = ((~P>>(~S&R))|~(S|~P))
