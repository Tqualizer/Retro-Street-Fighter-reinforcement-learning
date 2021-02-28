"""
Define discrete action spaces for Gym Retro environments with a limited set of button combos
"""

import gym
import numpy as np
import retro

class Discretizer(gym.ActionWrapper):
    """
    Wrap a gym environment and make it use discrete actions.
    Args:
        combos: ordered list of lists of valid button combinations
    """

    def __init__(self, env, combos):
        super().__init__(env)
        assert isinstance(env.action_space, gym.spaces.MultiBinary)
        buttons = env.unwrapped.buttons
        self._decode_discrete_action = []
        for combo in combos:
            arr = np.array([False] * env.action_space.n)
            for button in combo:
                arr[buttons.index(button)] = True
            self._decode_discrete_action.append(arr)

        self.action_space = gym.spaces.Discrete(len(self._decode_discrete_action))

    def action(self, act):
        return self._decode_discrete_action[act].copy()


class SF2Discretizer(Discretizer):
    """
    Use Sonic-specific discrete actions
    based on https://github.com/openai/retro-baselines/blob/master/agents/sonic_util.py
    """
    def __init__(self, env):
        super().__init__(env=env, combos=[[],['DOWN'],['DOWN','LEFT'],['LEFT'],['DOWN'],['DOWN','RIGHT'],['RIGHT'],['UP','RIGHT'],['UP','LEFT'],['A'],['B'],['C'],['X'],['Y'],['Z']])

def main():
    env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis',state='Champion.Level1.RyuVsGuile.state', use_restricted_actions=retro.Actions.DISCRETE)
    print('retro.Actions.DISCRETE action_space', env.action_space)
    env.close()

    env = retro.make(game='StreetFighterIISpecialChampionEdition-Genesis', state= 'Champion.Level1.RyuVsGuile.state',)
    env = SF2Discretizer(env)
    print('SF2Discretizer action_space', env.action_space)
    env.close()


if __name__ == '__main__':
    main()