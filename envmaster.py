## Run the selected game and state from here

import gym
import retro
from stable_baselines.common.policies import MlpPolicy, CnnPolicy
from ppo2template import PPO2
from brute import TimeLimit
from discretizer import SF2Discretizer


env = retro.make('StreetFighterIISpecialChampionEdition-Genesis', 'Champion.Level1.RyuVsGuile.state',obs_type = retro.Observations.IMAGE) #change to compare IMAGE to RAM observations
env = SF2Discretizer(env)
env = TimeLimit(env, max_episode_steps=2500)

model = PPO2(MlpPolicy, env, n_steps=2500,verbose=2).learn(75000) #put the selected policy and episode steps in here.
model.save("ppo2_esf")

#del model # remove to demonstrate saving and loading

#model = PPO2.load("ppo2_esf") # load a saved file

# Enjoy trained agent
obs = env.reset()
timesteps = 0
totalrewards = 0.0
#env.unwrapped.record_movie("PPOII.bk2") #to start saving the recording
while True: 
    action, _states = model.predict(obs)
    timesteps = timesteps + 1
    obs, rewards, dones, info = env.step(action)
    totalrewards = totalrewards + rewards
    env.render() #watch the prediction of the trained model
#    if timesteps > 2500: # to limit the playback length
#        print("timestep limit exceeded.. score:", totalrewards)
#        break
#env.unwrapped.stop_record() # to finish saving the recording