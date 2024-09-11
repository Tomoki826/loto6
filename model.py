import torch
import random
import torch.nn as nn
import torch.nn.functional as F
from torch import Tensor

class Model(nn.Module):
    
    def __init__(self, orders=10):
        super(Model, self).__init__()
        
        self.linear_ii = nn.Linear(43, 43)
        self.linear_hi = nn.Linear(43, 43)
        self.linear_if = nn.Linear(43, 43)
        self.linear_hf = nn.Linear(43, 43)
        self.linear_ig = nn.Linear(43, 43)
        self.linear_hg = nn.Linear(43, 43)
        self.linear_io = nn.Linear(43, 43)
        self.linear_ho = nn.Linear(43, 43)
        
        self.orders = orders
        self.reset_state()
    
    def reset_state(self):
        self.c = torch.rand(self.orders, 43)
        self.h = torch.rand(self.orders, 43)
    
    def forward(self, x: Tensor):
        i = F.sigmoid(self.linear_ii(x) + self.linear_hi(self.h))
        f = F.sigmoid(self.linear_if(x) + self.linear_hf(self.h))
        g = F.tanh(self.linear_ig(x) + self.linear_hg(self.h))
        o = F.sigmoid(self.linear_io(x) + self.linear_ho(self.h))
        self.c = torch.mul(f, self.c) + torch.mul(i, g)
        self.h = torch.mul(o, F.tanh(self.c))
        return self.h