from torchvision import transforms
import functools
import numpy as np
import random
import torch


def apply_by_channel(transform):
    """
    Takes a transform function and turns it into another transform, that will be applied independently to each channel.
    This is useful when using torchvision transforms, which interpret channels as RGB, and do PIL weirdness with them.
    Additionally, ToPILImage will automatically be applied to the image.
    This has been checked with uint8 and float32 inputs and preserves these types and their ranges.
    This function can be used as a decorator for your function.

    :param transform: A transformation function.
    :return: The same transformation function, modified as described.
    """
    to_pil_image = transforms.ToPILImage()

    def channel_transform(image):
        new_image = []
        # record the random number generator state
        seed = np.random.randint(2147483647)
        for i, channel in enumerate(image):
            random.seed(seed)
            torch.manual_seed(seed)

            channel = to_pil_image(channel)
            channel = transform(channel)
            new_image.append(np.asarray(channel))
        return np.asarray(new_image)

    @functools.wraps(transform)
    def wrapper(image):
        if image.ndim == 3:
            return channel_transform(image)

        elif image.ndim == 4:
            shape = image.shape
            new_image = channel_transform(image.reshape((-1, *shape[-2:])))
            return new_image.reshape((*shape[:2], *new_image.shape[-2:]))

        else:
            raise ValueError("Input must be a 3d image (channels, x, y) or a 4d video (time, channels, x, y)")

    return wrapper


def _display_frame(frame, label=None, ax=None):
    import matplotlib.pyplot as plt
    assert frame.ndim == 3, f"Image must have 3 dimensions, found {frame.ndim}"
    assert len(frame) == 2, f"Image must have 2 channels, found {len(frame)}"

    if ax is None:
        ax = plt.gca()
    if label is not None:
        ax.set_title("Label: " + str(label))

    diff = frame[0] - frame[1]
    maxdiff = diff.abs().max()
    ax.imshow(diff, cmap=plt.cm.coolwarm, vmin=-maxdiff, vmax=maxdiff)
    ax.set_axis_off()


def display_frames(frames, labels=None, ncols=4):
    import matplotlib.pyplot as plt

    if frames.ndim == 3:
        return _display_frame(frames, label=labels)

    assert frames.ndim == 4, "Expected array of 3d images"
    nframes = len(frames)
    nrows = int(np.ceil(nframes / ncols))

    for i in range(nframes):
        label = labels[i] if labels is not None else None
        plt.subplot(nrows, ncols, i + 1)
        _display_frame(frames[i], label)

    plt.show()

def events_animation(xytp: np.ndarray, timescale, framerate = 24, repeat = False, show = False):
    """
    :param xytp:  events np arrary, with strict ["x"], ["y"], ["t"], ["p"] to call correspond event information
                  p should be either 1/0 or True/False to represent ON/OF polarity
    :param timescale: the timescale of recording events (ms)
    :param framerate: framerate of animation
    :param repeat(boolean):  if repeat
    :param show(boolean):  if show the animation

    :return: animation object
    """

    import matplotlib.pyplot as plt
    from matplotlib import animation

    fig = plt.figure()

    xdim, ydim = xytp["x"].max() + 1, xytp["y"].max() +1
    interval = 1e3/framerate

    minFrame = int(np.floor(xytp["t"].min())/timescale/interval)
    maxFrame = int(np.ceil(xytp["t"].max())/timescale/interval)
    Image    = plt.imshow(np.zeros((ydim, xdim, 3)))
    frames   = np.zeros((maxFrame - minFrame, ydim, xdim, 3))

    for i in range(len(frames)):
        tStart   = (i + minFrame) * interval
        tEnd     = (i + minFrame +1) * interval
        timeMask = (xytp["t"]/timescale >= tStart) & (xytp["t"]/timescale < tEnd)
        rInd     = timeMask & (xytp["p"].astype("uint8") == 1)
        gInd     = timeMask & (xytp["p"].astype("uint8") == 0)

        frames[i, xytp["y"][rInd], xytp["x"][rInd], 0] = 1
        frames[i, xytp["y"][gInd], xytp["x"][gInd], 1] = 1

    def animate(inputFrame):
        Image.set_data(inputFrame)
        return Image

    anim = animation.FuncAnimation(fig, animate, frames = frames, interval = interval, repeat = repeat)
    if show:
        plt.show()
    return anim


