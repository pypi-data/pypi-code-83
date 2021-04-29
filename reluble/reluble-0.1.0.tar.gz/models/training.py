import torch
import torch.nn.functional as F
from reluble.utils.stats import inspect_gradients, ttest
import matplotlib.pyplot as plt
import numpy as np

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')


def train(network, train_loader, optimizer, epoch, log_interval=10, check_interval=10, stats=None):
    network.train()
    network = network.to(device)
    stats = dict(clean=[], noise=[], p=[], pflug=[]) if stats is None else stats
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad()
        output = network(data.to(device))
        loss = F.cross_entropy(output, target.to(device))
        loss.backward()
        optimizer.step()

        if batch_idx % check_interval == 0:
            avg_grads1, std_grads1, raw1 = inspect_gradients(network.named_parameters())
            stats['clean'].append(avg_grads1)
            # if len(stats['pflug']) > 0:
            #     stats['pflug'].append(stats['pflug'][-1] * avg_grads1)
            # else:
            #     stats['pflug'].append(torch.ones_like(avg_grads1))
            optimizer.zero_grad()
            idx = torch.randperm(len(target))
            output = network(data.to(device))
            loss = F.cross_entropy(output, target[idx].to(device))
            loss.backward()
            avg_grads2, std_grads2, raw2 = inspect_gradients(network.named_parameters())
            stats['noise'].append(avg_grads2)

            t_stat, df, cv, p = ttest(avg_grads1, avg_grads2, std_grads1, std_grads2, data.shape[0])
            stats['p'].append(p)

        if batch_idx % log_interval == 0:
            print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                epoch, batch_idx * len(data), len(train_loader.dataset),
                       100. * batch_idx / len(train_loader), loss.item()))
    return stats


def test(network, test_loader):
    network.eval()
    network = network.to(device)
    test_loss = 0
    correct = 0
    with torch.no_grad():
        for data, target in test_loader:
            output = network(data.to(device))
            test_loss += F.cross_entropy(output, target.to(device), size_average=False).item()
            pred = output.cpu().data.max(1, keepdim=True)[1]
            correct += pred.eq(target.data.view_as(pred)).sum()
    test_loss /= len(test_loader.dataset)
    print('\nTest set: Avg. loss: {:.4f}, Accuracy: {}/{} ({:.0f}%)\n'.format(
        test_loss, correct, len(test_loader.dataset),
        100. * correct / len(test_loader.dataset)))
    return 100. * correct / len(test_loader.dataset)

