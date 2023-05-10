import random

def check(x):
    return 1 if x >= 0 else 0


def algo(inputs, targets):
    
    weights = [random.uniform(1, 10), random.uniform(1, 10)]
    bias = random.uniform(1, 10)
    learning_rate = 0.1
    iterations = 0
    error = True

    while error:
        error = False
        for i in range(len(inputs)):
            
            dot_product = sum(x * w for x, w in zip(inputs[i], weights)) + bias

            
            predicted_output = check(dot_product)

            delta = targets[i] - predicted_output

           
            if delta != 0:
                error = True
                weights = [w + learning_rate * delta * x for x, w in zip(inputs[i], weights)]
                bias += learning_rate * delta
        iterations += 1

    return iterations


a_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
and_targets = [0, 0, 0, 1]

a_iterations = algo(a_inputs, and_targets)

or_inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
or_targets = [0, 1, 1, 1]


or_iterations = algo(or_inputs, or_targets)

print("AND gate iterations:", a_iterations)
print("OR gate iterations:", or_iterations)

# method 2

# import numpy as np

# def perceptron_learning_algorithm(gate_name, data):
#   X  =  data[ : ,  : 2]
#   y = data[:, 2]

#   np.random.seed(0)
#   w = np.random.rand(2) * 9 + 1 
#   b = np.random.rand() * 9 + 1

#   lr = 1.5
#   epochs = 100
#   iteration = 0

#   for epoch in range(epochs): 
#     total_error = 0

#     for i in range(len(X)): 
#       x = X[i]
#       desired_output = y[i]
#       actual_output = 1 if np.dot(w, x) + b > 0 else 0

#       error = desired_output - actual_output 
#       total_error += abs(error)

#       w += lr * error * x 
#       b += lr * error

#     iteration += 1

#     if total_error == 0:
#       break

#   return gate_name, X, y, iteration

# if __name__  ==  "__main__" :
#   gate = {
#     "AND" : np.array([[0,0,0], [0,1,0], [1,0,0], [1,1,1]]),
#     "OR" : np.array([[0,0,0], [0,1,1], [1,0,1], [1,1,1]]),
#     "NAND" : np.array([[0,0,0], [0,1,1], [1,0,1], [1,1,1]]),
#     "NOR" : np.array([[0,0,0], [0,1,1], [1,0,1], [1,1,1]])
#   }

#   gate_name, inputs, outputs, iterations = perceptron_learning_algorithm("OR", gate["OR"]) 
#   print(f"{gate_name} gate: ")
#   for input_, output in zip(inputs, outputs): print(f"{input_}={output} It: {iterations}")
#   print()

#   gate_name, inputs, outputs, iterations = perceptron_learning_algorithm("AND", gate["AND"]) 
#   print(f"{gate_name} gate: ")
#   for input_, output in zip(inputs, outputs): print(f"{input_}={output} It: {iterations}")
#   print()

#   gate_name, inputs, outputs, iterations = perceptron_learning_algorithm("NAND", gate["NAND"]) 
#   print(f"{gate_name} gate: ")
#   for input_, output in zip(inputs, outputs): print(f"{input_}={output} It: {iterations}")
#   print()
