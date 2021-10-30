probabilities1 = {
    "Bull": {
        "Bull": .9,
        "Bear": .07,
        "Recession": .03
    },
    "Bear": {
        "Bull": .8,
        "Bear": .1,
        "Recession": .1
    },
    "Recession": {
        "Bull": .1,
        "Bear": .4,
        "Recession": .5
    }
}

probabilities2 = {
    "Bull": [.9, .07, .03],
    "Bear": [.1, .8, .1],
    "Recession": [.5, .1, .4]
}

''' Using the model above, write a function to return the next state
when given a current state.
'''
'''
Pseudo code:
1. we need to know the state we're in (input)
2. From the input, we have three choices. We need to assign the probabilities,
choose from one of our choices and return once of those three states.
3. We need to return the state that we're going into.
'''

#let's import a tool that helps us select between our probabilities randomly:
import random
from random import choices

def markov_function(our_data, current_state):

    # choices(economic_states, weights=None, k=1)
    # population is a list
    # weights is also a list
    our_choices = list(our_data.keys())
    #let current_state = Bull
    our_weights = list(our_data[current_state].values())
    next_state = choices(our_choices, weights=our_weights)
    print('next state', next_state)
    chose_ten = choices(our_choices, weights=our_weights, k=10)
    print("choose ten", chose_ten)

    return next_state

markov_function(probabilities1, "Bull")