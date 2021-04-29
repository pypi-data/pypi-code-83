from typing import Any, Callable, Dict, List, NewType, Optional, Tuple, Union
import torch

InputDataClass = NewType("InputDataClass", Any)

class CollataAndPad(object):
    r''' Arrange the data into the right format + add padding or trim where necessary.

    Args:
        max_len (`int`, `optional`, defaults to -1):
            Upper bound for sequence length. If it is -1 means that it will be
            calculated for each bach and set to the max length without upper limits.
        pad_id (`int`, `optional`, defaults to 0):
            What ID will be used to pad the inputs to max_len
    '''
    def __init__(self, max_len=-1, pad_id=0):
        self.max_len = max_len
        self.pad_id = pad_id


    def __call__(self, features: List[InputDataClass]) -> Dict[str, torch.Tensor]:
        batch = {}
        if self.max_len == -1:
            max_len = max([len(f['input_ids']) for f in features])
        else:
            max_len = min(self.max_len, max([len(f['input_ids']) for f in features]))

        batch['labels'] = torch.tensor([f["labels"][0:max_len] + [-100] * max(0, max_len - len(f['labels']))
                                        for f in features], dtype=torch.long)
        batch['input_ids'] = torch.tensor([f['input_ids'][0:max_len] + [self.pad_id] * max(0, max_len - len(f['input_ids']))
                                          for f in features], dtype=torch.long)
        batch['attention_mask'] = batch['input_ids'] != self.pad_id

        return batch

