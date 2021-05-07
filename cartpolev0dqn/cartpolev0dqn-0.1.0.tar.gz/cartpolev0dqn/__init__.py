from dqn import DQN
import gym

ENV_NAME = 'CartPole-v0'

def model():
    env = gym.make(ENV_NAME)
    return DQN(env)