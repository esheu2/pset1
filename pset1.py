import numpy as np

actions = R, U, L, D, N = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]


Length = 5   # grid length
Height = 6   # grid height
p_err = 0.01  # error rate
gamma = 0.9     # discount factor

# State space is size H*L
# which is 30 in this case

#2a
grid = np.zeros((Length,Height))
obstacles = [(1,1),(1,3),(2,1),(2,3)]
# populating rewards
grid[2,0] = 10
grid[2,2] = 1
grid[4] = -100

# 3a: creating the initial policy to always take left step
policy = {}
for i in range(Length):
    for j in range(Height):
        policy[(i,j)] = L

init = (1,2)   # initialize state
state = init    # state
probability = 1

#1a,1b,1c,2a
def mdp_prob(state, action, next_state):
    """
    Update the state

    Inputs:
    - state: 2x1 tuple of position on grid
    - action: Tuple consisting of values that would be added to position if the action is taken
    - next_state: 2x1 tuple of predicted position

    Return:
    - prob: returns the probability of arriving at the next_state
    """
    prob = 0
    if action == N:
        prob = 1
    else:
        if (state[0]+action[0])<Length and (state[0]+action[0])>=0 and (state[1]+action[1])<Height and (state[1]+action[1])>=0 and (state[0]+action[0], state[1]+action[1]) not in obstacles:
            if (state[0]+action[0], state[1]+action[1])==next_state:
                prob = (1-p_err) + p_err/4
            elif ((state[0]+1, state[1]+0)==next_state) or ((state[0]-1, state[1]+0)==next_state) or ((state[0]+0, state[1]+1)==next_state) or ((state[0]+0, state[1]-1)==next_state):
                prob = p_err/4
        else:
            prob = 0
    return prob

#2b
def expected_reward(state):
    return grid[state[0],state[1]]

#3b
def show_policy(pi):
    print(pi)
#3c
def policy_evaluation(pi):
    """
    Policy Evaluation

    Inputs:
    - pi: dict that is a mapping of state to action

    Return:
    - V: dict that is a utility mapping from each state to its utility
    """
    V = {}
    for i in range(Length):
        for j in range(Height):
            V[(i,j)] = 0

    for i in range(20):
        for j in range(Length):
            for k in range(Height):
                state = (j,k)
                temp_arr = [mdp_prob(state,pi[state],(state[0]+1,state[1]+0)),
                            mdp_prob(state,pi[state],(state[0]-1,state[1]+0)),
                            mdp_prob(state,pi[state],(state[0]+0,state[1]+1)),
                            mdp_prob(state,pi[state],(state[0]+0,state[1]-1))]
                V[state] = expected_reward(state) + gamma * sum([p * V[state] for p in temp_arr])

    return V

#3d
def expected_utility(action, state, V):
    temp_arr = [(mdp_prob(state,action,(state[0]+1,state[1]+0)),(state[0]+1,state[1]+0)),
    (mdp_prob(state,action,(state[0]-1,state[1]+0)),(state[0]-1,state[1]+0)),
    (mdp_prob(state,action,(state[0]+0,state[1]+1)),(state[0]+0,state[1]+1)),
    (mdp_prob(state,action,(state[0]+0,state[1]-1)),(state[0]+0,state[1]-1))]
    sum = 0
    for thing in temp_arr:
        p = thing[0]
        state_next = thing[1]
        if state_next[0] >= 0 and state_next[0] < Length and state_next[1] >= 0 and state_next[1] < Height and state_next not in obstacles:
            sum += p * V[state_next]
    return sum

def bellman(V,pi):
    """
    Gives the optimal policy under a one-step lookahead (Bellman backup)

    Inputs:
    - V: dict that is a utility mapping from each state to its utility

    Return:
    - pi: dict that is a mapping of state to action
    """

    for i in range(Length):
        for j in range(Height):
            state = (i,j)
            best = None
            for a in actions:
                utility = expected_utility(a,state,V)
                if best == None:
                    best = a,utility
                else:
                    if utility > best[1]:
                        best = a,utility
            if pi[state] != best[0]:
                pi[state] = best[0]
    return pi

#3e
def policy_iteration(pi):
    counter = 0
    while True:
        V = policy_evaluation(pi)
        temp = pi.copy()
        unchanged = True
        pi = bellman(V,pi)
        for i in range(Length):
            for j in range(Height):
                state = (i,j)
                if temp[state] != pi[state]:
                    unchanged = False
        if unchanged:
            return pi
        counter += 1
        print(counter)


#3b continuation. Showing pi_0, the initial policy
'''
show_policy(policy)
V = policy_evaluation(policy)
print(V)
bellman_policy = bellman(V)
print(bellman_policy)
'''
policy = policy_iteration(policy)
v = policy_evaluation(policy)
print(policy)
print(v)
