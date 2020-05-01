from dec_opt.utils import unpickle_dir
import numpy as np
import matplotlib.pyplot as plt


def plot_results(repeats, label, plot='train'):
    scores = []
    for result in repeats:
        loss_val = result[0] if plot == 'train' else result[1]
        scores += [np.log(loss_val)]
    mean = np.mean(scores, axis=0)
    UB = mean + np.std(scores, axis=0)
    LB = mean - np.std(scores, axis=0)
    x = np.arange(mean.shape[0])
    plt.plot(x, mean, label=label)
    plt.fill_between(x, LB, UB, alpha=0.2)


if __name__ == '__main__':
    # Example plot generation :
    # Follow this template to generate your own combination of plots
    # remember the naming convention of the results
    # Load all results of a particular data-set
    data = unpickle_dir(d='./results/breast_cancer')
    print('Loaded Data')

    # Now Lets
    plt.figure()
    fig = plt.gcf()

    # Specify what result runs you want to plot together
    plot_results(repeats=data['ours.16.ring.0.top'], label='Boyd')
    # plot_results(repeats=data['ours.16.ring.0.top'], label='Q=0')
    plot_results(repeats=data['ours.16.ring.1.top'], label='Q=1')
    plot_results(repeats=data['ours.16.ring.2.top'], label='Q=2')
    plot_results(repeats=data['ours.16.ring.3.top'], label='Q=3')
    plot_results(repeats=data['ours.16.ring.4.top'], label='Q=4')
    plot_results(repeats=data['ours.16.ring.5.top'], label='Q=5')
    plot_results(repeats=data['ours.16.ring.10.top'], label='Q=10')
    plot_results(repeats=data['ours.16.ring.15.top'], label='Q=15')
    # plot_results(repeats=data['ours.9.torus.2.full'], label='torus')
    # plot_results(repeats=data['ours.9.ring.2.full'], label='ring')
    # plot_results(repeats=data['ours.9.disconnected.2.full'], label='disconnected')

    plt.legend()
    plt.show()
