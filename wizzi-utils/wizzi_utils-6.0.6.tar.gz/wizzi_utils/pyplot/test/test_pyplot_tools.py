from wizzi_utils.pyplot import pyplot_tools as pyplt
from wizzi_utils.misc import misc_tools as mt
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def get_colors_formats_test():
    mt.get_function_name(ack=True, tabs=0)
    color_str = 'orange'
    rgb = pyplt.get_RGB_color(color_str)
    rgba = pyplt.get_RGBA_color(color_str)
    bgr = pyplt.get_BGR_color(color_str)
    print('\tcolor {}: RGB={}, RGBA={}, BGR={}'.format(color_str, rgb, rgba, bgr))
    return


def RGBA_to_RGB_and_BGR_test():
    mt.get_function_name(ack=True, tabs=0)
    color_str = 'orange'
    rgb = pyplt.get_RGB_color(color_str)
    bgr = pyplt.get_BGR_color(color_str)

    rgba = pyplt.get_RGBA_color(color_str)
    rgb2 = pyplt.RGBA_to_RGB(rgba)
    bgr2 = pyplt.RGBA_to_BGR(rgba)

    print('\tRGBA {} - {}'.format(rgba, color_str))
    print('\tRGB {}=={} ? {}'.format(rgb, rgb2, rgb == rgb2))
    print('\tBGR {}=={} ? {}'.format(bgr, bgr2, bgr == bgr2))
    return


def BGR_to_RGB_and_RGBA_test():
    mt.get_function_name(ack=True, tabs=0)
    color_str = 'orange'
    rgb = pyplt.get_RGB_color(color_str)
    rgba = pyplt.get_RGBA_color(color_str)

    bgr = pyplt.get_BGR_color(color_str)
    rgb2 = pyplt.BGR_to_RGB(bgr)
    rgba2 = pyplt.BGR_to_RGBA(bgr)
    print('\tBGR {} - {}'.format(bgr, color_str))
    print('\tRGB {}=={} ? {}'.format(rgb, rgb2, rgb == rgb2))
    print('\tRGBA {}=={} ? {}'.format(rgba, rgba2, rgba == rgba2))
    return


def RGB_to_RGBA_and_BGR_test():
    mt.get_function_name(ack=True, tabs=0)
    color_str = 'orange'
    bgr = pyplt.get_BGR_color(color_str)
    rgba = pyplt.get_RGBA_color(color_str)

    rgb = pyplt.get_RGB_color(color_str)
    bgr2 = pyplt.RGB_to_BGR(rgb)
    rgba2 = pyplt.RGB_to_RGBA(rgb)
    print('\tRGB {} - {}'.format(rgb, color_str))
    print('\tRGBA {}=={} ? {}'.format(rgba, rgba2, rgba == rgba2))
    print('\tBGR {}=={} ? {}'.format(bgr, bgr2, bgr == bgr2))
    return


def get_ticks_list_test():
    mt.get_function_name(ack=True, tabs=0)
    ticks_list = pyplt.get_ticks_list(x_low=10, x_high=30, p=10)
    print(mt.to_str(ticks_list, '\tticks_list'))
    return


def get_random_RGBA_color_map_test():
    mt.get_function_name(ack=True, tabs=0)
    random_RBGA_colors = pyplt.get_random_RBGA_color_map(n=3)
    print(mt.to_str(random_RBGA_colors, '\trandom_color_map'))
    return


def screen_dims_test():
    mt.get_function_name(ack=True, tabs=0)
    sd = pyplt.screen_dims()
    print('\tscreen dims {}'.format(sd))
    return


def move_figure_x_y_test():
    def on_click(event):
        import sys
        sys.stdout.flush()
        if event.key == 'escape':
            plt.close('all')

    mt.get_function_name(ack=True, tabs=0)
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)
    options = [(0, 0), (100, 0), (0, 100), (150, 150), (400, 400), (250, 350)]
    print('\tVisual test: move to all options {}'.format(options))
    print('\t\tClick Esc to close all')
    for x, y in options:
        title = 'move to ({}, {})'.format(x, y)
        fig, ax = plt.subplots()
        fig.canvas.set_window_title(title)
        fig.canvas.mpl_connect('key_press_event', pyplt.on_click)
        ax.plot(t, s)
        pyplt.move_figure_x_y(fig, x=x, y=y)
    plt.show(block=True)
    return


def move_figure_by_str_test():
    mt.get_function_name(ack=True, tabs=0)
    t = np.arange(0.0, 2.0, 0.01)
    s = 1 + np.sin(2 * np.pi * t)
    options = ['top_right', 'top_center', 'top_left', 'bottom_right', 'bottom_center', 'bottom_left']
    print('\tVisual test: move to all options {}'.format(options))
    print('\t\tClick Esc to close all')
    for where_to in options:
        title = 'move to {}'.format(where_to)
        fig, ax = plt.subplots()
        fig.canvas.set_window_title(title)
        fig.canvas.mpl_connect('key_press_event', pyplt.on_click)
        ax.plot(t, s)
        pyplt.move_figure_by_str(fig, where=where_to)
    plt.show(block=True)
    return


def plot_2d_iterative_test():
    mt.get_function_name(ack=True, tabs=0)
    iters = 3
    print('\tVisual test: {} iters of 2d iterative plot'.format(iters))
    fig, axes_list, scatters = pyplt.plot_2d_iterative_figure(
        rows=1,
        cols=2,
        main_title='1x1 scatter',
        window_title='1x1 scatter',
        legend=pyplt.LEGEND_DEFAULT,
        sub_titles=['left cam', 'right cam'],
        labels=['MVS1', 'MVS2'],
        default_color='blue',
        resize=0,
        # plot_location='top_center',
        plot_location=None,
        x_y_lims=[0, 640, 0, 480],  # fits cv img
        add_center={'c': 'orange', 'marker': 'x', 'marker_size': 150, 'label': 'Scene Center'},
        zoomed=False,
        render=False,  # if you wanna see the main figure before add ons and data
        block=False
    )

    for i in range(iters):
        mt.sleep(seconds=1)
        block = (i == 1)  # block first just for fun
        # emulate data of each scatter - say number of points is 3
        datum, colors_sets = [], []
        for j in range(len(scatters)):
            data_j = mt.np_random_integers(low=0, high=480, size=(3, 2))
            if j == 0:  # cam0
                colors = [pyplt.get_RGBA_color('y')]  # 1 color for all
            else:  # cam1
                colors = pyplt.get_random_RBGA_color_map(3)  # random color for each point
                # colors = [get_RGBA_color('r'), get_RGBA_color('b'), get_RGBA_color('g')]  # fixed color per point
            if i == 2 and j == 1:  # emulate in iter 2, cam 1 found no data
                data_j, colors = [], []
            datum.append(data_j)
            colors_sets.append(colors)

        pyplt.update_2d_scatters(
            fig=fig,
            scatters=scatters,
            datum=datum,
            colors_sets=colors_sets,
            new_title='iter {}'.format(i),
            save_img_path=None,
            render=True,
            block=block
        )

        # second option if you have more stuff to render
        # pyplt.render_plot(fig, block=block)
    pyplt.finalize_plot(fig)
    return


def plot_2d_scatter_test():
    mt.get_function_name(ack=True, tabs=0)
    data_j = mt.np_random_integers(low=0, high=480, size=(3, 2))
    colors = [pyplt.get_RGBA_color('r'), pyplt.get_RGBA_color('b'), pyplt.get_RGBA_color('g')]
    save_path = './test'  # .png will be added
    print('\tVisual test: scatter 2d plot')
    pyplt.plot_2d_scatter(
        data=data_j,
        colors=colors,
        data_label='SCP',
        window_title='1x1 scatter',
        legend=pyplt.LEGEND_DEFAULT,
        main_title='1x1 scatter',
        sub_title='normal 2d scatter',
        def_color='green',
        resize=1.3,
        # plot_location='top_center',
        plot_location=None,
        x_y_lims=[0, 640, 0, 480],  # fits cv img,
        save_img_path=save_path,
        add_center={'c': 'orange', 'marker': 'x', 'marker_size': 150, 'label': 'Scene Center'},
        zoomed=False,
    )
    mt.delete_file('{}.png'.format(save_path), ack=True)
    return


def plot_x_y_std_test():
    mt.get_function_name(ack=True, tabs=0)
    data_x = [10, 20, 30]

    C_errors = [5, 7, 1]
    C_errors_stds = [2, 1, 0.5]
    group_c = (C_errors, C_errors_stds, 'g', 'C')

    U_errors = [10, 8, 3]
    U_errors_vars = [4, 3, 1.5]
    group_u = (U_errors, U_errors_vars, 'r', 'U')

    print('\tVisual test: errors and stds')
    pyplt.plot_x_y_std(
        data_x,
        groups=[group_c, group_u],
        title='bla',
        legend=pyplt.LEGEND_DEFAULT,
        x_label='X',
        y_label='Y',
        save_path=None,
        show_plot=True,
        with_shift=True
    )
    return


def histogram_test():
    mt.get_function_name(ack=True, tabs=0)
    data = mt.np_uniform(shape=1000, lows=0, highs=10000)
    print('\tVisual test: histogram')
    pyplt.histogram(
        values=data,
        title='histogram: 10 bins of 1000 numbers from 0 to 10000',
        save_path=None,
        bins_n=10,
    )
    return


def compare_images_sets_test():
    mt.get_function_name(ack=True, tabs=0)
    try:
        from torchvision import datasets
        # choose data set - both work
        # data_root = path to the data else download
        print('\tVisual test: 2 compare_images_sets')
        data_root = './Datasets/'
        mt.create_dir(data_root, ack=True)  # TODO - delete folder?
        # dataset = datasets.MNIST(root=data_root, train=False, download=True)
        dataset = datasets.CIFAR10(root=data_root, train=False, download=True)
        set_a = dataset.data[:3]
        set_b = dataset.data[10:50]
        pyplt.compare_images_sets(set_a, set_b)
        set_a = dataset.data[0:3]
        set_b = dataset.data[0:3]
        pyplt.compare_images_sets(set_a, set_b)
    except ModuleNotFoundError as e:
        mt.exception_error(e)
    return


def compare_images_multi_sets_squeezed_test():
    mt.get_function_name(ack=True, tabs=0)
    try:
        import torch
        from torchvision import datasets
        import torchvision.transforms as transforms
        transform = transforms.Compose([transforms.ToTensor(), ])
        # choose data set - both work
        # data_root = path to the data else download
        print('\tVisual test: 2 compare_images_multi_sets_squeezed')
        data_root = './Datasets/'
        mt.create_dir(data_root, ack=True)  # TODO - delete folder?
        # dataset = datasets.MNIST(root=data_root, train=False, download=False, transform=transform)
        dataset = datasets.CIFAR10(root=data_root, train=False, download=False, transform=transform)
        data_loader = torch.utils.data.DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2)
        images32, labels = iter(data_loader).next()

        images = images32[:16]  # imagine the first 16 are base images and predicted_images are the model output
        predicted_images = images32[16:32]
        d = {'original_data': images, 'predicted_data': predicted_images}
        pyplt.compare_images_multi_sets_squeezed(
            sets_dict=d, title='comp', desc=True, tabs=1
        )
    except ModuleNotFoundError as e:
        mt.exception_error(e)
    return


def plot_3d_iterative_test():
    mt.get_function_name(ack=True, tabs=0)
    iters = 3
    print('\tVisual test: {} iters of 3d iterative plot'.format(iters))
    fig, ax, iterative_scatter = pyplt.plot_3d_iterative_figure(
        scatter_dict={'c': 'b', 'marker_size': 100, 'marker': 'o', 'label': 'MVS'},
        main_title='3d scatter plot',
        window_title='3d scatter plot',
        legend={'loc': 'lower left', 'ncol': 1, 'fancybox': True, 'framealpha': 0.5, 'edgecolor': 'black'},
        resize=1.3,
        # plot_location='top_center',
        plot_location=None,
        x_y_z_lims=[-20, 20, -20, 20, -20, 20],
        fig_face_color=None,
        ax_background=None,
        ax_labels_and_ticks_c=None,
        add_center={'c': 'orange', 'marker': 'x', 'marker_size': 150, 'label': 'Scene Center'},
        zoomed=False,
        view=None,
        render=False,  # if you wanna see the main figure before add ons and data
        block=False
    )

    # # CUSTOM ADD ON 1 - update each round
    center_mass_x_y = {"x1": 0.05, "y1": 0.95, }
    center_mass_label_base = "(xyz)={}"
    center_mass_label = ax.text2D(
        x=center_mass_x_y['x1'],
        y=center_mass_x_y['y1'],
        s=center_mass_label_base.format(np.zeros(3)),
        transform=ax.transAxes,
        color='green'
    )

    # # CUSTOM ADD ON 2 - done once
    pyplt.add_cube3d_around_origin(ax, edge_len=4, add_labels=False)

    # should call legend if you want custom add ons in it
    # plt.legend(loc='upper right', ncol=1, fancybox=True, framealpha=0.5)

    pyplt.render_plot(fig=fig, block=False)  # not necessary - only if you want to see the plot before first data comes

    num_points = 5

    for i in range(iters):
        mt.sleep(seconds=1)
        data_j = mt.np_random_integers(low=-15, high=15, size=(num_points, 3))
        colors = pyplt.get_random_RBGA_color_map(num_points)
        block = (i == 1)  # block second iter - just for fun

        pyplt.update_3d_scatters(
            fig=fig,
            scatter=iterative_scatter,
            data=data_j,
            colors=colors,
            new_title='iter {}'.format(i),
            render=False,
            block=False
        )

        # # CUSTOM ADD ON 1 - update each round
        center_mass_label.set_text(center_mass_label_base.format(np.round(np.mean(data_j, axis=0), 2)))
        pyplt.render_plot(fig, block=block)  # must render here due to custom add on

    pyplt.finalize_plot(fig)
    return


def plot_3d_scatter_test():
    mt.get_function_name(ack=True, tabs=0)

    num_points = 50
    data_j = mt.np_random_integers(low=-15, high=15, size=(num_points, 3))
    save_path = './3dplot'
    print('\tVisual test: scatter 3d plot')
    pyplt.plot_3d_scatter(
        scatter_dict={'c': 'b', 'marker_size': 100, 'marker': 'o', 'label': 'MVS'},
        data=data_j,
        colors=pyplt.get_random_RBGA_color_map(num_points),
        main_title='3d scatter plot',
        window_title='3d scatter plot',
        legend=pyplt.LEGEND_DEFAULT,
        resize=1.5,
        # plot_location='top_center',
        plot_location=None,
        x_y_z_lims=[-20, 20, -20, 20, -20, 20],
        fig_face_color=None,
        ax_background=None,
        ax_labels_and_ticks_c=None,
        add_center={'c': 'orange', 'marker': 'x', 'marker_size': 150, 'label': 'Scene Center'},
        zoomed=False,
        view=None,
        save_img_path=save_path
    )
    mt.delete_file('{}.png'.format(save_path))
    return


def plot_3d_cube_test():
    mt.get_function_name(ack=True, tabs=0)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    # base on 0,0,0 and get points from left right and top by edge
    edge = 10.0
    point_base = np.array([0., 0., 0.])
    point_edge_left = np.array([0., edge, 0.])
    point_edge_right = np.array([edge, 0., 0.])
    point_edge_top = np.array([0., 0., edge])
    cube_def = [point_base, point_edge_left, point_edge_right, point_edge_top]

    pyplt.plot_3d_cube(
        ax,
        cube_definition=cube_def,
        color='r',
        add_labels=True
    )
    plt.legend(loc='upper right', ncol=1, fancybox=True, framealpha=0.5)
    # should call legend if you want custom add ons in it
    # plt.legend(loc='upper right', ncol=1, fancybox=True, framealpha=0.5)
    print('\tVisual test: plot_3d_cube_test')

    pyplt.finalize_plot(fig)
    return


def add_cube3d_around_origin_test():
    mt.get_function_name(ack=True, tabs=0)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    pyplt.add_cube3d_around_origin(
        ax,
        edge_len=4,
        color='green',
        add_labels=False
    )

    plt.legend(loc='upper right', ncol=1, fancybox=True, framealpha=0.5)
    print('\tVisual test: add_cube3d_around_origin')
    pyplt.finalize_plot(fig)
    return


def test_all():
    print('{}{}:'.format('-' * 5, mt.get_base_file_and_function_name()))
    get_colors_formats_test()
    RGBA_to_RGB_and_BGR_test()
    BGR_to_RGB_and_RGBA_test()
    RGB_to_RGBA_and_BGR_test()
    get_ticks_list_test()
    get_random_RGBA_color_map_test()
    screen_dims_test()
    move_figure_x_y_test()
    move_figure_by_str_test()
    plot_2d_iterative_test()
    plot_2d_scatter_test()
    plot_x_y_std_test()
    histogram_test()
    compare_images_sets_test()
    compare_images_multi_sets_squeezed_test()
    plot_3d_iterative_test()
    plot_3d_scatter_test()
    plot_3d_cube_test()
    add_cube3d_around_origin_test()
    print('{}'.format('-' * 20))
    return
