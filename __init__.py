from gym.envs.registration import register

register(
        id = 'Grid-v0',
        entry_point='Grid.envs:GridEnv')

