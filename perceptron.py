import numpy as np
epoch = 3
teta = 0

class Perceptron:
    def __init__(self,input_size,learning_rate=1):
        self.weights = np.zeros(input_size+1)
        self.learning_rate = learning_rate
        
    def calculate(self,x):
        return self.weights[0] +  np.dot(x,self.weights[1:])
    
    def train(self,x,y,weights):
        for inputs,target in zip(x,y):
            y_net = self.calculate(inputs)
            if y_net > teta:
                y_out = 1
            elif y_net < -teta:
                y_out = -1
            else:
                y_out = 0
                
            if y_out != target:
                
                self.weights[0] += self.learning_rate * target
                self.weights[1:] += self.learning_rate * target * inputs
            print("Yin-{} Yout={} target={} weights={}".format(y_net,y_out,target,self.weights))
    
    
x = []
x.append(np.array([1,1]))
x.append(np.array([-1,1]))
x.append(np.array([1,-1]))
x.append(np.array([-1,-1]))

y = np.array([1,-1,-1,-1])

perceptron = Perceptron(2)

for i in range(epoch):
    print("EPOCH {}".format(i))
    weights = perceptron.weights
    print("Initial weights are {}".format(weights))
    perceptron.train(x,y,weights)