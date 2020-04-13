import torch
import torch.nn as nn
import torch.nn.functional as F

class QNetwork(nn.Module):
	"""Class for neural network
		Attributes:
			state_size(int): Dimension of each state
			action_size(int): Dimension of each action
			seed(int): Random seed
	"""

	def __init__(self, state_size, action_size, seed):
		"""Initialize parameters and model architecture"""
		super(QNetwork, self).__init__()
		self.seed = torch.manual_seed(seed)
		self.fc1 = nn.Linear(state_size, 128)
		self.fc2 = nn.Linear(128, 64)
		self.fc3 = nn.Linear(64, action_size)

	def forward(self, state):
		"""Forward propogation of Neural Netwok
			Arguments:
				state(vector): sized(self.state_size x batch_size) with environment state data

			Returns:
				Vector sized (self.action_size x batch_size) with return of a Neural Network
		"""
		x = F.relu(self.fc1(state))
		x = F.relu(self.fc2(x))
		x = self.fc3(x)
		return x