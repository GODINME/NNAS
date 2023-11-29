# Refactoring Example2 in "ex2.py"

inputs = [1, 2, 3, 2.5]
weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

# Output of current layer
layer_outputs = []

# For every neuron
for neuron_weights, neuron_bias in zip(weights, biases):
    # Initializing each neuron output from forward pass
    neuron_output = 0
    
    # For each input and associated weight of each neuron
    for n_input, weight in zip(inputs, neuron_weights):
        # Multiply input with associated weight and add to the neuron output
        neuron_output += n_input * weight 
    # Add bias
    neuron_output += neuron_bias 
    # Append the neuron output to the layer neuron output 
    layer_outputs.append(neuron_output)


print(layer_outputs)
