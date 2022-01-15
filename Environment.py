from __future__ import absolute_import, division, print_function

import base64
import imageio
import IPython
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
import pyvirtualdisplay
import reverb

import tensorflow as tf
from Gameplay import Gameplay
from Color import Color

from tf_agents.agents.dqn import dqn_agent
from tf_agents.drivers import py_driver
from tf_agents.environments import suite_gym
from tf_agents.environments import tf_py_environment
from tf_agents.eval import metric_utils
from tf_agents.metrics import tf_metrics
from tf_agents.networks import sequential
from tf_agents.policies import py_tf_eager_policy
from tf_agents.policies import random_tf_policy
from tf_agents.replay_buffers import reverb_replay_buffer
from tf_agents.replay_buffers import reverb_utils
from tf_agents.trajectories import trajectory
from tf_agents.specs import tensor_spec
from tf_agents.utils import common

# https://www.tensorflow.org/agents/tutorials/1_dqn_tutorial 
# we copied the tutorial code and modified some parts
# this class doesn't function properly yet

class Environment(tf_py_environment.PyEnvironment):

  def __init__(self):
    self._action_spec = array_spec.BoundedArraySpec(
        shape=(), dtype=np.int32, minimum=0, maximum=1, name='action')
    self._observation_spec = array_spec.BoundedArraySpec(
        shape=(1,), dtype=np.int32, minimum=0, name='observation')
    self._gameplay = Gameplay()
    self._state = self._gameplay._board
    self._episode_ended = False

  def action_spec(self):
    return self._action_spec

  def observation_spec(self):
    return self._observation_spec

  def _reset(self):
    self._state = 0
    self._episode_ended = False
    return ts.restart(np.array([self._state], dtype=np.int32))

  def _step(self, action, piece): # obtaining the reward from the environment at any given timestep

    # first, we need to specify a piece with its (x,y) coordinates

    if action == "front left":
      # move the piece to the left
      pass
    elif action == "front right":
      # move the piece to the right
      pass
    elif action == "back left":
      # move the piece to the left
      pass
    elif action == "back right":
      # move the piece to the right
      pass
    else:
      raise ValueError('action should be front left, front right, back left, or back right.')

    if self._gameplay.check_win() is not None: # if someone won

      count_white = 0
      count_black = 0

      for piece in self._gameplay._pieces:
        if piece._color == Color.WHITE:
          count_white += 1
        elif piece._color == Color.BLACK:
          count_black += 1
        else:
          print("N/A")

      # let's say that white is the AI, and black is the player

      reward = count_white - count_black # if the AI captures opponent pieces, then higher reward

      return ts.termination(np.array([self._state], dtype=np.int32), reward)

    else:
      return ts.transition(
          np.array([self._state], dtype=np.int32), reward=0.0, discount=1.0)