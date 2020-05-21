#!/usr/bin/env python
# coding: utf-8

# In[54]:


import numpy as np
import random
import Grid
from Grid import *


class DynamicProgramming:
    """
    class for performing value iteration
    """
    def __init__(self):
        
        self.lambda = 0.9
        self.env = Grid.GridEnv()
        self.theta = 0.044
        
    def One_step_search(self, state, Value):
        """
        Function for calculating the value function v(s)
        -----------
        Function parameters
        --------------
        state: current state, for example, say s: coordinates [x,y]
        V: value function: array
        A: all possible actions: array/ list
        
        """
        Action_list = np.arrays(self.env.actions)
        for actions in range(self.env.actions):
            
            for prabability, next_state, reward, done in self.env.array[state][actions]:
            
                Action_list[actions] += probability*(reward + self.lambda*V[next_state])
            
            return Action_list
        
        
    def iterative_policy_evaluation(self):
        V = np.zeros(self.env.agent_state)
        while True:
            
            Del =0
            for states in range(self.env.agent_state):
                Action_list = self.One_step_search(states, V)
                A_max = np.max(Action_list)
                Del = np.max(Del, np.abs(A_max-V[states]))
                V[states] = A_max
                
                if Del < self.theta
                break
                else:
                    return V[states]
                
    if __name__ == '__main__':
        
        dynaprog= DynamicProgramming('')
        policy, Value_fuction = dynaprog.iterative_policy_evaluation()
        
        print("the policy is", policy)
        print("the value function is", Value_function)







