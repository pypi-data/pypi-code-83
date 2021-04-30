import torch
import numpy as np
# import torchvision
from wizzi_utils import misc_tools as mt  # misc tools


def cuda_on() -> bool:
    """
     check if cuda available
     see cuda_on_test()
     """
    return torch.cuda.is_available()


def set_cuda_scope_and_seed(seed: int, dtype='FloatTensor', tabs: int = 1) -> None:
    """
    :param seed: setting torch seed and default torch if cuda on
    :param dtype:
        https://pytorch.org/docs/stable/tensors.html
        32-bit floating point: torch.cuda.FloatTensor
        64-bit floating point: torch.cuda.DoubleTensor
    :param tabs:
    see set_cuda_scope_and_seed_test()
    """
    mt.set_seed(seed)
    if cuda_on():
        def_dtype = 'torch.cuda.{}'.format(dtype)
        torch.set_default_tensor_type(def_dtype)
        torch.cuda.manual_seed(seed)
        print('{}working on CUDA. default dtype = {} <=> {}'.format(tabs * '\t', def_dtype, torch.get_default_dtype()))
    else:
        torch.manual_seed(seed)
        print('{}working on CPU'.format(tabs * '\t'))
    return


def add_cuda(var: torch.Tensor) -> torch.Tensor:
    """
    assigns the variables to GPU if available
    see add_cuda_test()
    """
    if cuda_on() and not is_cuda(var):
        var = var.cuda()
    return var


def is_trainable(var: torch.Tensor) -> bool:
    """
    :param var:
    :return: if the variable is trainable
    see is_trainable_test()
    """
    return var.requires_grad


def set_trainable(var: torch.Tensor, trainable: bool = True) -> None:
    """
    :param var:
    :param trainable: True\False
    sets the var to 'trainable'
    """
    var.requires_grad = trainable
    return


def is_cuda(var: torch.Tensor) -> bool:
    """
    :param var:
    :return: if the variable is Cuda\CPU variable
    see is_cuda_test()
    """
    return var.is_cuda


def size_s(var: torch.Tensor) -> str:
    """
    :param var:
    :return: clean str of tensor size
    e.g. torch.Size([1, 3, 29]) -> [1, 3, 29]
    see size_s_test()
    """
    size_str = str(var.size())
    size_str = size_str[size_str.find("(") + 1:size_str.find(")")]
    return size_str


def total_size(t: torch.Tensor, ignore_first=True) -> int:
    """
    :param t:
    :param ignore_first: if the first dim is the rows and you want each row size
    calculates the total size of a tensor.
    see total_size_test()
    """
    total = 1
    my_shape = t.shape[1:] if ignore_first else t.shape
    for d in my_shape:
        total *= d
    return total


def torch_to_numpy(var_torch: torch.Tensor) -> np.array:
    """
    :param var_torch:
    :return: np array of var_torch
    convert torch to numpy
    see torch_to_numpy_test()
    """
    if is_trainable(var_torch):
        var_np = var_torch.detach().cpu().numpy()
    else:
        var_np = var_torch.cpu().numpy()
    return var_np


def numpy_to_torch(var_np: np.array, to_double=True, detach: bool = False) -> torch.Tensor:
    """
    :param var_np:
    :param to_double: create torch double - else float
    :param detach: if needed to be detached - don't remember when detached needed to be true happened
    convert numpy to torch also add to cude if cuda is on
    see numpy_to_torch_test()
    """
    if detach:
        if to_double:
            var_torch = add_cuda(torch.from_numpy(var_np).double()).detach()
        else:
            var_torch = add_cuda(torch.from_numpy(var_np).float()).detach()
    else:
        if to_double:
            var_torch = add_cuda(torch.from_numpy(var_np).double())
        else:
            var_torch = add_cuda(torch.from_numpy(var_np).float())
    return var_torch


def to_str(var, title: str, data_chars: int = 100, float_precision: int = 2, recursive: bool = False) -> str:
    """
    :param var: the variable
    :param title: the title (usually variable name)
    :param data_chars: how many char to print.
        -1: none
         0: all
        +0: maximum 'data_chars' (e.g. data_chars=50 and |str(var)|=100 - first 50 chars)
    :param data_chars: how many char to print.
    :param float_precision: round number if possible(float, np array...). 0 for no rounding
    :param recursive: to keep printing if there are more items inside e.g. torch.ones(shape=(2,3,4)) -> 3 prints
    :return: informative string of the variable
    see to_str_test()
    """

    if isinstance(var, torch.Tensor):
        type_s = str(type(var)).replace('<class \'', '').replace('\'>', '')  # clean type name
        string = '{}({},shape={},dtype={},trainable:{},is_cuda:{})'
        string = string.format(title, type_s, size_s(var), var.dtype, is_trainable(var), is_cuda(var))
        if float_precision > 0:
            string += mt.add_data(np.round(var.tolist(), float_precision).tolist(), data_chars, float_precision=0)
        else:
            string += mt.add_data(var.tolist(), data_chars, float_precision=0)
        if recursive and len(var.size()) > 0:  # recursive call
            string += '\n\t{}'.format(
                to_str(var=var[0], title='{}[0]'.format(title), data_chars=data_chars, float_precision=float_precision,
                       recursive=recursive))
    else:  # if it's not Tensor - use the default to_str() from misc_tools
        string = mt.to_str(var, title=title, data_chars=data_chars, float_precision=float_precision,
                           recursive=recursive)
    return string


def save_tensor(t, path: str, ack_print: bool = True, tabs: int = 1):
    """
    :param t: dict or a tensor
    :param path:
    :param ack_print:
    :param tabs:

    see save_load_tensor_test()
    """
    torch.save(t, path)
    if ack_print:
        print('{}{} Saved'.format(tabs * '\t', path))
    return


def load_tensor(path: str, ack_print: bool = True, tabs: int = 1):
    """
    :param path:
    :param ack_print:
    :param tabs:
    :return: t: dict or a tensor
    see save_load_tensor_test()
    """
    dst_allocation = None if cuda_on() else 'cpu'
    t = torch.load(path, map_location=dst_allocation)
    if ack_print:
        print('{}{} Loaded'.format(tabs * '\t', path))
    return t


def torch_uniform(shape: tuple, range_low: float, range_high: float) -> torch.Tensor:
    """
    :param shape:
    :param range_low:
    :param range_high:
    :return:
    see torch_uniform_test()
    """
    ret = torch.empty(shape).uniform_(range_low, range_high)
    return ret


def torch_normal(shape: tuple, miu: float, std: float) -> torch.Tensor:
    """
    :param shape:
    :param miu:
    :param std:
    :return:
    see torch_normal_test()
    """
    ret = torch.empty(shape).normal_(miu, std)
    return ret


def opt_to_str(optimizer: torch.optim) -> str:
    """
    :param optimizer:
    :return:
    see opt_to_str_test()
    """
    opt_s = str(optimizer).replace('\n', '').replace('    ', ' ')
    return opt_s


def get_lr(optimizer: [torch.optim, int]) -> float:
    """
    :param optimizer:
    :return:
    see get_lr_test()
    """
    lr = None
    if isinstance(optimizer, torch.Tensor):
        if "lr" in optimizer.param_groups[0]:
            lr = optimizer.param_groups[0]['lr']
    elif isinstance(optimizer, OptimizerHandler):
        lr = optimizer.lr()
    return lr


def set_lr(optimizer: torch.optim, new_lr: float) -> None:
    """
    :param optimizer:
    :param new_lr:
    :return:
    see set_lr_test()
    """
    optimizer.param_groups[0]['lr'] = new_lr
    return


def get_opt_by_name(opt_d: dict, params: list) -> torch.optim:
    """
    :param params: trainable params
    :param opt_d: has keys: name, lr, weight_decay and optional if SGD momentum
        e.g. options: {'name'= 'ADAM', 'lr': 0.001, 'weight_decay': 0}
    :return: optimizer
    see get_opt_by_name_test()
    """
    opt = None
    if opt_d['name'] == 'ADAM':
        opt = torch.optim.Adam(params, lr=opt_d['lr'], weight_decay=opt_d['weight_decay'])
    elif opt_d['name'] == 'SGD':
        opt = torch.optim.SGD(params, lr=opt_d['lr'], momentum=opt_d['momentum'], weight_decay=opt_d['weight_decay'])
    return opt


class OptimizerHandler:
    """
    Optimizer wrapper.
    if update_lr() called 'patience' times:
        new_lr = max(factor * lr, min_lr)
        set_lr(opt, new_lr)
    see OptimizerHandler_test()
    """

    def __init__(self, optimizer: torch.optim, factor: float, patience: int, min_lr: float):
        """
        :param optimizer: class torch.optim: e.g. Adam, SGD ...
        :param factor: percent to keep from old lr. if factor 0.1 and lr was 5: new lr = 0.5
        :param patience: how long to wait before changing lr
        :param min_lr: minimal lr
        """
        self.optimizer = optimizer
        self.factor = factor
        self.patience = patience
        self.min_lr = min_lr
        self.epochs_passed = 0

    def step(self):
        self.optimizer.step()
        return

    def lr(self):
        return self.optimizer.param_groups[0]['lr']

    def set_lr(self, new_lr: float):
        self.optimizer.param_groups[0]['lr'] = new_lr
        return

    def zero_grad(self):
        self.optimizer.zero_grad()
        return

    def update_lr(self):
        self.epochs_passed += 1
        if self.epochs_passed >= self.patience:
            self.epochs_passed = 0
            old_lr = self.lr()
            new_lr = max(old_lr * self.factor, self.min_lr)
            self.set_lr(new_lr)
            # print('new lr changed to {}'.format(self.lr()))
        return


class EarlyStopping:
    """
    counts how many rounds no improvment in loss
    if that passed patience - return true in should_early_stop()
    see EarlyStopping_test()
    """

    def __init__(self, patience: int):
        """
        :param patience:
        """
        self.patience = patience
        self.counter = 0
        self.best = None
        return

    def should_early_stop(self, loss: float):
        """
        :param loss:
        :return:
        """
        should_stop = False
        if self.best is None:
            self.best = loss
        elif loss < self.best:
            self.best = loss
            self.counter = 0
        else:
            self.counter += 1
            # print('\t\tpatience {}/{}'.format(self.counter, self.patience))
            if self.counter >= self.patience:
                should_stop = True
        return should_stop


def subset_init(c_size: int, A: torch.Tensor, trainable: bool = True) -> torch.Tensor:
    """
    :param c_size:
    :param A:
    :param trainable:
    :return:
    given c_size <= |A|, initialize a tensor C with a random subset of A
    see subset_init_test()
    """
    n = A.shape[0]
    if c_size >= n:
        if A.dtype == 'torch.float64':
            C = A.clone().double()
        elif A.dtype == 'torch.float32':
            C = A.clone().float()
        else:
            C = A.clone()
    else:
        perm = np.random.permutation(n)
        idx = perm[:c_size]
        if A.dtype == 'torch.float64':
            C = A[idx].clone().double()
        elif A.dtype == 'torch.float32':
            C = A[idx].clone().float()
        else:
            C = A[idx].clone()

    set_trainable(C, trainable)
    return C


def augment_x_y_torch(X: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """
    :param X:
    :param y:
    :return:
    creates A=X|y
    see augment_x_y_torch_test()
    """
    assert X.shape[0] == y.shape[0], 'row count must be the same'
    if len(X.shape) == 1:  # change x size()=[n,] to size()=[n,1]
        X = X.view(X.shape[0], 1)
    if len(y.shape) == 1:  # change y size()=[n,] to size()=[n,1]
        y = y.view(y.shape[0], 1)
    A = torch.cat((X, y), 1)
    return A


def de_augment_torch(A: torch.Tensor) -> (torch.Tensor, torch.Tensor):
    """
    :param A:
    :return:
    creates X|y=A
    see de_augment_torch_test()
    """
    assert 0 < len(A.shape) <= 2, 'supports 2d only'
    if len(A.shape) == 1:  # A is 1 point. change from size (n) to size (1,n)
        A = A.view(1, A.shape[0])
    X, y = A[:, :-1], A[:, -1]
    if len(X.shape) == 1:  # change x size()=[n,] to size()=[n,1]
        X = X.view(X.shape[0], 1)
    if len(y.shape) == 1:  # change y size()=[n,] to size()=[n,1]
        y = y.view(y.shape[0], 1)
    return X, y


def split_tensor(Q: torch.Tensor, p: float = 0.9) -> (torch.Tensor, torch.Tensor):
    """
    :param Q:
    :param p:
    :return:
    see split_tensor_test()
    """
    partition = int(p * Q.shape[0])
    Q_1 = Q[:partition]
    Q_2 = Q[partition:]
    return Q_1, Q_2


def shuffle_tensor(arr: torch.Tensor) -> torch.Tensor:
    """
    :param arr:
    :return:
    shuffles an array
    see shuffle_tensor_test()
    """
    if isinstance(arr, torch.Tensor):
        arr = arr[torch.randperm(arr.shape[0])]
    return arr


def count_keys(y: [torch.Tensor, np.array, list], tabs: int = 1) -> None:
    """
    :param y: nx1 array (torch, list, numpy)
    :param tabs:
    see count_keys_test()
    """
    from collections import Counter
    if hasattr(y, "shape"):
        y_shape = y.shape
    else:
        y_shape = len(y)
    print('{}Count classes: (y shape {})'.format(tabs * '\t', y_shape))
    cnt = Counter()
    for value in y:
        ind = value.item() if isinstance(y, torch.Tensor) else value
        cnt[ind] += 1
    cnt = sorted(cnt.items())
    for item in cnt:
        print('{}\tClass {}: {} samples'.format(tabs * '\t', item[0], item[1]))
    return


def get_torch_version() -> str:
    """
    :return:
    see get_torch_version_test()
    """
    string = '* PyTorch Version {}'.format(torch.__version__)
    return string

# def data_set_size_to_str(ds: torchvision.datasets) -> str:
#     ds_len = len(ds)
#
#     x = ds.data[0]  # load 1st sample as data loader will load
#     X_size_post_tr = (ds_len,)
#     for d in x.shape:
#         X_size_post_tr += (d,)
#
#     y_size = (len(ds.targets),)  # real data
#     res = '|X|={}, |y|={}'.format(X_size_post_tr, y_size)
#     return res
#
#
# import torch.nn as nn
#
#
# def model_params_print(model: nn.Module, print_values: bool = False, max_samples: int = 2):
#     """
#     :param model: nn model with self.title member
#     :param print_values: print vars values as a list
#     :param max_samples: if print_values: prints first 'max_samples' as a list
#     :return:
#     """
#     print('{}:'.format(model.title))
#     msg = '\t{:15s}: {:10s} ({:7} params), trainable:{}, is_cuda:{}'
#     sum_params = 0
#     for name, param in model.named_parameters():
#         layer_params = 1
#         for d in param.shape:
#             layer_params *= d
#         sum_params += layer_params
#         print(msg.format(name, size_s(param), layer_params, is_trainable(param), is_cuda(param)))
#         if print_values:
#             print('\t\tvalues: {}'.format(param[min(max_samples, param.shape[0])].tolist()))
#     print('\tTotal {:,.0f} params'.format(sum_params))
#     return
#
#
# def model_summary_to_string(model: nn.Module, input_size: tuple, batch_size: int) -> str:
#     """
#         get model info to string
#         e.g.
#             m = MnistModel()
#             print(utils.model_summary_to_string(m, (1, 28, 28), 64))
#     """
#     from torchsummary import summary
#     a, b = redirect_std_start()
#     summary(model, input_size, batch_size)
#     return redirect_std_finish(a, b)
#
#
# def model_params_count(model: nn.Module) -> int:
#     total_parameters = 0
#     for p in list(model.parameters()):
#         total_parameters += tensor_total_size(p, False)
#     return total_parameters
#
#
# def save_model(model: nn.Module, ack_print: bool = True, tabs: int = 0):
#     """ nn model with self.title and self.path members """
#     torch.save(model.state_dict(), model.path)
#     if ack_print:
#         print('{}{} Saved {}'.format(tabs * '\t', model.title, model.path))
#     return
#
#
# def load_model(model: nn.Module, ack_print: bool = True, tabs: int = 0):
#     """ nn model with self.title and self.path members """
#     dst_allocation = None if cuda_on() else 'cpu'
#     model.load_state_dict(torch.load(model.path, map_location=dst_allocation))
#     model.eval()
#     if ack_print:
#         print('{}{} loaded from {}'.format(tabs * '\t', model.title, model.path))
#     return
#
#
# def set_model_status(model: nn.Module, status: bool, status_print: bool = False):
#     """ set model parameters trainable status to 'status' """
#     for param in model.parameters():
#         param.requires_grad_(status)
#     if status_print:
#         print(model_status_str(model))
#     return
#
#
# def model_status_str(model: nn.Module) -> str:
#     """
#     3 options: model fully trainable, fully frozen, both
#     model has self.title
#     """
#     saw_trainable, saw_frozen = 0, 0
#     for param in model.parameters():
#         if is_trainable(param):
#             saw_trainable = 1
#         else:
#             saw_frozen = 1
#     ans = saw_trainable + saw_frozen
#     if ans == 2:
#         msg = '{} is part trainable and part frozen'.format(model.title)
#     elif saw_trainable == 1:
#         msg = '{} is fully trainable'.format(model.title)
#     else:
#         msg = '{} is fully frozen'.format(model.title)
#     return msg
#
#
# def copy_models(model_source: nn.Module, model_target: nn.Module, dont_copy_layers: list, ack: bool = False):
#     """
#     :param model_source: copy from
#     :param model_target: copy to
#     :param dont_copy_layers: list of exact names as appear in model.named_parameters()[0]
#            make sure before coping that dst and target tensors are in the same size
#     :param ack: prints copy\not
#     :return:
#     """
#     print('Copying model {} to model {} except {}:'.format(model_source.title, model_target.title, dont_copy_layers))
#     for name, param in model_source.named_parameters():
#         if name in dont_copy_layers:
#             if ack:
#                 print('\tNOT copied Layer {}'.format(name))
#         else:
#             if ack:
#                 print('\tCopied Layer {}'.format(name))
#             model_target.state_dict()[name].copy_(param)
#             # print('\t\tvalues orig   : {}'.format(param.tolist()))
#             # print('\t\tvalues coreset: {}'.format(model_coreset.state_dict()[name].tolist()))
#             # print('\t\tvalues coreset: {}'.format(model_coreset.state_dict()[name].tolist()))
#     return
#
#
# def freeze_layers(model: nn.Module, trainable_layers: list):
#     """
#     trainable_layers: list of exact names as appear in model.named_parameters()[0]
#     all params that are in trainable_layers -> trainable = True
#     else -> trainable = False
#     """
#     print('Model {}: freezing all except {}:'.format(model.title, trainable_layers))
#     for name, param in model.named_parameters():
#         if name in trainable_layers:
#             param.requires_grad_(True)
#             # print('alive {}'.format(name))
#         else:
#             param.requires_grad_(False)
#             # print('frozen {}'.format(name))
#     return
#
#
# def clone_model(model: nn.Module):
#     import copy
#     model_clone = copy.deepcopy(model)
#     return model_clone
#
#
# def shuffle_ds(ds: torchvision.datasets):
#     """
#     by ref
#     :param ds:
#     :return:
#     """
#     n = ds.targets.shape[0]
#     perm = torch.randperm(n)
#     ds.targets = ds.targets[perm]
#     ds.data = ds.data[perm]
#     return
