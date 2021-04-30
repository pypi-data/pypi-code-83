import numpy as np
from matplotlib import pyplot as plt, cm

# TODO: on both of these functions, each vertical section doesn't need to
#  be its own subplot.
# Big picture, these functions gets a little cleaner if I don't use subplots
# but rather handle scaling myself and plot everything onto one axis.
# It took building out this approach to realize that, so in case of using
# this function in production, make the switch.  Else, here we are.
from scipy import stats


def plot_custom_violin(x, ys, x_lables):
    """
    Custom violin plot - sns and plt give interfaces to to feed in raw data to
    which it aggregates


    :param x:
    :param ys:
    :return:
    """
    params = {
        'color': 'b',
        'alpha': 0.3
    }
    n_levers = len(ys)
    fig, axs = plt.subplots(1, n_levers, sharex=True,
                            figsize=(10, 6))  # sharey=True
    fig.suptitle('Aggregate Treatment Performance')

    for i, y in enumerate(ys):
        axs[i].plot(y, x, **params)
        axs[i].plot(-y, x, **params)
        axs[i].fill_betweenx(x, y, -y, **params)
        axs[i].set_xlabel(x_lables[i])
        axs[i].set_facecolor((0., 0., 0., 0.))  # background of subplot

        # axs[i].axis('off')
        axs[i].tick_params(
            axis='x',  # changes apply to the x-axis
            which='both',  # both major and minor ticks are affected
            bottom=False,  # ticks along the bottom edge are off
            top=False,  # ticks along the top edge are off
            labelbottom=False)  # labels along the bottom edge are off
        if i > 0:  # for all plots except the far left, disable additional bits
            axs[i].tick_params(
                axis='y',  # changes apply to the x-axis
                which='both',  # both major and minor ticks are affected
                left=False,
                right=False,
                labelleft=False,
            )

    axs[0].set_ylabel("Estimated Response Rates")
    return fig


def plot_per_batch_performance(batches, treatment_names):
    params = {
        'alpha': 0.3
    }
    n_batches = len(batches)

    # TODO: assign color to each email.
    cmap = cm.get_cmap('Set1')  # Dark2, Pastel1
    assert cmap.N >= n_batches, \
        f"Or let the cmap repeat?? n_colors={cmap.N}, n_batches={n_batches}"

    fig, axs = plt.subplots(1, n_batches, sharex=True, figsize=(10, 6))
    fig.suptitle('Batch and Treatment Performances')

    # plt.figure(4, (10, 8))

    perf_x = np.linspace(0., 1., 1000)

    batch_agg_rates = []
    for i, batch in enumerate(batches):
        visual_offset = i   # In case of single axis.  Harmless with subplots.
        batch_n_pos = 0
        batch_n_neg = 0
        for j, [n_pos, n_neg] in enumerate(batch):
            this_ax = axs[i]

            batch_n_pos += n_pos
            batch_n_neg += n_neg
            n = n_pos + n_neg
            # Generate this pdf:
            # perf = [stats.beta.pdf(x, a, b) for a, b in simulated_responses]
            y = stats.beta.pdf(perf_x, n_pos, n_neg) * n
            # TODO: flip beta out for gaussian? this stage is more about visual
            # inuition for what each part of the batch contributes

            this_params = params
            this_params['color'] = cmap.colors[j]

            this_ax.plot(y+visual_offset, perf_x, **params)
            this_ax.plot(-y+visual_offset, perf_x, **params)
            this_ax.fill_betweenx(perf_x, y+visual_offset, -y+visual_offset,
                                 label=treatment_names[j],
                                 **params)
            this_ax.plot([1]*len(y), perf_x, color=(.2, .2, .2, .8), lw=0.7)

            this_ax.axis('off')

        batch_agg_rates.append((batch_n_pos, batch_n_neg))

    # zoom vertical dimension into proper scale
    vlim = 0.6
    for this_ax in axs:
        this_ax.set_ylim((0, vlim))

    plt.legend(loc='upper right')

    ax_overlay = fig.add_subplot()
    ax_overlay.set_facecolor((0., 0., 0., 0.))

    batch_x = [x*2 + 1 for x in range(n_batches)]
    batch_y = [p/(p+n) for p, n in batch_agg_rates]
    ax_overlay.plot(batch_x, batch_y, color='k', marker='*', lw=0.4,
                    markersize=8)
    for x, y in zip(batch_x, batch_y):
        ax_overlay.text(x, y, f"{y:0.3f}",
                        horizontalalignment='right',
                        verticalalignment='bottom')

    ax_overlay.set_ylim((0, vlim))
    ax_overlay.set_xlim((.165, n_batches*2-0.16))
    # ax_over
    ax_overlay.set_xticks(batch_x)  # [1, 3, 5,...]
    ax_overlay.set_xticklabels([f"Batch {x+1}" for x in range(n_batches)])

    plt.ylabel("Treatment Success Rate")
    # axs[0].set_ylabel("Estimated Response Rates")

    return fig
