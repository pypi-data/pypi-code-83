import matplotlib
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d.art3d import Path3DCollection
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from wizzi_utils.misc import misc_tools as mt


def get_RGB_color(color_str: str) -> tuple:
    """
    :param color_str: e.g. "red", "blue" ...
    :return: RGB color
    see get_colors_formats_test()
    """
    rgb_normed = matplotlib.colors.to_rgb(color_str)
    rgb = tuple([int(round(255 * x)) for x in rgb_normed])
    return rgb


def get_RGBA_color(color_str: str, opacity: float = 1.0, float_pre: int = 3) -> tuple:
    """
    :param color_str: e.g. "red", "blue" ...
    :param opacity: value from 0 to 1
    :param float_pre: round to x digits - 0 no rounding
    :return: rgba color
    see get_colors_formats_test()
    """
    rgba = matplotlib.colors.to_rgba(color_str, alpha=opacity)
    if float_pre > 0:
        rgba = list(rgba)
        for i in range(len(rgba)):
            rgba[i] = round(rgba[i], float_pre)
        rgba = tuple(rgba)
    return rgba


def get_BGR_color(color_str: str) -> tuple:
    """
    :param color_str: e.g. "red", "blue" ...
    :return: bgr color
    see get_colors_formats_test()
    """
    rgb = get_RGB_color(color_str)
    bgr = RGB_to_BGR(rgb)
    return bgr


def RGBA_to_RGB(rgba: tuple) -> tuple:
    """
    :param rgba: RGBA format - tuple 1,4
    :return: rgb color format
    see RGBA_to_RGB_and_BGR_test()
    """
    rgb_normed = matplotlib.colors.to_rgb(rgba)
    rgb = tuple([int(round(255 * x)) for x in rgb_normed])
    return rgb


def RGBA_to_BGR(rgba: tuple) -> tuple:
    """
    :param rgba: RGBA format - tuple 1,4
    :return: bgr color format
    see RGBA_to_RGB_and_BGR_test()
    """
    rgb = RGBA_to_RGB(rgba)
    bgr = RGB_to_BGR(rgb)
    return bgr


def BGR_to_RGB(bgr: tuple) -> tuple:
    """
    :param bgr:
    :return: rgb
    see BGR_to_RGB_and_RGBA_test()
    """
    rgb = mt.reverse_tuple_or_list(bgr)  # reverse the tuple order
    return rgb


def BGR_to_RGBA(bgr: tuple, opacity: float = 1.0) -> tuple:
    """
    :param bgr:
    :param opacity:
    :return: rgba
    see BGR_to_RGB_and_RGBA_test()
    """
    rgb = BGR_to_RGB(bgr)
    rgba = RGB_to_RGBA(rgb, opacity)
    return rgba


def RGB_to_BGR(rgb: tuple) -> tuple:
    """
    :param rgb:
    :return: bgr
    see RGB_to_RGBA_and_BGR_test()
    """
    bgr = mt.reverse_tuple_or_list(rgb)  # reverse the tuple order
    return bgr


def RGB_to_RGBA(rgb: tuple, opacity: float = 1.0, float_pre: int = 3) -> tuple:
    """
    :param rgb:
    :param opacity:
    :param float_pre:
    :return: rgba
    see RGB_to_RGBA_and_BGR_test()
    """
    rgba = tuple([round(x / 255, float_pre) for x in rgb])
    rgba += (opacity,)
    return rgba


def get_ticks_list(x_low: [float, int], x_high: [float, int], p: int = 10) -> list:
    """
    :param x_low:
    :param x_high:
    :param p:
    :return:
    calculates a list that starts from x_low to x_high each p%
    see get_ticks_list_test()
    """
    p_percent_jump = (x_high - x_low) / p
    x_ticks = [x_low + i * p_percent_jump for i in range(p + 1)]
    return x_ticks


def get_random_RBGA_color_map(n: int, opacity: float = 1.0) -> np.array:
    """
    get colors list uniform distribution
    :param n: how many colors
    :param opacity:
    :return: np array of size(n,4). each row in RGBA format
    see get_random_RGBA_color_map_test()
    """
    colors_map = mt.np_uniform(shape=(n, 4), lows=0, highs=1)
    colors_map[:, -1] = opacity
    return colors_map


def screen_dims() -> (int, int):
    """
    :requires pip install PIL
    see move_figure_test()
    """
    try:
        from PIL import ImageGrab
        img = ImageGrab.grab()
        window_w, window_h = img.size
    except (ValueError, Exception, ModuleNotFoundError) as e:
        window_w, window_h = 0, 0
        mt.exception_error(e)
    return window_w, window_h


def move_figure_x_y(fig: matplotlib.figure, x: int, y: int) -> None:
    """
    :param fig: figure to be moved
    :param x: x of top left corner
    :param y: y of top left corner
    Move figure's upper left corner to pixel (x, y)
    see move_figure_test()
    """
    try:
        x, y = int(x), int(y)
        new_geom = "+{}+{}".format(x, y)
        backend = matplotlib.get_backend()
        if backend == 'TkAgg':
            manager = fig.canvas.manager
            manager.window.wm_geometry(new_geom)
        elif backend == 'WXAgg':
            fig.canvas.manager.window.SetPosition((x, y))
        else:
            # This works for QT and GTK
            # You can also use window.setGeometry
            fig.canvas.manager.window.move(x, y)
    except (ValueError, Exception) as e:
        mt.exception_error(e)
    return


def move_figure_by_str(fig: matplotlib.figure, where: str = 'top_left') -> None:
    """
    :param fig: figure to be moved
    :param where: top_right, top_center, top_left, bottom_right, bottom_center, bottom_left
    see move_figure_by_str_test()
    """
    try:
        window_w, window_h = screen_dims()  # screen dims in pixels
        fig_w, fig_h = fig.get_size_inches() * fig.dpi  # fig dims in pixels
        task_bar_offset = 100  # about 100 pixels due to task bar

        x, y = 0, 0  # top_left: default

        if where == 'top_center':
            x, y = (window_w - fig_w) / 2, 0
        elif where == 'top_right':
            x, y = (window_w - fig_w), 0
        elif where == 'bottom_left':
            x, y = 0, window_h - fig_h - task_bar_offset
        elif where == 'bottom_center':
            x, y = (window_w - fig_w) / 2, window_h - fig_h - task_bar_offset
        elif where == 'bottom_right':
            x, y = (window_w - fig_w), window_h - fig_h - task_bar_offset
        move_figure_x_y(fig=fig, x=x, y=y)
    except (ValueError, Exception) as e:
        mt.exception_error(e)
    return


def render(block: bool = False, pause: float = 0.0001) -> None:
    """
    :param block:
    :param pause:
    :return:
    just renders the 2d and 3d plots
    """
    plt.draw()
    plt.show(block=block)
    plt.pause(pause)
    return


# 2d plots
def plot_2d_iterative_figure(
        rows: int = 1,
        cols: int = 1,
        main_title: str = None,
        sub_titles: list = None,
        labels: list = None,
        default_color: str = 'green',
        resize: float = 0,
        plot_location: str = None,
        x_y_lims: list = None,
        add_center: dict = False,
        zoomed: bool = False,
        render_d: dict = None
) -> (matplotlib.figure, list, list):
    """
    THIS is for building a figure with 1 or more subplots that changes each iteration.
        this function just builds the frame. use update_subplots to insert\change the data of the scatters
    :param rows:
    :param cols:
    :param main_title:
    :param sub_titles: if not None, sub title to each sub plots. |sub_titles| must be equal to rows*cols
    :param labels: if labels are given to each subplot, legend will be on
    :param default_color: when updating, color is not mandatory. if non given, default color will remain
    :param resize: if not 0, figure size *= resize
    :param plot_location: top_right, top_center, top_left, bottom_right, bottom_center, bottom_left or None
    :param x_y_lims: limits of x and y axes. list of 4 ints: x_left, x_right, y_bottom, y_top
    :param add_center: dict. if not None - add center with the params in the dict
        e.g. add_center = {'c': 'orange', 'marker': 'x', 'marker_size': 150, 'label': 'Scene Center'}
    :param zoomed: bool - full screen or not
    :param render_d: dict - if not None: show plot
        block mandatory. pause optional.
        e.g. render = {'block': False, 'pause': 0.0001}
    :return:
    figure
    list of axes
    list of scatters (1 for each ax in axes - this will be used to update the data)

    see plot_2d_iterative_test()
    """
    plt.close('all')
    figsize = (6.4, 4.8) if resize == 0 else (6.4 * resize, 4.8 * resize)  # default figsize=(6.4, 4.8)
    fig, axes = plt.subplots(nrows=rows, ncols=cols, sharex=False, sharey=False, figsize=figsize)
    axes_list = [axes] if (rows == 1 and cols == 1) else axes.flatten().tolist()

    if sub_titles is not None:
        err_msg = '|sub_titles| must be equal to rows*cols ({}!={})'.format(len(sub_titles), rows * cols)
        assert len(sub_titles) == len(axes_list), err_msg
    if labels is not None:
        err_msg = '|labels| must be equal to rows*cols ({}!={})'.format(len(labels), rows * cols)
        assert len(labels) == len(axes_list), err_msg

    if main_title is not None:
        fig.suptitle(main_title)
    if plot_location is not None:
        move_figure_by_str(fig, where=plot_location)

    scatters = []
    for i, ax in enumerate(axes_list):
        if sub_titles is not None:
            ax.set_title(sub_titles[i])
        ax.set_aspect('equal', adjustable='box')

        # init data scatter for this axis
        if labels is not None:
            sc = ax.scatter([0], [0], c=default_color, marker='.', label=labels[i])
            ax.legend(loc='upper right', ncol=1, fancybox=True, framealpha=0.5, edgecolor='black')
        else:
            sc = ax.scatter([0], [0], c=default_color, marker='.')
        scatters.append(sc)

        if x_y_lims is not None:
            ax.set_xlim(left=x_y_lims[0], right=x_y_lims[1])
            ax.set_ylim(bottom=x_y_lims[2], top=x_y_lims[3])
            # scatters.append(sc)

        x_left, x_right = ax.get_xlim()
        y_bottom, y_top = ax.get_ylim()

        cx = (x_right - x_left) / 2 + x_left
        cy = (y_top - y_bottom) / 2 + y_bottom

        ax.set_xticks([x_left, cx, x_right])
        ax.set_yticks([y_bottom, cy, y_top])

        if add_center is not None:
            ax.scatter(
                [cx], [cy],
                c=add_center['c'], marker=add_center['marker'],
                s=add_center['marker_size'], label='{}({},{})'.format(add_center['label'], cx, cy)
            )

    if zoomed:
        wm = plt.get_current_fig_manager()
        wm.window.state('zoomed')

    if render_d is not None:
        if 'pause' in render_d:
            render(block=render_d['block'], pause=render_d['pause'])
        else:
            render(block=render_d['block'])
    return fig, axes_list, scatters


def update_2d_scatters(
        scatters: list,
        datum: list,
        colors_sets: list = None,
        new_title: str = None,
        save_img_path: str = None,
        tabs: int = 1,
        render_d: dict = None
) -> None:
    """
    :param scatters: list of scatters to update
    :param datum: list of data per scatter.
            |datum| == |scatters|
            data could be empty list or None
    :param colors_sets: list of colors per scatter.
            if colors_sets is not None: |colors_sets| == |scatters| == |datum|
            color_set could be:
                empty list or None - former color will remain (first is default color)
                list of size 1 - RGBA color. all points will get this color
                list of size |data| - RGBA colors. each point will get it's corresponding color
    :param new_title: changed main title
    :param save_img_path: if not none, save the fig to this path
    :param tabs:
    :param render_d: dict - if not None: show plot
        block mandatory. pause optional.
        e.g. render = {'block': False, 'pause': 0.0001}

    see plot_2d_iterative_test()
    """
    assert len(datum) == len(scatters), 'data per scatter is required.'
    err_msg = 'colors_sets should be none or same size as scatters and datum'
    assert colors_sets is None or len(colors_sets) == len(scatters) == len(datum), err_msg

    if new_title is not None:
        plt.suptitle(new_title)
    for i in range(len(scatters)):
        sc_i = scatters[i]
        if datum[i] is not None and len(datum[i]) > 0:
            sc_i._offsets = datum[i]
            if colors_sets is not None and colors_sets[i] is not None and len(colors_sets[i]) > 0:
                sc_i._facecolors = colors_sets[i]
                sc_i._edgecolors = colors_sets[i]

    if save_img_path is not None:
        plt.savefig(save_img_path, dpi=200, bbox_inches='tight')
        print('{}Saved {}.png'.format(tabs * '\t', save_img_path))

    if render_d is not None:
        if 'pause' in render_d:
            render(block=render_d['block'], pause=render_d['pause'])
        else:
            render(block=render_d['block'])
    return


def plot_2d_scatter(
        data: np.array,
        colors: list = None,
        data_label: str = None,
        main_title: str = None,
        sub_title: str = None,
        def_color: str = None,
        resize: float = 0,
        plot_location=None,
        x_y_lims=None,
        save_img_path: str = None,
        add_center: dict = False,
        zoomed: bool = False,
) -> None:
    """
    see documentation in plot_2d_iterative_figure() and update_2d_scatters()
    see plot_2d_scatter_test()
    """
    fig, axes_list, scatters = plot_2d_iterative_figure(
        rows=1,
        cols=1,
        main_title=main_title,
        sub_titles=[sub_title],
        labels=[data_label],
        default_color=def_color,
        resize=resize,
        plot_location=plot_location,
        x_y_lims=x_y_lims,
        add_center=add_center,
        zoomed=zoomed,
        render_d=None
    )
    update_2d_scatters(
        scatters=scatters,
        datum=[data],
        colors_sets=[colors],
        new_title=None,
        save_img_path=save_img_path,
        render_d={'block': True}
    )
    return


def plot_x_y_std(
        data_x: np.array,
        groups: list,
        title: str = None,
        x_label: str = 'Size',
        y_label: str = 'Error',
        save_path: str = None,
        tabs: int = 1,
        show_plot: bool = True,
        with_shift: bool = False
) -> None:
    """
    :param data_x: x values for all groups
    :param groups: list of groups s.t. each tuple(y values, y std, color, title)  y std could be None
    :param title:
    :param x_label:
    :param y_label:
    :param save_path:
    :param tabs:
    :param show_plot:
    :param with_shift: moves a bit the point x's so it won't be one on another - blocking the view
    see plot_x_y_std_test()
    """
    data_x_last = data_x  # in order to see all STDs, move a little on the x axis
    data_x_jump = 0.5
    data_x_offset = - int(len(groups) / 2) * data_x_jump
    line_style = {"linestyle": "-", "linewidth": 1, "markeredgewidth": 2, "elinewidth": 1, "capsize": 4}
    for i, group in enumerate(groups):
        data_y, std_y = group[0], group[1]  # std_y could be None
        color, label = group[2], group[3]
        if with_shift:  # move x data for each set a bit so you can see it clearly
            dx_shift = [x + i * data_x_jump + data_x_offset for x in data_x]
            data_x_last = dx_shift
        plt.errorbar(data_x_last, data_y, std_y, color=color, fmt='.', label=label, **line_style)

    plt.grid()
    plt.legend(loc='upper right', ncol=1, fancybox=True, framealpha=0.5)
    if title is not None:
        plt.title(title)
    plt.xticks(data_x)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    if save_path is not None:
        plt.savefig(save_path, dpi=100, bbox_inches='tight')
        print('{}Saved: {}.png'.format(tabs * '\t', save_path))
    plt.pause(0.0001)
    if show_plot:
        plt.show(block=True)
    plt.cla()
    return


def histogram(values: np.array, title: str, bins_n: int = 50, save_path: str = None, tabs: int = 1) -> None:
    """
    :param values:
    :param title:
    :param bins_n:
    :param save_path:
    :param tabs:
    plots a histogram
    see histogram_test()
    """
    plt.hist(values, bins_n, density=False, facecolor='blue', alpha=0.75)
    plt.xlabel('Values')
    plt.ylabel('Bin Count')
    plt.title(title)
    plt.grid(True)
    if save_path is not None:
        plt.savefig(save_path, dpi=100, bbox_inches='tight')
        print('{}Saved: {}.png'.format(tabs * '\t', save_path))
    plt.show()
    plt.cla()
    return


def compare_images_sets(set_a, set_b, title: str = None) -> None:
    """
    build for images BEFORE transform:
    notice images should be in the format:
        gray scale mnist: [number of images, 28, 28]
        RGB  Cifar10    : [number of images, 32, 32, 3]

    :param set_a: array (nd\torch) of images
    :param set_b: array (nd\torch) of images
    :param title: plot title
    plot set a of images in row 1 and set b in row 2
    set_a and set_b can be ndarray or torch arrays
    see compare_images_sets_test()
    """
    n_cols = max(set_a.shape[0], set_b.shape[0])
    fig, axes = plt.subplots(nrows=2, ncols=n_cols, sharex='all', sharey='all', figsize=(15, 4))
    for images, row in zip([set_a, set_b], axes):
        for img, ax in zip(images, row):
            ax.imshow(np.squeeze(img), cmap='gray')
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
    if title is not None:
        plt.title(title)
    plt.show()
    return


def compare_images_multi_sets_squeezed(
        sets_dict: dict, title: str = None, desc: bool = True, tabs: int = 0
) -> None:
    """
    build for images AFTER transform:
    notice images should be in the format:
        gray scale mnist: [number of images, 1, 28, 28]
        RGB  Cifar10    : [number of images, 3, 32, 32]

    :param sets_dict: each entry in dict is title, set of images(np/tensor)
    :param title: for plot
    :param desc: str with details which set in each row
    :param tabs:
    plot sets of images in rows
    see compare_images_multi_sets_squeezed_test()
    """
    try:
        from wizzi_utils.torch import torch_tools as tt
        from torchvision.utils import make_grid
        import torch
        for k, v in sets_dict.items():
            if isinstance(sets_dict[k], np.ndarray):
                sets_dict[k] = tt.numpy_to_torch(sets_dict[k])

        all_sets = None
        msg = ''
        set_len = 0
        msg_base = 'row {}: {}, '

        for i, (k, v) in enumerate(sets_dict.items()):
            all_sets = v if all_sets is None else torch.cat((all_sets, v), 0)
            msg += msg_base.format(i, k)
            set_len = v.shape[0]

        grid_images = make_grid(all_sets, nrow=set_len)
        if title is not None:
            plt.title(title)
        plt.axis('off')
        if desc:
            print(tabs * '\t', msg)
        plt.imshow(np.transpose(tt.torch_to_numpy(grid_images), (1, 2, 0)))
        plt.show()
    except ModuleNotFoundError as e:
        mt.exception_error(e)
    return


# 3d plots
def plot_3d_iterative_figure(
        scatter_dict: dict,
        main_title: str = None,
        resize: float = 0,
        plot_location: str = None,
        x_y_z_lims: list = None,
        fig_face_color: str = None,
        ax_background: str = None,
        ax_labels_and_ticks_c: str = None,
        add_center: dict = None,
        zoomed: bool = False,
        view: dict = None,
        render_d: dict = None
) -> (matplotlib.figure, Axes3D, Path3DCollection, FigureCanvasTkAgg):
    """
    THIS is for building a figure with 1 or more subplots that changes each iteration.
        this function just builds the frame. use update_subplots to insert\change the data of the scatters
    :param scatter_dict: dict with mandatory entries of the main scatter
        e.g. {'c': 'b', 'marker_size': 1, 'marker': 'o', 'label': 'MVS'} # c for color
    :param main_title:
    :param resize: if not 0, figure size *= resize
    :param plot_location: top_right, top_center, top_left, bottom_right, bottom_center, bottom_left or None
    :param x_y_z_lims: limits of x, y and z axes. list of 6 ints: x_left, x_right, y_bottom, y_top, z_in, z_out
    :param fig_face_color: color of the whole background - default is white
    :param ax_background: color of the axes background - default is white
    :param ax_labels_and_ticks_c: color of the ticks and axes labels
    :param add_center: dict. if not None - add center with the params in the dict
        e.g. add_center = {'c': 'orange', 'marker': 'x', 'marker_size': 150, 'label': 'Scene Center'}
    :param zoomed: bool - full screen or not
    :param view: dict - view onto the world. e.g. {'azim': 90.0, 'elev': -100.0}
    :param render_d: dict - if not None: show plot
        block mandatory. pause optional.
        e.g. render = {'block': False, 'pause': 0.0001}
    :return:
    figure
    axes3d
    Path3DCollection (pointer to the scatter data) - used for updating
    FigureCanvasTkAgg - used to change title
    see plot_3d_iterative_test()
    """
    plt.close('all')
    figsize = (6.4, 4.8) if resize == 0 else (6.4 * resize, 4.8 * resize)  # default figsize=(6.4, 4.8)
    fig = plt.figure(figsize=figsize)
    fig_canvas = fig.canvas
    ax = Axes3D(fig)
    if fig_face_color is not None:
        ax.set_facecolor(fig_face_color)

    if ax_background is not None:
        ax_background = get_RGBA_color(ax_background)
        ax.w_xaxis.set_pane_color(ax_background)
        ax.w_yaxis.set_pane_color(ax_background)
        ax.w_zaxis.set_pane_color(ax_background)

    if main_title is not None:
        fig.suptitle(main_title)
    if plot_location is not None:
        move_figure_by_str(fig, where=plot_location)

    if x_y_z_lims is not None:
        ax.set_xlim3d(left=x_y_z_lims[0], right=x_y_z_lims[1])
        ax.set_ylim3d(bottom=x_y_z_lims[2], top=x_y_z_lims[3])
        ax.set_zlim3d(bottom=x_y_z_lims[4], top=x_y_z_lims[5])

    x_left, x_right = ax.get_xlim()
    y_bottom, y_top = ax.get_ylim()
    z_in, z_out = ax.get_zlim()

    cx = int((x_right - x_left) / 2) + x_left
    cy = int((y_top - y_bottom) / 2) + y_bottom
    cz = int((z_out - z_in) / 2) + z_in

    ax.set_xticks([x_left, cx, x_right])
    ax.set_yticks([y_bottom, cy, y_top])
    ax.set_zticks([z_in, cz, z_out])

    if ax_labels_and_ticks_c is not None:
        ax.w_xaxis.line.set_color(ax_labels_and_ticks_c)
        ax.w_yaxis.line.set_color(ax_labels_and_ticks_c)
        ax.w_zaxis.line.set_color(ax_labels_and_ticks_c)
        ax.tick_params(axis='x', colors=ax_labels_and_ticks_c)
        ax.tick_params(axis='y', colors=ax_labels_and_ticks_c)
        ax.tick_params(axis='z', colors=ax_labels_and_ticks_c)
        ax.set_xlabel("X", color=ax_labels_and_ticks_c)
        ax.set_ylabel("Y", color=ax_labels_and_ticks_c)
        ax.set_zlabel("Z", color=ax_labels_and_ticks_c)
    else:
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

    if add_center is not None:
        ax.scatter(
            cx, cy, cz,
            c=add_center['c'], marker=add_center['marker'],
            s=add_center['marker_size'], label='{}({},{},{})'.format(add_center['label'], cx, cy, cz)
        )

    iterative_scatter = ax.scatter(
        0, 0, 0,
        c=scatter_dict['c'], marker=scatter_dict['marker'],
        s=scatter_dict['marker_size'], label=scatter_dict['label']
    )

    plt.legend(loc='upper right', ncol=1, fancybox=True, framealpha=0.5)

    if view is not None:
        ax.view_init(azim=view['azim'], elev=view['elev'])

    if zoomed:
        wm = plt.get_current_fig_manager()
        wm.window.state('zoomed')

    if render_d is not None:
        if 'pause' in render_d:
            render(block=render_d['block'], pause=render_d['pause'])
        else:
            render(block=render_d['block'])
    return fig, ax, iterative_scatter, fig_canvas


def update_3d_scatters(
        scatter: Path3DCollection,
        fig_canvas: FigureCanvasTkAgg,
        data: np.array,
        colors: [list, np.array] = None,
        new_title: str = None,
        save_img_path: str = None,
        tabs: int = 1,
        render_d: dict = None
) -> None:
    """
    :param scatter: the data scatter obj
    :param fig_canvas: used to change title
    :param data: array of 3d data.
    :param colors: list of colors. None, 1 color or |data| colors. rgba format
    :param new_title: changed main title
    :param save_img_path: if not none, save the fig to this path
    :param tabs:
    :param render_d: dict - if not None: show plot
        block mandatory. pause optional.
        e.g. render = {'block': False, 'pause': 0.0001}
    see plot_3d_iterative_test()
    """
    fig_canvas.set_window_title(new_title)
    scatter._offsets3d = data.T

    if colors is not None:
        scatter._facecolor3d = colors
        scatter._edgecolor3d = colors

    if save_img_path is not None:
        plt.savefig(save_img_path, dpi=200, bbox_inches='tight')
        print('{}Saved: {}.png'.format(tabs * '\t', save_img_path))

    if render_d is not None:
        if 'pause' in render_d:
            render(block=render_d['block'], pause=render_d['pause'])
        else:
            render(block=render_d['block'])
    return


def plot_3d_scatter(
        scatter_dict: dict,
        data: np.array,
        colors: [list, np.array] = None,
        main_title: str = None,
        resize: float = 0,
        plot_location: str = None,
        x_y_z_lims: list = None,
        fig_face_color: str = None,
        ax_background: str = None,
        ax_labels_and_ticks_c: str = 'black',
        add_center: dict = False,
        zoomed: bool = False,
        view: dict = None,
        save_img_path: str = None,
) -> None:
    """
    see documentation in plot_3d_iterative_figure() and update_3d_scatters()
    see plot_3d_scatter_test()
    """
    fig, ax, iterative_scatter, fig_canvas = plot_3d_iterative_figure(
        scatter_dict=scatter_dict,
        main_title=main_title,
        resize=resize,
        plot_location=plot_location,
        x_y_z_lims=x_y_z_lims,
        fig_face_color=fig_face_color,
        ax_background=ax_background,
        ax_labels_and_ticks_c=ax_labels_and_ticks_c,
        add_center=add_center,
        zoomed=zoomed,
        view=view,
        render_d=None
    )

    update_3d_scatters(
        scatter=iterative_scatter,
        fig_canvas=fig_canvas,
        data=data,
        colors=colors,
        new_title=None,
        save_img_path=save_img_path,
        render_d={'block': True}
    )
    return


def plot_3d_cube(axes: Axes3D, cube_definition: list, color='b', label='cube', add_labels=False) -> None:
    """
    :param axes:
    :param cube_definition: list of np.arrays
        4 points of the cube (1 corner node and 3 nodes to the left right and top)
    :param color:
    :param label:
    :param add_labels: add cube corners label on figure
    see plot_3d_cube_test()
    """

    points = []
    points += cube_definition
    vectors = [
        cube_definition[1] - cube_definition[0],
        cube_definition[2] - cube_definition[0],
        cube_definition[3] - cube_definition[0]
    ]

    points += [cube_definition[0] + vectors[0] + vectors[1]]
    points += [cube_definition[0] + vectors[0] + vectors[2]]
    points += [cube_definition[0] + vectors[1] + vectors[2]]
    points += [cube_definition[0] + vectors[0] + vectors[1] + vectors[2]]

    points = np.array(points)

    edges = [
        [points[0], points[3], points[5], points[1]],
        [points[1], points[5], points[7], points[4]],
        [points[4], points[2], points[6], points[7]],
        [points[2], points[6], points[3], points[0]],
        [points[0], points[2], points[4], points[1]],
        [points[3], points[6], points[7], points[5]]
    ]

    faces = Poly3DCollection(edges, linewidths=1, edgecolors='k')
    color_rgba = matplotlib.colors.to_rgba(color, alpha=0.1)
    faces.set_facecolor(color_rgba)
    axes.add_collection3d(faces)

    # Plot the points themselves to force the scaling of the axes
    axes.scatter(points[:, 0], points[:, 1], points[:, 2], s=0.1, color=color, label=label)

    if add_labels:
        for p in points:
            x, y, z = p
            text = '{},{},{}'.format(x, y, z)
            axes.text(x, y, z, text, zdir=(1, 1, 1))
    return


def add_cube3d_around_origin(axes: Axes3D, edge_len: int, color: str = 'b', add_labels: bool = False) -> None:
    """
    :param axes:
    :param edge_len: cube edge size
    :param color: cube color
    :param add_labels: add cube labels on the scene
    see add_cube3d_around_origin_test()
    """
    half_edge = int(edge_len / 2)
    xyz_bot_left = np.array([-half_edge, -half_edge, -half_edge], dtype=float)
    xyz_top_left = np.copy(xyz_bot_left)
    xyz_bot_right = np.copy(xyz_bot_left)
    xyz_bot_left_depth = np.copy(xyz_bot_left)
    xyz_top_left[1] += edge_len  # add just y
    xyz_bot_right[0] += edge_len  # add just x
    xyz_bot_left_depth[2] += edge_len  # add just z

    cube_4_edges = [xyz_bot_left, xyz_top_left, xyz_bot_right, xyz_bot_left_depth]
    plot_3d_cube(
        axes=axes,
        cube_definition=cube_4_edges,
        label='cube(edge={})'.format(edge_len),
        color=color,
        add_labels=add_labels
    )
    return
