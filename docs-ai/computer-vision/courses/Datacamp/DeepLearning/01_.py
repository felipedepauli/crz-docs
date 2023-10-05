import numpy as np

def relu(result):
    return max(result, 0)

def predict_using_network(input, weights):
    
    node_0 = (input * weights['node_0']).sum()
    node_0 = relu(node_0)
    
    node_1 = (input * weights['node_1']).sum()
    node_1 = relu(node_1)
    
    hidden = np.array([node_0, node_1])
    class_0 = (hidden * weights['class_0']).sum()
    class_0 = relu(class_0)
    
    class_1 = (hidden * weights['class_1']).sum()
    class_1 = relu(class_1)
    
    return [class_0, class_1]

input = np.array([2, 3])
weights = {
    'node_0': [-1, 1],
    'node_1': [-1, 2],
    'class_0': [2, 1],
    'class_1': [1, 1]
}

print(predict_using_network(input, weights))



