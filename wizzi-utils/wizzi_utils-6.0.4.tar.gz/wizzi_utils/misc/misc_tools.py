import os
import datetime
from timeit import default_timer as timer
from typing import Callable
import cProfile
import pstats
import io
import numpy as np
import random
import inspect
import sys
import time
import pickle
from itertools import combinations
import shutil

LINES = '-' * 80
CONST_COLOR_MAP = {
    'ResetAll': "\033[0m",
    'Bold': "\033[1m",
    'Dim': "\033[2m",
    'Underlined ': "\033[4m",
    'Blink      ': "\033[5m",
    'Reverse    ': "\033[7m",
    'Hidden     ': "\033[8m",

    'ResetBold': "\033[21m",
    'ResetDim': "\033[22m",
    'ResetUnderlined': "\033[24m",
    'ResetBlink': "\033[25m",
    'ResetReverse': "\033[27m",
    'ResetHidden': "\033[28m",

    'Default': "\033[39m",
    'Black': "\033[97m",
    'Red': "\033[31m",
    'Green': "\033[32m",
    'Yellow': "\033[33m",
    'Blue': "\033[34m",
    'Magenta': "\033[35m",
    'Cyan': "\033[36m",
    'LightGray': "\033[37m",
    'DarkGray': "\033[90m",
    'LightRed': "\033[91m",
    'LightGreen': "\033[92m",
    'LightYellow': "\033[93m",
    'LightBlue': "\033[94m",
    'LightMagenta': "\033[95m",
    'LightCyan': "\033[96m",
    'White': "\033[30m",

    'BackgroundDefault': "\033[49m",
    'BackgroundBlack': "\033[107m",
    'BackgroundRed': "\033[41m",
    'BackgroundGreen': "\033[42m",
    'BackgroundYellow': "\033[43m",
    'BackgroundBlue': "\033[44m",
    'BackgroundMagenta': "\033[45m",
    'BackgroundCyan': "\033[46m",
    'BackgroundLightGray': "\033[47m",
    'BackgroundDarkGray': "\033[100m",
    'BackgroundLightRed': "\033[101m",
    'BackgroundLightGreen': "\033[102m",
    'BackgroundLightYellow': "\033[103m",
    'BackgroundLightBlue': "\033[104m",
    'BackgroundLightMagenta': "\033[105m",
    'BackgroundLightCyan': "\033[106m",
    'BackgroundWhite': "\033[40m"
}


def exception_error(e, tabs: int = 1):
    """
    Aux function - print exception error in red with function name
    :param e: error. e.g. <class 'ModuleNotFoundError'>
    :param tabs: error. e.g. <class 'ModuleNotFoundError'>
    :return:
    """
    error_str = '{}{}: {}'.format(tabs * '\t', get_function_name(depth=2), e)
    print(add_color(string=error_str, color='Red'))
    return


def chop_microseconds(delta: datetime.timedelta) -> datetime.timedelta:
    """
    Aux function - removes micro seconds from datetime.timedelta object
    e.g. 0:00:02.000001 -> 0:00:02
    :param delta:
    :return:
    """
    return delta - datetime.timedelta(microseconds=delta.microseconds)


def get_timer_delta(start_timer: float, with_ms: bool = False, ack: bool = False, tabs: int = 1) -> datetime.timedelta:
    """
    :param start_timer: begin time
    :param with_ms: if microseconds needed - set to true. else: no microseconds
    :param ack: print time passed
    :param tabs:
    :return:
    see timer_test()
    """
    end_timer = get_timer()
    d = datetime.timedelta(seconds=(end_timer - start_timer))
    if not with_ms:
        d = chop_microseconds(d)
    if ack:
        print('{}Time passed {}'.format(tabs * '\t', d))
    return d


def get_timer() -> float:
    """
    sets a timer beginning
    :return:
    see timer_test()
    """
    return timer()


def timer_action(seconds: int, action: str = '', tabs: int = 1) -> None:
    """
    :param seconds:
    :param action:
    :param tabs:
    :return:
    counts till seconds or block
    see timer_action_test()
    """
    if seconds is None:
        input('{}Press "Enter" key for {}...'.format(tabs * '\t', action))
    else:
        time_in_future = datetime.datetime.now() + datetime.timedelta(seconds=seconds)
        print('{}{} IN: {}'.format(tabs * '\t', action, seconds), end='', flush=True)
        while time_in_future > datetime.datetime.now():
            time.sleep(1)
            seconds -= 1
            print(' {}'.format(seconds), end='', flush=True)
        print('')
    return


def get_current_date_hour(format_s: str = '%d-%m-%Y %H:%M:%S', ack: bool = False, tabs: int = 1) -> str:
    """
    :param format_s: date time format
    :param ack: prints current time
    :param tabs:
    :return:
    see get_current_date_hour_test()
    """
    now = datetime.datetime.now()
    current_time = now.strftime(format_s)
    if ack:
        print('{}Current time is {}'.format(tabs * '\t', current_time))
    return current_time


def get_pc_name(ack: bool = False, tabs: int = 1) -> str:
    """
    :param ack:
    :param tabs:
    :return: pc name as str
    see get_pc_name_test()
    """
    try:
        import platform
        pc_name = platform.uname()[1]
        if ack:
            print('{}* Computer Name: {}'.format(tabs * '\t', pc_name))
    except ModuleNotFoundError as e:
        pc_name = ''
        exception_error(e)
    return pc_name


def get_mac_address(add_semi_colons: bool = True, ack: bool = False, tabs: int = 1) -> str:
    """
    :return: pc mac as str
    see get_mac_address_test()
    """
    try:
        from uuid import getnode as get_mac
        mac = get_mac()
        mac = "{:X}".format(mac)  # turn to Hex
        if add_semi_colons:
            mac = ':'.join(mac[i:i + 2] for i in range(0, 12, 2))
        if ack:
            print('{}* Computer Mac: {}'.format(tabs * '\t', mac))
    except ModuleNotFoundError as e:
        mac = ''
        exception_error(e)
    return mac


def get_cuda_version(ack: bool = False, tabs: int = 1) -> str:
    """
    :param ack:
    :param tabs:
    :return: cuda version if found on environment variables
    see get_cuda_version_test()
    """
    if 'CUDA_PATH' in os.environ:
        cuda_v = '* CUDA Version: {}'.format(os.path.basename(os.environ['CUDA_PATH']))
    else:
        cuda_v = '* No CUDA_PATH found'
    if ack:
        print('{}{}'.format(tabs * '\t', cuda_v))
    return cuda_v


def get_env_variables(ack: bool = False, tabs: int = 1) -> dict:
    """
    :param ack:
    :param tabs:
    :return: dict with envs
    prints env variables
    see get_env_variables_test()
    """
    env_d = dict(os.environ)
    if ack:
        print('{}Environment variables:'.format(tabs * '\t'))
        for k, v in env_d.items():
            print('{}\t{} = {}'.format(tabs * '\t', k, v))
    return env_d


def make_cuda_invisible() -> None:
    """
        disable gpu 0
        FUTURE - support disabling many GPUS
        os.environ['CUDA_VISIBLE_DEVICES'] = '0'  # GPU 0 available
        os.environ['CUDA_VISIBLE_DEVICES'] = '-1, 0'  # GPU 0 not available
        os.environ['CUDA_VISIBLE_DEVICES'] = '0, -1, 0'  # GPU 0 available but 1 disabled
        os.environ['CUDA_VISIBLE_DEVICES'] = '1, 2, -1, 0'  # GPU 1,2 available but 0 disabled

        read more: https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#env-vars
        see make_cuda_invisible_test()
    """
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1, 0'
    return


def start_profiler() -> cProfile.Profile:
    """
    starts profiling
    :return: profiling object that is needed for end_profiler()
    see profiler_test()
    """
    pr = cProfile.Profile()
    pr.enable()
    return pr


def end_profiler(pr: cProfile.Profile, rows: int = 10, ack: bool = False) -> str:
    """
    profiling output
    :param pr: object returned from start_profiler()
    :param rows: how many rows to print sorted by 'cumulative' run time
    :param ack:
    :return: profiler output as string
    see profiler_test()
    """
    pr.disable()
    s = io.StringIO()
    ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
    ps.print_stats(rows)
    profiler_str = s.getvalue()
    if ack:
        print('{}'.format(profiler_str))
    return profiler_str


def set_seed(seed: int = 42) -> None:
    """
    :param seed: setting numpy and random seeds
    :return:
    see main_wrapper_test() - uses set_seed
    """
    np.random.seed(seed)
    random.seed(seed)
    return


def get_tensorflow_version(ack: bool = False, tabs: int = 1) -> str:
    """
    :param ack:
    :param tabs:
    :return:
    see get_tensorflow_version_test()
    """
    try:
        import tensorflow as tf
        string = '* TensorFlow Version {}'.format(tf.__version__)
        if ack:
            print('{}{}'.format(tabs * '\t', string))
    except ModuleNotFoundError as e:
        string = '* {}'.format(e)
    return string


def main_wrapper(
        main_function: Callable,
        seed: int = -1,
        cuda_off: bool = False,
        torch_v: bool = False,
        tf_v: bool = False,
        cv2_v: bool = False,
        with_profiler: bool = False
) -> None:
    """
    :param main_function: the function to run
    :param seed: if -1 no seed, else set_seed(seed=seed)
    :param cuda_off: make gpu invisible and force run on cpu
    :param torch_v: print torch version
    :param tf_v: print tensorflow version
    :param cv2_v: print opencv version
    :param with_profiler: run profiler
    see main_wrapper_test()
    :return:
    """
    print(LINES)
    start_timer = get_timer()

    print('main_wrapper:')
    print('* Run started at {}'.format(get_current_date_hour()))
    print('* Python Version {}'.format(sys.version))
    print('* Working Dir: {}'.format(os.getcwd()))
    print('* Computer Name: {}'.format(get_pc_name()))
    print('* Computer Mac: {}'.format(get_mac_address()))
    cuda_msg = get_cuda_version()
    if cuda_off:
        make_cuda_invisible()
        cuda_msg += ' (Turned off)'
    print(cuda_msg)

    if torch_v:
        try:
            from wizzi_utils.torch.torch_tools import get_torch_version
            print(get_torch_version())
        except (ImportError, ModuleNotFoundError, NameError) as err:
            string = '* {}'.format(err)
            exception_error(string)
    if tf_v:
        try:
            print(get_tensorflow_version())
        except (ImportError, ModuleNotFoundError, NameError) as err:
            string = '* {}'.format(err)
            exception_error(string)
    if cv2_v:
        try:
            from wizzi_utils.open_cv.open_cv_tools import get_cv_version
            print(get_cv_version())
        except (ImportError, ModuleNotFoundError, NameError) as err:
            string = '* {}'.format(err)
            exception_error(string)

    if seed > -1:
        set_seed(seed=seed)
        print('* Seed was initialized to {}'.format(seed))

    print('Function {} started:'.format(main_function))
    print(LINES)
    pr = start_profiler() if with_profiler else None

    main_function()
    if with_profiler:
        print(end_profiler(pr))

    print(LINES)
    print('Total run time {}'.format(get_timer_delta(start_timer)))
    return


def add_data(var, data_chars: int, float_precision: int = 0) -> str:
    """
    Aux function for to_str()
    :param var:
    :param data_chars:
    :param float_precision:
    :return:
    """
    if isinstance(var, (float, int)):
        if isinstance(var, float) and float_precision > 0:
            data_str_raw = '{:,.' + str(float_precision) + 'f}'
            data_str_raw = data_str_raw.format(var)
        else:
            data_str_raw = '{:,}'.format(var)
    else:
        data_str_raw = str(var)
    data_str_raw = data_str_raw.replace('\n', '').replace('  ', '')
    if data_chars == 0:  # all data
        data_chars = len(data_str_raw) + 1
    elif data_chars < 0:  # no data
        data_chars = 0
    # else keep positive chars

    data_str = ': {}'.format(data_str_raw[:data_chars])
    if len(data_str_raw) > data_chars > 0:
        data_str += ' ...too long'
    return data_str


def to_str(var,
           title: str = 'var',
           data_chars: int = 100,
           float_precision: int = 2,
           recursive: bool = False
           ) -> str:
    """
    :param var: the variable
    :param title: the title (usually variable name)
    :param data_chars: how many char to print.
        -1: none
         0: all
        +0: maximum 'data_chars' (e.g. data_chars=50 and |str(var)|=100 - first 50 chars)
    :param float_precision: round number if possible(float, np array...). 0 for no rounding
    :param recursive: to keep printing if there are more items inside e.g. np.array(shape=(2,3,4)) -> 3 prints
    :return: informative string of the variable
    see to_str_test()
    """
    type_s = str(type(var)).replace('<class \'', '').replace('\'>', '')  # clean type name
    string = '{}({}'.format(title, type_s)  # base: title and type

    if isinstance(var, (int, float, str)):
        if hasattr(var, "__len__"):
            string += ',len={})'.format(var.__len__())
        else:
            string += ')'
        string += add_data(var, data_chars, float_precision)

    elif isinstance(var, (list, tuple)):
        string += ',len={})'.format(var.__len__())
        string += add_data(var, data_chars)
        if recursive and len(var) > 0:  # recursive call
            string += '\n\t{}'.format(
                to_str(var=var[0], title='{}[0]'.format(title), data_chars=data_chars, float_precision=float_precision,
                       recursive=recursive))

    elif isinstance(var, np.ndarray):
        string += ',shape={},dtype={})'.format(var.shape, var.dtype)
        if var.dtype == np.float64 and float_precision > 0:
            string += add_data(np.round(var, float_precision).tolist(), data_chars, float_precision=0)
        else:
            string += add_data(var.tolist(), data_chars, float_precision=0)
        if recursive and len(var) > 0:  # recursive call
            string += '\n\t{}'.format(
                to_str(var=var[0], title='{}[0]'.format(title), data_chars=data_chars, float_precision=float_precision,
                       recursive=recursive))

    elif isinstance(var, dict):
        string += ',len={},keys={})'.format(var.__len__(), list(var.keys()))
        string += add_data(var, data_chars)
        if recursive and len(var) > 0:  # recursive call
            first_key = next(iter(var))
            string += '\n\t{}'.format(
                to_str(var=var[first_key], title='{}[{}]'.format(title, first_key), data_chars=data_chars,
                       float_precision=float_precision, recursive=recursive))

    else:  # all unidentified elements get default print (title(type): data)
        string += ')'
        string += add_data(var, data_chars)
    return string


def save_np(t: np.array, path: str, ack: bool = True, tabs: int = 1) -> None:
    """
    :param t: numpy array
    :param path: suffix '.npy' added automatically if not exists
    :param ack:
    :param tabs:
    :return:
    see save_load_np_test()
    """
    np.save(path, t)
    if ack:
        print('{}Saved: {}'.format(tabs * '\t', path))
    return


def load_np(path: str, ack: bool = True, tabs: int = 1) -> np.array:
    """
    :param path:
    :param ack:
    :param tabs:
    :return: numpy array
    see save_load_np_test()
    """
    t = np.load(path)
    if ack:
        print('{}Loaded: {}'.format(tabs * '\t', path))
    return t


def save_npz(arrays_dict: dict, path: str, ack: bool = True, tabs: int = 1) -> None:
    """
    :param arrays_dict: e.g. { 'a': np.ones(3) }
    :param path:
    :param ack:
    :param tabs:
    :return:
    save a dict of numpy arrays
    see save_load_npz_test()
    """
    np.savez(path, **{n: a for n, a in arrays_dict.items()})
    if ack:
        print('{}Saved: {}. Keys={}'.format(tabs * '\t', path, arrays_dict.keys()))
    return


def load_npz(path: str, ack: bool = True, tabs: int = 1) -> dict:
    """
    :param path:
    :param ack:
    :param tabs:
    :return: numpy array
    see save_load_npz_test()
    """
    arrays_obj = np.load(path)
    arrays_dict = {}
    for k in arrays_obj.files:
        arrays_dict[k] = arrays_obj[k]
    if ack:
        print('{}Loaded: {}. Keys={}'.format(tabs * '\t', path, arrays_dict.keys()))
    return arrays_dict


def save_pkl(data_dict: dict, path: str, ack: bool = True, tabs: int = 1) -> None:
    """
    :param data_dict:
    :param path:
    :param ack:
    :param tabs:
    :return:
    see save_load_pkl_test()
    """
    file_obj = open(path, "wb")
    pickle.dump(data_dict, file_obj)
    file_obj.close()
    if ack:
        print('{}Saved: {}'.format(tabs * '\t', path))
    return


def load_pkl(path: str, ack: bool = True, tabs: int = 1) -> dict:
    """
    :param path:
    :param ack:
    :param tabs:
    :return:
    see save_load_pkl_test()
    """
    file_obj = open(path, "rb")
    data_dict = pickle.load(file_obj)
    file_obj.close()
    if ack:
        print('{}Loaded: {}'.format(tabs * '\t', path))
    return data_dict


def get_uniform_dist_by_dim(A: [np.array, list]) -> (np.array, np.array):
    """
    :param A:
    :return:
    for every dimension gets the lowest and highest
    see get_uniform_dist_by_dim_test()
    """
    lows = np.min(A, axis=0)
    highs = np.max(A, axis=0)
    return lows, highs


def get_normal_dist_by_dim(A: [np.array, list]) -> (np.array, np.array):
    """
    :param A:
    :return:
    see get_normal_dist_by_dim_test()
    """
    means = np.mean(A, axis=0)
    stds = np.std(A, axis=0)
    return means, stds


def np_uniform(shape: tuple, lows: [list, int], highs: [list, int]) -> np.array:
    """
    :param shape:
    :param lows:
    :param highs:
    :return:
    see np_uniform_test()
    """
    ret = np.random.uniform(low=lows, high=highs, size=shape)
    return ret


def np_normal(shape: tuple, mius: [list, int, float], stds: [list, int, float]) -> np.array:
    """
    :param shape:
    :param mius:
    :param stds:
    :return:
    see np_normal_test()
    """
    ret = np.random.normal(loc=mius, scale=stds, size=shape)
    return ret


def generate_new_data_from_old(old_data: np.array, new_data_n: int, dist: str = 'normal'):
    """
    :param old_data:
    :param new_data_n:
    :param dist:
    :return:
    see generate_new_data_from_old_test()
    """
    d = old_data.shape[1]
    if dist == 'uniform':
        lows, highs = get_uniform_dist_by_dim(old_data)
        new_data = np_uniform(shape=(new_data_n, d), lows=lows, highs=highs)
    else:  # else normal
        means, stds = get_normal_dist_by_dim(old_data)
        new_data = np_normal(shape=(new_data_n, d), mius=means, stds=stds)
    return new_data


def np_random_integers(low: int, high: int, size: tuple) -> np.array:
    """
    :param low:
    :param high:
    :param size:
    :return:
    see np_random_integers_test()
    """
    ret = np.random.random_integers(low=low, high=high, size=size)
    return ret


def augment_x_y_numpy(X: np.array, y: np.array) -> np.array:
    """
    :param X:
    :param y:
    :return:
    see augment_x_y_numpy_test()
    """
    assert X.shape[0] == y.shape[0], 'row count must be the same'
    if len(X.shape) == 1:  # change x size()=[n,] to size()=[n,1]
        X = X.reshape(X.shape[0], 1)
    if len(y.shape) == 1:  # change y size()=[n,] to size()=[n,1]
        y = y.reshape(y.shape[0], 1)
    A = np.column_stack((X, y))
    return A


def de_augment_numpy(A: np.array) -> (np.array, np.array):
    """
    :param A:
    :return:
    see de_augment_numpy_test()
    """
    if len(A.shape) == 1:  # A is 1 point. change from size (n) to size (1,n)
        A = A.reshape(1, A.shape[0])
    X, y = A[:, :-1], A[:, -1]
    if len(X.shape) == 1:  # change x size()=[n,] to size()=[n,1]
        X = X.reshape(X.shape[0], 1)
    if len(y.shape) == 1:  # change y size()=[n,] to size()=[n,1]
        y = y.reshape(y.shape[0], 1)
    return X, y


def nCk(n: int, k: int, as_int: bool = False):
    """
    :param n:
    :param k:
    :param as_int:
    :return: if as_int True: the result of nCk, else the combinations of nCk
    n choose k
    see nCk_test()
    """
    range_list = np.arange(0, n, 1)
    combs = list(combinations(range_list, k))
    combs = [list(comb) for comb in combs]
    if as_int:
        combs = len(combs)
    return combs


def redirect_std_start() -> (io.TextIOWrapper, io.StringIO):
    """
    redirect all prints to summary_str
    :return:
        io.TextIOWrapper - to revert back the prints to sys.stdout
        io.StringIO - to extract output
    see redirect_std_test()
    """
    old_stdout = sys.stdout
    sys.stdout = summary_str = io.StringIO()
    return old_stdout, summary_str


def redirect_std_finish(old_stdout: io.TextIOWrapper, summary_str: io.StringIO) -> str:
    """
    :param old_stdout: to revert back the prints to sys.stdout
    :param summary_str: to extract output
    :return:
    redirect all prints back to std out and return a string of what was captured"
    see redirect_std_test()
    """
    sys.stdout = old_stdout
    return summary_str.getvalue()


def get_line_number(depth: int = 1, ack: bool = False, tabs: int = 1) -> str:
    """
    :param depth:
    :param ack:
    :param tabs:
    :return:
    see get_line_number_test()
    """
    ret_val = ''
    try:
        scope_1_back = inspect.stack()[depth]  # stack()[0] is this function
        ret_val = '{}'.format(scope_1_back.lineno)
        if ack:
            print('{}Line {}:'.format(tabs * '\t', ret_val))
    except IndexError as e:
        exception_error(e)
    return ret_val


def get_function_name(depth: int = 1, ack: bool = False, tabs: int = 1) -> str:
    """
    :param depth:
    :param ack:
    :param tabs:
    :return:
    see
    """
    ret_val = ''
    try:
        scope_1_back = inspect.stack()[depth]  # stack()[0] is this function
        ret_val = '{}'.format(scope_1_back.function)
        if ack:
            print('{}{}:'.format(tabs * '\t', ret_val))
    except IndexError as e:
        exception_error(e)
    return ret_val


def get_file_name(depth: int = 1, ack: bool = False, tabs: int = 1) -> str:
    """
    :param depth:
    :param ack:
    :param tabs:
    :return:
    see get_file_name_test()
    """
    ret_val = ''
    try:
        scope_1_back = inspect.stack()[depth]  # stack()[0] is this function
        ret_val = '{}'.format(scope_1_back.filename)
        if ack:
            print('{}{}:'.format(tabs * '\t', ret_val))
    except IndexError as e:
        exception_error(e)
    return ret_val


def get_base_file_name(depth: int = 1, ack: bool = False, tabs: int = 1) -> str:
    """
    :param depth:
    :param ack:
    :param tabs:
    :return:
    see get_base_file_name_test()
    """
    # +1 because of this function
    file_name = get_file_name(depth + 1)
    base_name = os.path.basename(file_name)
    if ack:
        print('{}{}:'.format(tabs * '\t', base_name))
    return base_name


def get_function_name_and_line(depth: int = 1, ack: bool = False, tabs: int = 1) -> str:
    """
    :param depth:
    :param ack:
    :param tabs:
    :return:
    see get_function_name_and_line_test()
    """
    # +1 because of this function
    ret_val = '{}::{}'.format(get_file_name(depth + 1), get_line_number(depth + 1))
    if ack:
        print('{}{}:'.format(tabs * '\t', ret_val))
    return ret_val


def get_base_file_and_function_name(depth: int = 1, ack: bool = False, tabs: int = 1) -> str:
    """
    :param depth:
    :param ack:
    :param tabs:
    :return:
    see get_base_file_and_function_name_test()
    """
    # +1 because of this function
    ret_val = '{}::{}'.format(get_base_file_name(depth + 1), get_line_number(depth + 1))
    if ack:
        print('{}{}:'.format(tabs * '\t', ret_val))
    return ret_val


def add_color(string: str, color: str = 'Red') -> str:
    """
    :param string:
    :param color: from color map
    # todo add option for combination (like bold, underlined ...)
    # todo change to lower case
    # todo color numbers maybe wrong
    to see all colors and options:
        for k, v in CONST_COLOR_MAP.items():
            print('{}{}{}'.format(v, k, CONST_COLOR_MAP['ResetAll']))
    see add_color_test()
    """

    if color in CONST_COLOR_MAP:
        # concat (color, string, reset tag)
        string = '{}{}{}'.format(CONST_COLOR_MAP[color], string, CONST_COLOR_MAP['ResetAll'])
    return string


def init_logger(logger_path: str = './log.txt') -> io.TextIOWrapper:
    """
    :param: logger_path
    :return: logger obj
    see logger_test()
    """
    global logger
    logger = open(file=logger_path, mode='w', encoding='utf-8')
    return logger


def flush_logger() -> None:
    """
    good for loops - writes every iteration if used
    see logger_test()
    """
    global logger
    if logger is not None:
        logger.flush()
    return


def log_print(line: str, tabs: int = 0) -> None:
    """
    :param line:
    :param tabs:
    :return:
    see logger_test()
    """
    global logger
    print('{}{}'.format(tabs * '\t', line))
    if logger is not None:
        logger.write('{}{}\n'.format(tabs * '\t', line))
    return


def log_print_dict(my_dict, tabs: int = 1) -> None:
    """
    :param my_dict:
    :param tabs:
    :return:
    see logger_test()
    """
    for k, v in my_dict.items():
        log_print('{}{}: {}'.format(tabs * '\t', k, v))
    return


def close_logger() -> None:
    """
    :return:
    see logger_test()
    """
    global logger
    if logger is not None:
        logger.close()
    return


def create_dir(dir_path: str, ack: bool = True, tabs: int = 1):
    """
    :param dir_path:
    :param ack:
    :param tabs:
    :return:
    see create_and_delete_dir_test()
    """
    status = 'exists'
    if not os.path.exists(dir_path):
        try:
            os.mkdir(dir_path)
            status = 'created'
        except OSError as e:
            exception_error(e)
    if ack:
        print('{}{} {}'.format(tabs * '\t', dir_path, status))
    return


def delete_dir(dir_path: str, ack: bool = True, tabs: int = 1):
    """
    :param dir_path:
    :param ack:
    :param tabs:
    :return:
    see create_and_delete_dir_test()
    """
    status = 'doesn\'t exist'
    if os.path.exists(dir_path):
        files_n = len(os.listdir(dir_path))
        if files_n > 0:
            status = 'HAS {} FILES - use delete_dir_with_files()'.format(files_n)
        else:
            try:
                os.rmdir(dir_path)
                status = 'deleted'
            except OSError as e:
                exception_error(e)
    if ack:
        print('{}{} {}'.format(tabs * '\t', dir_path, status))
    return


def delete_dir_with_files(dir_path: str, ack: bool = True, tabs: int = 1):
    """
    :param dir_path:
    :param ack:
    :param tabs:
    :return:
    see create_and_delete_dir_test()
    """
    status = 'doesn\'t exist'
    if os.path.exists(dir_path):
        files = os.listdir(dir_path)
        try:
            shutil.rmtree(dir_path)
            status = 'deleted(with {} files - {})'.format(len(files), files)
        except OSError as e:
            exception_error(e)
    if ack:
        print('{}{} {}'.format(tabs * '\t', dir_path, status))
    return


def delete_file(file: str, ack: bool = True, tabs: int = 1) -> None:
    """
    :param file:
    :param ack:
    :param tabs:
    see delete_file_test()
    """
    os.remove(file)
    if ack:
        print('{}Removed: {} '.format(tabs * '\t', file))
    return


def delete_files(files: list, ack: bool = True, tabs: int = 1) -> None:
    """
    :param files:
    :param ack:
    :param tabs:
    :return:
    see delete_files_test()
    """
    for file in files:
        delete_file(file, ack=False)
    if ack:
        print('{}Removed: {} '.format(tabs * '\t', files))
    return


def sleep(seconds: int, ack: bool = False, tabs: int = 1):
    """
    :param seconds:
    :param ack:
    :param tabs:
    :return:
    see sleep_test()
    """
    if ack:
        print('{}Sleeping {} seconds'.format(tabs * '\t', seconds))
    time.sleep(seconds)
    return


def reverse_tuple_or_list(orig: [tuple, list]) -> [tuple, list]:
    """
    :param orig: list or tuple
    :return: dst: reversed list or tuple
    see reverse_tuple_or_list_test()
    """
    dst = orig[::-1]
    return dst


def get_time_stamp(format_s: str = '%Y_%m_%d_%H_%M_%S') -> str:
    """
    :param format_s:
    examples:
    "%Y_%m_%d_%H_%M_%S_%f" >>> 2020_07_19_13_36_24_597247
    "%Y_%m_%d" >>> 2021_04_07
    :return:
    see get_time_stamp_test()
    """
    date_time_obj = datetime.datetime.now()
    timestamp_str = date_time_obj.strftime(format_s)
    return timestamp_str
