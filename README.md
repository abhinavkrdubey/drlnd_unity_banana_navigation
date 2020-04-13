# Reinforcement Learning Project 1: Navigation

## Introduction
![banana](images/banana-intro.gif)

In this project, the goal is to teach a reinforcement learning AI agent to navigate a Unity environment and play a simple game - collecting yellow bananas (with a reward of +1) and avoiding blue ones (with a reward of (-1). 

![trained](images/trained.gif)

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around agent's forward direction.  Given this information, the agent has to learn how to best select actions.  Four discrete actions are available, corresponding to:

- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes. However, to present more of a challenge and get a better sense of the agent's abilities, I've increased the average score threshold to +15 in my own implementation.

## Methods

There are four types of reinforcement learning algorithms used in this project:

- A **deep Q-network**, which is a neural network that approximates Q-values (measures of the 'quality' of a possible action) for each action that can be taken in a particular state.
- A **double deep Q-network**, which is meant to improve on a deep Q-network's tendency to overestimate action-value functions by using two separate sets of value functions: one to select an action, and another to estimate the action's effectiveness.
- A **dueling deep Q-network**, which is a network architecture that separates the estimation of a state value from the effectiveness of each action in that state, and then combines them in an aggregation layer. This allows the Q-network to learn which states are and aren't valuable, without needing to know the effect of each action in each state.
- **Prioritized experience replay**. This is an experience replay buffer that puts a priority on state-action experiences that have large differences between the prediction and the intended target, so the agent is more likely to replay those experiences and learn from its mistakes.

These algorithms are first used separately and then combined, to see how they affect the agent's performance both on their own and together.

## Project details

Project created as 1st project on Udacity Deep Reinforcement Learning nanodegree. The goal of the agent is to gather `yellow` bananas while avoiding the `blue` ones. Here are Unity details of the environment:

```
Unity brain name: BananaBrain
        Number of Visual Observations (per agent): 0
        Vector Observation space type: continuous
        Vector Observation space size (per agent): 37
        Number of stacked Vector Observation: 1
        Vector Action space type: discrete
        Vector Action space size (per agent): 4
        Vector Action descriptions: , , , 
```

That means we work with state vector containing 37 continous values and 4 discrete actions representing moves (forward, backward, turn left, turn right). The environment is considered solved when agents reaches average score of 13.0 on 100 consecutive episodes.

## Getting started

Make sure you have `python 3.6` installed and virtual environment of your choosing activated. Unity has to be installed on your system. Run:

pip install -r requirements.txt

to install python dependencies. Then you should be able to run `jupyter notebook` and view `Banana.ipynb`. File `model.py` contains neural network class used as a Q function and file `dqn.py` contains agent code.

## Instructions

Run `Banana.ipynb` for further details.
