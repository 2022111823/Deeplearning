import numpy as np

inputs = [[3.0, 1.0, 2.1, 2.5],
             [2.6, 5.0, -1.0, 2.1],
             [-1.5,2.7,3.3,-0.8],
          [2.8, 2.0, -1.0, 2.1],
          [-1.1, 1.7, 2.3, -1.8]]

weights = [[0.2,0.3,-0.5,1.7],
           [0.5,-0.8,0.76,-0.6],
           [-0.36,-0.27,0.17,0.66],]



biases = [2.0,3.0,0.5,]


layers_outputs = np.dot(inputs, np.array(weights).T)+biases
print(layers_outputs)

weights_2 = [[0.1,0.2,-0.3],
           [0.5,-0.4,0.32],
           [-0.54,-0.32,0.11],]

biases_2 = [1.0,2.1,2.3]

layers_outputs2 = np.dot(layers_outputs, np.array(weights_2).T) + biases
print(layers_outputs2)

