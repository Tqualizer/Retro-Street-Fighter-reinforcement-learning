## Run the selected game and state from here

import gym
import retro
from stable_baselines.common.policies import MlpPolicy, CnnPolicy
from ppo2template import PPO2
from brute import TimeLimit

env = retro.make('StreetFighterIISpecialChampionEdition-Genesis', 'Champion.Level1.RyuVsGuile.state', use_restricted_actions=retro.Actions.DISCRETE)
env = TimeLimit(env, max_episode_steps=1500)

model = PPO2(MlpPolicy, env, n_steps=1500,verbose=1).learn(6000)
#model.save("ppo2_sf")

#del model # remove to demonstrate saving and loading

#model = PPO2.load("ppo2_sf")

# Enjoy trained agent
obs = env.reset()
#while True:
#    action, _states = model.predict(obs)
#    obs, rewards, dones, info = env.step(action)
#    env.render()
#    env.render()