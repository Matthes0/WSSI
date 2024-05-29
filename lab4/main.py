import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch


class Neuron:
    def __init__(self, n_inputs, bias=0., weights=None):
        self.b = bias
        if weights:
            self.ws = np.array(weights)
        else:
            self.ws = np.random.rand(n_inputs)

    def _f(self, x):  # activation function (here: leaky_relu)
        return max(x * .1, x)

    def __call__(self,
                 xs):  # calculate the neuron's output: multiply the inputs with the weights and sum the values together, add the bias value,
        # then transform the value via an activation function
        return self._f(xs @ self.ws + self.b)


class Layer:
    def __init__(self, n_neurons, n_inputs):
        self.neurons = [Neuron(n_inputs) for _ in range(n_neurons)]

    def __call__(self, xs):
        return np.array([neuron(xs) for neuron in self.neurons])


class NeuralNetwork:
    def __init__(self, input_size, hidden_sizes, output_size):
        self.layers = []
        self.layers.append(Layer(input_size, input_size))
        for i in range(len(hidden_sizes)):
            self.layers.append(Layer(hidden_sizes[i], len(self.layers[len(self.layers) - 1].neurons)))
        self.layers.append(Layer(output_size, len(self.layers[len(self.layers) - 1].neurons)))

def visualize_nn(nn):
    input_size = len(nn.layers[0].neurons)
    hidden_sizes = []
    if len(nn.layers) > 2:
        tmp = nn.layers[1:-1]
        for value in tmp:
            hidden_sizes.append(len(value.neurons))
    output_size = len(nn.layers[-1].neurons)

    fig, ax = plt.subplots(figsize=(15, 10))
    h_spacing = 2
    v_spacing = 1

    def get_layer_positions(n, layer_index):
        return [(layer_index * h_spacing, v_spacing * (i - (n - 1) / 2)) for i in range(n)]

    input_positions = get_layer_positions(input_size, 0)
    input_x, input_y = zip(*input_positions)
    input_rect = plt.Rectangle((min(input_x) - 0.3, min(input_y) - 0.5), 0.6, input_size, linewidth=1.5,
                               facecolor='red', alpha=0.2)
    ax.add_artist(input_rect)
    text = plt.Text(min(input_x) - 0.5, min(input_y) - 0.7, "input layer", color='red')
    ax.add_artist(text)
    for x, y in input_positions:
        circle = plt.Circle((x, y), radius=0.2, fill=True, facecolor='white', edgecolor='black')
        ax.add_artist(circle)
    hidden_positions = []
    if len(hidden_sizes):
        for l, layer_size in enumerate(hidden_sizes):
            positions = get_layer_positions(layer_size, l + 1)
            hidden_x, hidden_y = zip(*positions)
            hidden_rect = plt.Rectangle((min(hidden_x) - 0.3, min(hidden_y) - 0.5), 0.6, layer_size, linewidth=1.5,
                                        facecolor='blue', alpha=0.2)
            ax.add_artist(hidden_rect)
            hidden_positions.append(positions)
            text = plt.Text(min(hidden_x) - 0.5, min(hidden_y) - 0.7, f"hidden layer {l + 1}", color='blue')
            ax.add_artist(text)
            for x, y in positions:
                circle = plt.Circle((x, y), radius=0.2, linewidth=1.5, fill=True, facecolor='white', edgecolor='black')
                ax.add_artist(circle)
    output_positions = get_layer_positions(output_size, len(hidden_sizes) + 1)
    output_x, output_y = zip(*output_positions)
    output_rect = plt.Rectangle((min(output_x) - 0.3, min(output_y) - 0.5), 0.6, output_size, linewidth=1.5,
                                facecolor='green', alpha=0.2)
    ax.add_artist(output_rect)
    text = plt.Text(min(output_x) - 0.5, min(output_y) - 0.7, "output layer", color='green')
    ax.add_artist(text)
    for x, y in output_positions:
        circle = plt.Circle((x, y), radius=0.2, fill=True, facecolor='white', edgecolor='black')
        ax.add_artist(circle)
    if len(hidden_sizes):
        for (x0, y0) in input_positions:
            for (x1, y1) in hidden_positions[0]:
                arrow = FancyArrowPatch((x0 + 0.15, y0), (x1 - 0.15, y1), arrowstyle='-|>', mutation_scale=10,
                                        color='dimgray')
                ax.add_artist(arrow)
        for l in range(len(hidden_positions) - 1):
            for (x0, y0) in hidden_positions[l]:
                for (x1, y1) in hidden_positions[l + 1]:
                    arrow = FancyArrowPatch((x0 + 0.15, y0), (x1 - 0.15, y1), arrowstyle='-|>', mutation_scale=10,
                                            color='dimgray')
                    ax.add_artist(arrow)

        for (x0, y0) in hidden_positions[-1]:
            for (x1, y1) in output_positions:
                arrow = FancyArrowPatch((x0 + 0.15, y0), (x1 - 0.15, y1), arrowstyle='-|>', mutation_scale=10,
                                        color='dimgray')
                ax.add_artist(arrow)
    else:
        for (x0, y0) in input_positions:
            for (x1, y1) in output_positions:
                arrow = FancyArrowPatch((x0 + 0.15, y0), (x1 - 0.15, y1), arrowstyle='-|>', mutation_scale=10,
                                        color='dimgray')
                ax.add_artist(arrow)

    ax.set_aspect('equal')
    plt.xlim([-1, 10])
    plt.ylim([-5, 5])
    ax.axis('off')
    plt.show()


if __name__ == '__main__':

    nn = NeuralNetwork(3, [4,4], 1)
    visualize_nn(nn)  # graph of layers
