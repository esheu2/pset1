0

a) Collaborators:
Everett Sheu
Aditi Mittal
Gabriel Baltazar

b) Resources:
class notes
took inspiration from http://aima.cs.berkeley.edu/python/mdp.html


1

a) state space size = H*L
b) action space size = 5
c) mdp_prob(). It is denoted in a commented section in the code


2

Parts are denoted in commented sections in the code
a) mdp_prob()
b) expected_reward()


3

Parts are denoted in commented sections in the code
a) Near the top with the initialization and global variables
b)show_policy()
c)policy_evaluation()
d)bellman()
e)policy_iteration() and expected_utility()
f)
g)


5

a)
As the probability of error goes up, the prioritized path is led further from the red spaces so as to avoid accidentally entering them. In other words, it prioritizes "safety"

As the discount factor is decreased, the prioritized path becomes more direct and faster. This led the path to ride against the red squares. In other words, it prioritized speed and efficiency.
