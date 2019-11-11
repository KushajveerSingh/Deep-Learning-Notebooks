import torch
import torch.nn as nn
import torch.nn.functional as F

__all__ = ['Mish']

class Mish(nn.Module):
    r"""
    Mish activation function is proposed in "Mish: A Self 
    Regularized Non-Monotonic Neural Activation Function" 
    paper, https://arxiv.org/abs/1908.08681.
    """

    def __init__(self):
        super().__init__()

    def forward(self, x):
        return x * torch.tanh(F.softplus(x))