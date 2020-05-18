#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gym.envs.registration import register

register(
        id = 'Grid-v0',
        entry_point='Grid.envs:GridEnv')

