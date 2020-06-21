
#########################################################################################
"""                                                                                     #
This code was originally written by cxy1997                                             #
I have made some changes to the code.                                                   #
As long as names of the authors are mentioned: modification, redistribution is permitted#
"""                                                                                     #
#########################################################################################     


#import the libraries
import numpy as np
import os
import time
import sys
import gym
from gym import error, spaces, utils
import copy
from gym.utils import seeding
import matplotlib.pyplot as plt

#making gym environment

COLORS = {0:[0.0,0.0,0.0], 1:[0.5,0.5,0.5], 
          2:[0.0,0.0,1.0], 3:[0.0,1.0,0.0], 
          4:[1.0,0.0,0.0], 6:[1.0,0.0,1.0], 
          7:[1.0,1.0,0.0]}


class GridEnv(gym.Env):
    
    num_env = 0
    metadata = {'render.modes': ['human']}
    
    def __init__(self):
        
        #action space
        self.actions = ['up', 'down', 'right', 'left', 'begin']
        self.inv_actions = ['begin', 'down','up','left','right']
        self.actions_pos_dict = {up:[-1,0], down:[1,0], right:[0,-1], left:[0,1], begin:[0,0]}
        self.action_space = spaces.Discrete(5)
        
        
        #observation space
        self.obs_shape = [128, 128, 3]
        self.observation_space = spaces.Box(low=0, high=1, shape=self.obs_shape, dtype=np.float32)
        
        
        #construct the grid 
        file_path              = os.path.dirname(os.path.realpath(__file__))
        self.insert_grid_map   = os.path.join(file_path, 'map2.txt')
        self.initial_map       = self.read_grid_map(self.insert_grid_map)
        self.current_map       = copy.deepcopy(self.initial_map)
        self.observation       = self.grid_map_observation(self.initial_map)
        self.grid_shape = self.initial_map.shape
        
        #agent actions
        self.start_state, self.target_state = self.get_agent_states(self.initial_grid)
        self.agent_state = copy.deepcopy(self.start_state)
        
        #other params
        self.verbose=False
        
        #env parameters
        self.reset()
        self.viewer()
        self.seed()
        
        #function makes the obstacles
        def make_obstacles(self, obstacles):
            """
            add obstacles using matplotlib
            """
            self.obstacle_mask = obstacle_mask
        return obstacle_mask
    
        #seeding
        def seed(self, seed=None):
            self.np_random, seed = seeding.np.random(seed)
            return [seed]
        
        def render(self):
            
            GridEnv.num_env +=1
            self.fig_num = GridEnv.num_env
            if self.verbose == True:
                self.fig = plt.figure(self.fig_num)
                plt.show(block=False)
                plt.axis('off')
                
        def step(self, action):
            
            action = self.actions
            reward_dict = {'up':10, 'down':10, 'left':10, 'right':10, 'begin':0, 'obstacle':-5}
        
            next_state = (self.agent_state[0]+self.actions_pos_dict[actions][0],
                          self.agent_state[1]+self.actions_pos_dict[actions][1] )
            
            if action == "up":
                return (self.observation, reward_dict.value[0], action)
            
            elif action == "down":
                return (self.observation, reward_dict.value[1], action)
            elif action == "right":
                return (self.observation, reward_dict.value[2], action)
            
            elif action == "left":
                return (self.observation, reward_dict.value[3], action)
            else:
                return (self.observation, reward_dict.value[4])#the agent begins from start position
            
            
            #out of bounds condition
            if next_state[0] < 0 or next_state[0] >= self.grid_shape[0]:
                return (self.observation, "This state is out of bounds")
            
            elif next_state[1] <0 or next_state[1] >= self.grid_shape[1]:
                
                return (self.observation, "This state is out of bounds")
                
            #obstacle avoidance
            iterations =10
            for i in range(iterations):
                for j in range(obstacles):
                    if next_state[i] == self.obstacle_mask[j]:
                        start == [0,0]
                        next_state == start
                        
                        return (self.observation, next_state, reward_dict.value[5])
                    #condition for starting again
                    elif next_state == "begin":
                        self.observation = self.reset()
                        return (self.observation, reward_dict.value[4])
                    
                       
        def reset(self):
            self.agent_state = copy.deepcopy(self.start_state)
            self.current_map = copy.deepcopy(self.initial_map)
            self.observation = self.grid_map_observation(self.initial_map)

            self.render()
            return self.observation
        
        
        def read_grid_map(self, insert_grid_map):
            with open(insert_grid_map, 'r') as f:
                
                grid_map = f.readlines()
                grids = np.array(list(map(lambda x: 
                        list(map(lambda y: int(y), 
                    x.split(''))), grid_map)))
                
                return grids
            
        def get_agent_states(self):
            
            start_state  = None
            target_state = None
            start_state = list(map(lambda x:x[0] if len(x) > 0 else None, np.where(insert_grid_map==4)))
            
            target_state = list(map(lambda x:x[0] if len(x) > 0 else None, np.where(insert_grid_map==3)))
            
            if (start_state == [None, None] or target_state == [None, None]):
                sys.exit('Start or Target state not specified')
            
            if (start_state == self.obstacle_mask):
                sys.exit('Obstacle encountered GAME OVER !!!')
                
                return start_state, target_state
            
            
                
        def grid_map_to_observation(self, grid_map, obs_shape=None):
            
            if obs_shape is None:
                
                obs_shape = self.obs_shape
                
            observation = np.zeros(obs_shape, dtype=np.float)
            gs0 = int(observation.shape[0]/ grid_map.shape[0])
            gs1 = int(observation.shape[1]/ grid_map.shape[1])
            
            for i in range(grid_map.shape[0]):
                for j in range(grid_map.shape[1]):
                    
                    observation[i*gs0:(i+1)*gs1, j*gs0:(j+1)*gs1]
                    
            return observation
        
        def _render_(self, mode='human', close=False):
            
            if self.verbose == False:
                
                return
            img = self.observation
            fig = plt.figure(self.fig_num)
            plt.clf()
            plt.imshow(img)
            fig.canvas.draw()
            plt.pause(0.0002)
            return
        
        #configuring agent's states
        
        def _get_agent_state(self):

            return self.agent_state
        
        def get_agent__start_target_state(self):
            
            return self.start_state, self.target_state
        
        
        def jump_to_a_state(self, to_state):
            
            if self.current_map[to_state[0], to_state[1]] == self.current_map[self.obstacle_mask[0], self.obstacle_mask[1]]:
                    sys.exit("GAME OVER")
                    
            elif self.current_map[to_state[0], to_state[1]] == 0:
                
                if self.current_map[agent_state[0], agent_state[1]] == 4:
                    
                    self.current_map[agent_state[0], agent_state[1]] += self.actions_pos_dict[actions][2]
                    self.observation = self.grid_map_to_observation(self.current_map)
                    self.agent_state = [to_state[0], to_state[1]]
                    self._render_()
                    return (self.observation, agent_state)
                    
                if self.current_map[agent_state[0], agent_state[1]]== 6:
                    
                    self.current_map[agent_state[0], agent_state[1]] += self.actions_pos_dict[actions][1]
                    self.observation = self.grid_map_to_observation(self.current_map)
                    self.agent_state = [to_state[0], to_state[1]]
                    self._render_()
                    return (self.observation, agent_state)
                
                if self.current_map[agent_state[0], agent_state[1]]== 7:
                    
                    self.current_map[agent_state[0], agent_state[1]] += self.actions_pos_dict[actions][3]
                    self.observation = self.grid_map_to_observation(self.current_map)
                    self.agent_state = [to_state[0], to_state[1]]
                    self._render_()
                    return (self.observation, agent_state)
            
            elif self.current_map[to_state[0], to_state[1]] is None:
                
                    return ("Invalid state")
                
            """
            please add the to_state if condition for the remaining states i.e 4, 1, 3, and 7.
            
            """
            
            def close(self):
                plt.close(1)
                return 
            
                     



