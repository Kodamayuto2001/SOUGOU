import torch
import torch.nn.functional as F 

class Net_log_softmax(torch.nn.Module):
    def __init__(self,num,inputSize,Neuron):
        super(Net_log_softmax, self).__init__()
        self.iSize = inputSize
        self.fc1 = torch.nn.Linear(self.iSize*self.iSize, Neuron)
        self.fc2 = torch.nn.Linear(Neuron, num)
 
    def forward(self, x):
        x = x.view(-1,self.iSize*self.iSize)
        x = self.fc1(x)
        x = torch.relu(x)
        x = self.fc2(x)
        return F.log_softmax(x, dim=1)


class Net_return_x(torch.nn.Module):
    def __init__(self,num,inputSize,Neuron):
        super(Net_return_x, self).__init__()
        self.iSize = inputSize
        self.fc1 = torch.nn.Linear(self.iSize*self.iSize, Neuron)
        self.fc2 = torch.nn.Linear(Neuron, num)

    def forward(self,x):
        x = x.view(-1,self.iSize*self.iSize)
        x = self.fc1(x)
        x = torch.relu(x)
        x = self.fc2(x)
        return x 

# class CNN(torch.nn.Module):
#     def