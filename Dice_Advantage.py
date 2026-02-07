###############################################################################
### Determine the average of rolling d N-sided dice and taking the maximum
###############################################################################

"""
The average can be found algebraically by noting that the probability of the max
roll on d N-sided dice being n is P = P('all <= n') - P('all < n'). This gives
P = (n/N)^d - ((n-1)/N)^d. Then, the expectation formula is E = sum_1^N n*P_n.
This is what is solved for below.
"""

N = int(input("How many sides are on the die? "))
d = int(input("How many dice are being rolled? "))

sum = 0
for i in range(N):
    n = i+1
    sum = sum + n**(d+1) - n*(n-1)**d

E = sum/N**d

print("The average is", E)
