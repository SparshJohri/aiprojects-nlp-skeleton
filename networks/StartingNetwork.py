import torch
import torch.nn as nn


class StartingNetwork(torch.nn.Module):
    """
    Basic logistic regression example. You may need to double check the dimensions :)
    """

    def __init__(self, modelSize):
        super().__init__()
        self.fc1 = nn.Linear(modelSize, 50) # What could that number mean!?!?!? Ask an officer to find out :)
        self.fc2 = nn.Linear(50, 10)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        mystr = "This is a random string that Sparsh put inside the forward function to test if he can push."
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x