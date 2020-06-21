# Gridworld

A grid-based environment for single agent systems based on openAI-gym.

![Logo](https://github.com/addy1997/Gridworld/blob/master/Figures/default%202.21.27%20PM.png)

[![Software License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](LICENSE)  [![Build Status](https://ci.appveyor.com/api/projects/status/8e784doc5sye7c41?svg=true)](https://ci.appveyor.com/project/addy1997/Gridworld) [![Stars](https://img.shields.io/github/stars/addy1997/Gridworld.svg?style=flat&label=Star&maxAge=86400)](STARS)  [![Contributions](https://img.shields.io/github/commit-activity/m/addy1997/Gridworld.svg?color=%09%2346c018)](https://github.com/addy1997/Gridworld/graphs/commit-activity)  [![Dependency Status](https://david-dm.org/addy1997/Gridworld.svg)](https://david-dm.org/addy1997/Gridworld)                 

***Installation***
```shell
pip3 install -i https://test.pypi.org/simple/ Gridworld==0.0.1
```

***Alternative installation***
```shell
cd $HOME
git clone https://github.com/addy1997/Gridworld.git
cd Gridworld
virtualenv venv
source ./venv/bin/activate
pip install -e .
```

Note: you will get this message after installation(given below). This validates that the package installation is done properly. 

![drube](https://github.com/addy1997/Gridworld/blob/master/Figures/Screenshot%202020-06-21%20at%2012.35.27%20AM.png)

**For errors**

Visit this _[link](https://github.com/donnemartin/gitsome/issues/4)_

## You might encouter this problem after installing and sourcing the env on your machine

_You do not need to modify baselines repo._

Here is a minimal example. Say you have myenv.py, with all the needed functions (step, reset, ...). The name of the class environment is MyEnv, and you want to add it to the classic_control folder. You have to

    * Place myenv.py file in gym/gym/envs/classic_control

    * Add to __init__.py (located in the same folder)

    * from gym.envs.classic_control.myenv import MyEnv

    * Register the environment in gym/gym/envs/__init__.py by adding

    gym.envs.register(
         id='MyEnv-v0',
         entry_point='gym.envs.classic_control:MyEnv',
         max_episode_steps=1000,
    )

_At registration, you can also add reward_threshold and kwargs (if your class takes some arguments).
You can also directly register the environment in the script you will run (TRPO, PPO, or whatever) instead of doing it _

_in gym/gym/envs/__init__.py._

**Testing**
```shell
import Gridworld
import gym 
env = gym.make('Gridworld-v0')
```

Feel free to raise an issue for errors.

