from wizzi_utils.misc import misc_tools as mt
import numpy as np


def timer_test():
    mt.get_function_name(ack=True, tabs=0)
    start_t = mt.get_timer()
    total = mt.get_timer_delta(start_timer=start_t, with_ms=True)
    total_full = mt.get_timer_delta(start_timer=start_t, with_ms=False)
    print('\tTotal run time {}'.format(total))
    print('\tTotal run time {}'.format(total_full))
    mt.get_timer_delta(start_timer=start_t, with_ms=False, ack=True, tabs=1)
    return


def timer_action_test():
    mt.get_function_name(ack=True, tabs=0)
    print('\ttimer count down example:')
    for i in range(3):
        mt.timer_action(seconds=2, action='take image {}'.format(i), tabs=2)
    print('\tpress key example:')
    mt.timer_action(seconds=None, action='taking an image', tabs=2)
    return


def get_current_date_hour_test():
    mt.get_function_name(ack=True, tabs=0)
    print('\tCurrent time is {}'.format(mt.get_current_date_hour()))
    mt.get_current_date_hour(ack=True, tabs=1)
    return


def get_pc_name_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_pc_name(ack=True, tabs=1)
    print('\tPc name is {}'.format(mt.get_pc_name()))
    return


def get_mac_address_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_mac_address(ack=True, tabs=1)
    mt.get_mac_address(add_semi_colons=False, ack=True, tabs=1)
    print('\tMac address is {}'.format(mt.get_mac_address()))
    return


def get_cuda_version_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_cuda_version(ack=True, tabs=1)
    print('\t{}'.format(mt.get_cuda_version()))
    return


def get_env_variables_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_env_variables(ack=True, tabs=1)
    return


def make_cuda_invisible_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.make_cuda_invisible()
    env_d = mt.get_env_variables()
    key = 'CUDA_VISIBLE_DEVICES'
    if key in env_d:
        print('\t{} = {}'.format(key, env_d[key]))
    else:
        print('\tTest Failed')
    try:  # if torch available
        from wizzi_utils import torch as tt
        print('\tcuda available ? {}'.format(tt.cuda_on()))
    except ModuleNotFoundError as e:
        mt.exception_error(e)
    return


def profiler_test():
    mt.get_function_name(ack=True, tabs=0)
    pr = mt.start_profiler()
    mt.get_function_name(ack=False)
    profiler_str = mt.end_profiler(pr, rows=5, ack=True)
    print(profiler_str)
    return


def get_tensorflow_version_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_tensorflow_version(ack=True, tabs=1)
    return


def main_wrapper_test():
    def temp_function():
        print('hello_world')

    mt.get_function_name(ack=True, tabs=0)
    mt.main_wrapper(
        main_function=temp_function,
        seed=42,
        cuda_off=True,
        torch_v=True,
        tf_v=True,
        cv2_v=True,
        with_profiler=False
    )
    return


def to_str_test():
    mt.get_function_name(ack=True, tabs=0)
    print('\t{}'.format(mt.to_str(var=1234)))
    print(mt.to_str(var=32223123123123123, title='\tvery long int'))
    print(mt.to_str(var=3.2, title='\tmy_float'))
    print(mt.to_str(var=3.2123123, title='\tmy_float(rounded to 4 digits)', float_precision=4))
    print(mt.to_str(var=1234567890.223123123123123123, title='\tmy_long_float', float_precision=3))
    print(mt.to_str(var='a', title='\tmy_str'))
    print(mt.to_str(var=[], title='\tmy_empty_list'))
    print(mt.to_str(var=[112312312, 3, 4], title='\t1d list of ints', recursive=True))
    print(mt.to_str(var=[1, 3123123], title='\t1d list of ints no data', data_chars=-1, recursive=True))  # no data
    print(mt.to_str(var=[1.0000012323, 3123123.22454875123123], title='\t1d list', float_precision=7))
    print(mt.to_str(var=np.array([1.0000012323, 3123123.22454875123123], dtype=float), title='\t1d np array',
                    float_precision=7, recursive=True))
    print(mt.to_str(var=[11235] * 1000, title='\t1d long list', recursive=True))
    print(mt.to_str(var=(1239, 3, 9), title='\t1d tuple', recursive=True))
    print(mt.to_str(var=[[1231.2123123, 15.9], [3.0, 7.55]], title='\t2d list', recursive=True))
    print(mt.to_str(var=[(1231.2123123, 15.9), (3.0, 7.55)], title='\t2d list of tuples', recursive=True))
    b = np.array([[1231.123122, 15.9], [3.0, 7.55]])
    print(mt.to_str(var=b, title='\t2d np array', recursive=True))
    cv_img = np.zeros(shape=[480, 640, 3], dtype=np.uint8)
    print(mt.to_str(var=cv_img, title='\tcv_img', data_chars=20, recursive=False))
    print(mt.to_str(var={'a': [1213, 2]}, title='\tdict of lists', recursive=True))
    print(mt.to_str(var={'a': [{'k': [1, 2]}, {'c': [7, 2]}]}, title='\tnested dict', recursive=True))
    return


def save_load_np_test():
    mt.get_function_name(ack=True, tabs=0)
    path = './a.npy'
    a = np.ones(shape=(2, 3, 29))
    print(mt.to_str(a, '\ta'))
    mt.save_np(a, path=path)
    a2 = mt.load_np(path, ack=True)
    print(mt.to_str(a2, '\ta2'))
    mt.delete_file(path, tabs=1)
    return


def save_load_npz_test():
    mt.get_function_name(ack=True, tabs=0)
    path = './b_c.npz'
    b = np.ones(shape=(2, 3, 29))
    c = np.ones(shape=(2, 3, 29))
    b_c = {'b': b, 'c': c}
    print(mt.to_str(b_c, '\tb_c'))
    mt.save_npz(b_c, path=path)
    b_c2 = mt.load_npz(path)
    print(mt.to_str(b_c2, '\tb_c2', recursive=True))
    mt.delete_file(path)
    return


def save_load_pkl_test():
    mt.get_function_name(ack=True, tabs=0)
    path = './data.pkl'
    a = {'2': 'a', 'b': 9, 'x': np.ones(shape=3)}
    print(mt.to_str(a, '\ta'))
    mt.save_pkl(data_dict=a, path=path)
    a2 = mt.load_pkl(path=path)
    print(mt.to_str(a2, '\ta2'))
    mt.delete_file(path)
    return


def get_uniform_dist_by_dim_test():
    mt.get_function_name(ack=True, tabs=0)
    A = np.array([[1, 100], [7, 210], [3, 421]])
    lows, highs = mt.get_uniform_dist_by_dim(A)
    print(mt.to_str(A, '\tA'))
    print(mt.to_str(lows, '\tlows'))
    print(mt.to_str(highs, '\thighs'))
    A = A.tolist()
    print(mt.to_str(A, '\tA'))
    lows, highs = mt.get_uniform_dist_by_dim(A)
    print(mt.to_str(lows, '\tlows'))
    print(mt.to_str(highs, '\thighs'))
    A = mt.np_uniform(shape=(500, 2), lows=[3, 200], highs=[12, 681])
    print(mt.to_str(A, '\tA(lows=[3, 200],highs=[12, 681])'))
    lows, highs = mt.get_uniform_dist_by_dim(A)
    print(mt.to_str(lows, '\tlows'))
    print(mt.to_str(highs, '\thighs'))
    return


def get_normal_dist_by_dim_test():
    mt.get_function_name(ack=True, tabs=0)
    A = np.array([[1, 100], [7, 210], [3, 421]])
    means, stds = mt.get_normal_dist_by_dim(A)
    print(mt.to_str(A, '\tA'))
    print(mt.to_str(means, '\tmeans'))
    print(mt.to_str(stds, '\tstds'))
    A = A.tolist()
    print(mt.to_str(A, '\tA'))
    means, stds = mt.get_normal_dist_by_dim(A)
    print(mt.to_str(means, '\tmeans'))
    print(mt.to_str(stds, '\tstds'))
    A = mt.np_normal(shape=(500, 2), mius=[3, 200], stds=[12, 121])
    print(mt.to_str(A, '\tA(mius=[3, 200],stds=[12, 121])'))
    means, stds = mt.get_normal_dist_by_dim(A)
    print(mt.to_str(means, '\tmeans'))
    print(mt.to_str(stds, '\tstds'))
    return


def np_uniform_test():
    mt.get_function_name(ack=True, tabs=0)
    A = mt.np_uniform(shape=(500, 2), lows=[3, 200], highs=[12, 681])
    print(mt.to_str(A, '\tA(lows=[3, 200],highs=[12, 681])'))
    return


def np_normal_test():
    mt.get_function_name(ack=True, tabs=0)
    A = mt.np_normal(shape=(500, 2), mius=[3, 200], stds=[12, 121])
    print(mt.to_str(A, '\tA(mius=[3, 200],stds=[12, 121])'))
    return


def generate_new_data_from_old_test():
    mt.get_function_name(ack=True, tabs=0)
    print('\tgenerate uniform data example')
    old_data = mt.np_uniform(shape=(500, 2), lows=[3, 200], highs=[12, 681])
    print(mt.to_str(old_data, '\t\told_data(lows=[3, 200],highs=[12, 681])'))
    new_data = mt.generate_new_data_from_old(old_data, new_data_n=4000, dist='uniform')
    lows, highs = mt.get_uniform_dist_by_dim(new_data)
    print(mt.to_str(new_data, '\t\tnew_data'))
    print(mt.to_str(lows, '\t\tlows'))
    print(mt.to_str(highs, '\t\thighs'))

    print('\tgenerate normal data example')
    old_data = mt.np_normal(shape=(500, 2), mius=[3, 200], stds=[12, 121])
    print(mt.to_str(old_data, '\t\told_data(mius=[3, 200],stds=[12, 121])'))
    new_data = mt.generate_new_data_from_old(old_data, new_data_n=4000, dist='normal')
    means, stds = mt.get_normal_dist_by_dim(new_data)
    print(mt.to_str(new_data, '\t\tnew_data'))
    print(mt.to_str(means, '\t\tmeans'))
    print(mt.to_str(stds, '\t\tstds'))
    return


def np_random_integers_test():
    mt.get_function_name(ack=True, tabs=0)
    random_ints = mt.np_random_integers(low=5, high=20, size=(2, 3))
    print(mt.to_str(random_ints, '\trandom_ints from 5-20'))
    return


def augment_x_y_numpy_test():
    mt.get_function_name(ack=True, tabs=0)
    X = mt.np_random_integers(low=5, high=20, size=(10, 3))
    Y = mt.np_random_integers(low=0, high=10, size=(10,))
    print(mt.to_str(X, '\tX'))
    print(mt.to_str(Y, '\tY'))
    A = mt.augment_x_y_numpy(X, Y)
    print(mt.to_str(A, '\tA'))
    return


def de_augment_numpy_test():
    mt.get_function_name(ack=True, tabs=0)
    A = mt.np_random_integers(low=5, high=20, size=(10, 4))
    print(mt.to_str(A, '\tA'))
    X, Y = mt.de_augment_numpy(A)
    print(mt.to_str(X, '\tX'))
    print(mt.to_str(Y, '\tY'))
    return


def nCk_test():
    mt.get_function_name(ack=True, tabs=0)
    A = np.random.randint(low=-10, high=10, size=(3, 2))
    print(mt.to_str(A, '\tA'))

    # let's iterate on every 2 different indices of A
    combs_count = mt.nCk(len(A), k=2, as_int=True)
    print('\t{}C2={}:'.format(len(A), combs_count))  # result is 3

    combs_list = mt.nCk(len(A), k=2)  # result is [[0, 1], [0, 2], [1, 2]]
    for i, comb in enumerate(combs_list):
        print('\t\tcomb {}={}. A[comb]={}'.format(i, comb, A[comb].tolist()))
    return


def redirect_std_test():
    mt.get_function_name(ack=True, tabs=0)
    old_stdout, summary_str = mt.redirect_std_start()
    print('\t\tbla bla bla')
    print('\t\tline2')
    string = mt.redirect_std_finish(old_stdout, summary_str)
    print('\tcaptured output:')
    print(string)
    return


def get_line_number_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_line_number(ack=True)
    return


def get_function_name_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_function_name(ack=True)
    return


def get_file_name_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_file_name(ack=True)
    return


def get_base_file_name_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_base_file_name(ack=True)
    return


def get_function_name_and_line_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_function_name_and_line(ack=True)
    return


def get_base_file_and_function_name_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.get_base_file_and_function_name(ack=True)
    return


def add_color_test():
    mt.get_function_name(ack=True, tabs=0)
    my_str = 'hello colorful world!'
    print('\t{}'.format(my_str))
    print('\t{}'.format(mt.add_color(my_str, color='Red')))
    print('\t{}'.format(mt.add_color(my_str, color='Blue')))
    print('\t{}'.format(mt.add_color(my_str, color='Bold')))
    print(mt.add_color(mt.to_str(my_str, '\tmy_str'), color='Green'))
    return


def logger_test():
    mt.get_function_name(ack=True, tabs=0)
    path = './log_{}.txt'.format(mt.get_time_stamp())
    mt.init_logger(logger_path=path)
    mt.log_print(line='\tline 1')
    mt.flush_logger()
    mt.log_print(line='line 2', tabs=1)
    mt.log_print(line='line 3', tabs=3)
    mt.close_logger()

    print('\treading from {}'.format(path))
    file1 = open(path, 'r')
    Lines = file1.readlines()
    file1.close()
    for i, line in enumerate(Lines):
        print("\t\tLine{}: {}".format(i + 1, line.rstrip()))
    mt.delete_file(path)
    return


def create_and_delete_dir_test():
    mt.get_function_name(ack=True, tabs=0)
    path = 'TEMP_DIR1'
    mt.create_dir(dir_path=path)
    mt.delete_dir(dir_path=path)
    return


def create_and_delete_dir_with_files_test():
    mt.get_function_name(ack=True, tabs=0)
    path = 'TEMP_DIR2'
    mt.create_dir(dir_path=path)
    f1 = open(file='./{}/temp1.txt'.format(path), mode='w', encoding='utf-8')
    f1.close()
    f2 = open(file='./{}/temp2.txt'.format(path), mode='w', encoding='utf-8')
    f2.close()
    mt.delete_dir(dir_path=path)
    mt.delete_dir_with_files(dir_path=path)
    return


def delete_file_test():
    mt.get_function_name(ack=True, tabs=0)
    path = './temp.txt'
    f1 = open(file=path, mode='w', encoding='utf-8')
    f1.close()
    mt.delete_file(file=path)
    return


def delete_files_test():
    mt.get_function_name(ack=True, tabs=0)
    path1 = './temp1.txt'
    f1 = open(file=path1, mode='w', encoding='utf-8')
    f1.close()
    path2 = './temp2.txt'
    f2 = open(file=path2, mode='w', encoding='utf-8')
    f2.close()
    mt.delete_files(files=[path1, path2])
    return


def sleep_test():
    mt.get_function_name(ack=True, tabs=0)
    mt.sleep(seconds=2, ack=True, tabs=1)
    return


def reverse_tuple_or_list_test():
    mt.get_function_name(ack=True, tabs=0)
    my_tuple = (0, 0, 255)
    print(mt.to_str(my_tuple, '\tmy_tuple'))
    print(mt.to_str(mt.reverse_tuple_or_list(my_tuple), '\tmy_tuple_reversed'))
    my_list = [0, 0, 255]
    print(mt.to_str(my_list, '\tmy_list'))
    print(mt.to_str(mt.reverse_tuple_or_list(my_list), '\tmy_list_reversed'))
    return


def get_time_stamp_test():
    mt.get_function_name(ack=True, tabs=0)
    print('\tdate no day: {}'.format(mt.get_time_stamp(format_s='%Y_%m')))
    print('\tdate: {}'.format(mt.get_time_stamp(format_s='%Y_%m_%d')))
    print('\ttime: {}'.format(mt.get_time_stamp(format_s='%H_%M_%S')))
    print('\tdate and time: {}'.format(mt.get_time_stamp(format_s='%Y_%m_%d_%H_%M_%S')))
    print('\tdate and time with ms: {}'.format(mt.get_time_stamp(format_s='%Y_%m_%d_%H_%M_%S_%f')))
    return


def test_all():
    print('{}{}:'.format('-' * 5, mt.get_base_file_and_function_name(depth=1)))
    timer_test()
    timer_action_test()
    get_current_date_hour_test()
    get_pc_name_test()
    get_mac_address_test()
    get_cuda_version_test()
    get_env_variables_test()
    make_cuda_invisible_test()
    profiler_test()
    get_tensorflow_version_test()
    main_wrapper_test()
    to_str_test()
    save_load_np_test()
    save_load_npz_test()
    save_load_pkl_test()
    get_uniform_dist_by_dim_test()
    get_normal_dist_by_dim_test()
    np_uniform_test()
    np_normal_test()
    generate_new_data_from_old_test()
    np_random_integers_test()
    augment_x_y_numpy_test()
    de_augment_numpy_test()
    nCk_test()
    redirect_std_test()
    get_line_number_test()
    get_function_name_test()
    get_file_name_test()
    get_base_file_name_test()
    get_function_name_and_line_test()
    get_base_file_and_function_name_test()
    add_color_test()
    logger_test()
    create_and_delete_dir_test()
    create_and_delete_dir_with_files_test()
    delete_file_test()
    delete_files_test()
    sleep_test()
    reverse_tuple_or_list_test()
    get_time_stamp_test()
    print('{}'.format('-' * 20))
    return
