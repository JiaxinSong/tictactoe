import numpy as np
import torch as tr
from torch.nn import Sequential, Linear, Flatten, Sigmoid, ReLU, Tanh

#1 hidden layer, 20 units, activation funciton == sigmoid
def NN(board_size):
    modules = Sequential(Flatten(),
                         Linear(3*board_size*board_size, 40),
                         Linear(40, 20),
                         Sigmoid(),
                         Linear(20, 1))
    return modules

def calculate_loss(net, x, y_targ):
    y = net(x)
    e = tr.sum((y - y_targ)**2)
    return (y, e)

def optimization_step(optimizer, net, x, y_targ):
    optimizer.zero_grad()
    y, e = calculate_loss(net, x, y_targ)
    e.backward()
    optimizer.step()
    return (y, e)

def train(board_size):

    net = NN(board_size)
    import pickle as pk
    with open("data%d.pkl" % board_size, "rb") as fin:
        (x, y_targ) = pk.load(fin)

    optimizer = tr.optim.Adam(net.parameters(), lr = 0.01)
    train_loss, test_loss = [], []
    shuffle = np.random.permutation(range(len(x)))
    rd =int( 0.1 * len(shuffle))
    train, test = shuffle[:-rd], shuffle[-rd:]
    for epoch in range(500):
        y_train, e_train = optimization_step(optimizer, net, x[train], y_targ[train])
        y_test, e_test = calculate_loss(net, x[test], y_targ[test])
        print("%d: %f (%f)" % (epoch, e_train.item(), e_test.item()))
        train_loss.append(e_train.item() / (len(shuffle) - rd))
        test_loss.append(e_test.item() / rd)

    tr.save(net.state_dict(), "model%d.pth" % board_size)

    import matplotlib.pyplot as pt
    pt.plot(train_loss, 'b-')
    pt.plot(test_loss, 'r-')
    pt.legend(["Train", "Test"])
    pt.xlabel("Iteration")
    pt.ylabel("Average Loss")
    pt.show()

    pt.plot(y_train.detach().numpy(), y_targ[train].detach().numpy(), 'bo')
    pt.plot(y_test.detach().numpy(), y_targ[test].detach().numpy(), 'ro')
    pt.legend(["Train", "Test"])
    pt.xlabel("Actual output")
    pt.ylabel("Target output")
    pt.show()

if __name__ == "__main__":
    board_size = 3
    train(board_size)
