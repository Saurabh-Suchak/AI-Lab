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
